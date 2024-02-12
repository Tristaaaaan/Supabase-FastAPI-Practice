from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class Item(BaseModel):
    money_spent: float
    category: str
    user_id: str
    access_token: str