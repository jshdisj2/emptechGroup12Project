from google import genai 

client = genai.Client(api_key="AIzaSyDXEZz5RYl56gwLh7hslg2odF9TR-KPvqw")

chat = client.chats.create(model="gemini-3.1-flash-lite-preview")

while True:
    message = input("You: ")
    if message == "exit":
        break

    response = chat.send_message(message)
    print(response.text)