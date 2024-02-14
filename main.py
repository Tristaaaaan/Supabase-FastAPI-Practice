from fastapi import FastAPI
from models import User, Item
import bcrypt
from db.supabase import create_supabase_client
import jwt
import time

app = FastAPI()

supabase = create_supabase_client()


@app.post("/register")
async def register(user: User):
    try:
        # Convert email to lowercase
        user_email = user.email.lower()
        
        #hashed_password = bcrypt.hashpw(user.password, bcrypt.gensalt())
        
        res = supabase.auth.sign_up({
        "email": user_email,
        "password": user.password,
        })


    except Exception as e:
        print("Error: ", e)
        return e #{"message": "User creation failed"}

@app.post("/login")
async def login(user: User):

    try:
        # Convert email to lowercase
        user_email = user.email.lower()
        
        #hashed_password = bcrypt.hashpw(user.password, bcrypt.gensalt())
    
        getUserData = supabase.auth.sign_in_with_password({"email": user_email,"password": user.password})

        user_id = getUserData.user.id
        access_token = getUserData.session.access_token
        refresh_token = getUserData.session.refresh_token

        return user_id, access_token, refresh_token
    
    except Exception as e:
        print("Error: ", e)
        return e #{"message": "User creation failed"}


@app.post("/signout")
async def signout():
    try:
        session = supabase.auth.sign_out()

    except Exception as e:
        print("Error: ", e)
        return {"message": "User creation failed"}


@app.post("/add")
async def addItem(items: Item):
    try:
        # Decode the access token
        decoded_token = jwt.decode(items.access_token, options={"verify_signature": False})

        # Get the expiration time from the decoded token
        expiration_time = decoded_token.get("exp")

        # Get the current time
        current_time = int(time.time())

        # Check if the token is expired
        is_expired = current_time > expiration_time

        if is_expired:
            # If the Access Token is expired, it will refresh the session.
            # You have to retrieve the new Access Token and Refresh Token
            res = supabase.auth.refresh_session(items.refresh_token)
            print("Access token is expired")
            return res
        

        else:
            # If the Access Token is not expired, it will push the data
            # to the database
            supabase.postgrest.auth(items.access_token)

            data = supabase.table("expenses").insert({"money_spent": int(items.money_spent), "category": items.category, "user_id": items.user_id}).execute()
            
            return data

    except Exception as e:
        print("Error: ", e)
        return e #{"message": "Adding of Item Failed"}