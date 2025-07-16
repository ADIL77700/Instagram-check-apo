from fastapi import FastAPI
import requests
import random
import string

app = FastAPI()

def generate_username():
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(letters, k=4))

def check_instagram_username(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    return response.status_code == 404  # True = متاح

@app.get("/check")
def check():
    username = generate_username()
    available = check_instagram_username(username)
    return {
        "username": username,
        "status": "available" if available else "taken"
    }
