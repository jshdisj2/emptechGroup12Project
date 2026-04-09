import os
import json
from datetime import datetime
from google import genai 
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-3.1-flash-lite-preview")

LIMIT = 450
USAGE_FILE = "usage.json"

def loadUsage():
    try:
        with open(USAGE_FILE, "r") as f:
            data = json.load(f)
    except:
        data = {"date": "", "tokens": 0}

    today = datetime.now().strftime("%Y-%m-%d")

    if data["date"] != today:
        data = {"date": today, "tokens": 0}
    
    return data

def saveUsage(tokens):
    with open(USAGE_FILE, "w") as f:
        json.dump(tokens, f)

usage = loadUsage()
while True:
    if usage["tokens"] >= LIMIT:
             print("Token limit reached for today. Please try again tomorrow.")
             break
    
    remaining = LIMIT - usage["tokens"]
    print(f"Remaining tokens for today: {remaining}")

    message = input("You: ")
    if message.lower() == "exit":
        break
    
    try:
        response = chat.send_message(message)
        print("AI: ", response.text)

        usage["tokens"] += 1
        saveUsage(usage)
        
    except Exception as e:
        print("Error: ", e)