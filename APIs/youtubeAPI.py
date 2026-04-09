from googleapiclient.discovery import build

apiKey = "AIzaSyCFGR-9TzlFz6SB5_u_l3MPAf2iITy-GeI"

youtube = build('youtube', 'v3', developerKey=apiKey)

request = youtube.channels().list(
    part = 'statistics', 
    forUsername = 'schafer5'
)

response = request.execute()

print(response)