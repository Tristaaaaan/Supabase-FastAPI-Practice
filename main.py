from fastapi import FastAPI
from models import User, Item
import bcrypt
from db.supabase import create_supabase_client

app = FastAPI()

supabase = create_supabase_client()

@app.post("/register/")
async def register(user: User):
    try:
        # Convert email to lowercase
        user_email = user.email.lower()
        
        hashed_password = bcrypt.hashpw(user.password, bcrypt.gensalt())
        
        res = supabase.auth.sign_up({
        "email": user_email,
        "password": user.password,
        })
        
        return res.get("access_token")

    except Exception as e:
        print("Error: ", e)
        return {"message": "User creation failed"}

@app.post("/login")
async def login(user: User):

    global access_token

    try:
        # Convert email to lowercase
        user_email = user.email.lower()
        
        #hashed_password = bcrypt.hashpw(user.password, bcrypt.gensalt())
    
        getUserData = supabase.auth.sign_in_with_password({"email": user_email,"password": user.password})

        #idd = supabase.auth.user().id
        user_id = getUserData.user.id
        access_token = getUserData.session.access_token
        # supabase.postgrest.auth(access_token)

        # money_spent = 432432
        # category = 'Sports'

        # data = supabase.table("expenses").insert({"money_spent": money_spent, "category": category}).execute()

        # print("Item added")

        return user_id, access_token
    
    except Exception as e:
        print("Error: ", e)
        return {"message": "User creation failed"}

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
        supabase.postgrest.auth(items.access_token)

        data = supabase.table("expenses").insert({"money_spent": int(items.money_spent), "category": items.category, "user_id": items.user_id}).execute()
        
        print("Item Added")

        return data
    except Exception as e:
        print("Error: ", e)
        return {"message":"Adding of Item Failed"}