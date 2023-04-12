import os
import json
from yt_dlp import YoutubeDL
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Replace this with your own YouTube Data API key
API_KEY = os.getenv("YOUTUBE_API_KEY")

# Video URL
video_url_list = ['https://www.youtube.com/watch?v=hX0OUFJs9nQ', 'https://www.youtube.com/watch?v=nQ2A30cD3Q8']

# Download video and metadata
ydl_opts = {
    'best': '[height<=720p]',
    'writeinfojson': True,
    'outtmpl': 'videos/%(id)s.%(ext)s',
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_url_list)

# Function to fetch comments
def get_video_comments(video_id, max_results=100):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    results = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
        maxResults=max_results,
        order='relevance'
    ).execute()

    comments = []
    for item in results['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments

for video_url in video_url_list:
    # Get video ID from the URL
    video_id = video_url.split('v=')[-1]

    # Fetch comments
    try:
        comments = get_video_comments(video_id)
        with open(f"./videos/{video_id}_comments.json", "w") as outfile:
            json.dump(comments, outfile, indent=4)
        print("Comments saved.")
    except HttpError as e:
        print(f"An error occurred: {e}")
