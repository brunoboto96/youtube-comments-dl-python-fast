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
video_url_list = ['https://youtube.com/watch?v=keOaQm6RpBg']

# Download video and metadata
ydl_opts = {
    'best': '[height<=720p]',
    'writeinfojson': True,
    'outtmpl': 'videos/%(id)s.%(ext)s',
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_url_list)

# Function to fetch comments
def get_video_comments(video_id, max_results_per_page=100, max_pages=None):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Initialize empty list to store comments and replies
    comments = []

    # Initialize credit spent
    credit_spent = 0

    # Fetch comments with pagination
    page_token = None
    page_count = 0

    while True:
        results = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id,
            textFormat='plainText',
            maxResults=max_results_per_page,
            order='relevance',
            pageToken=page_token
        ).execute()

        # Add the cost of the API request to the credit spent
        credit_spent += 3

        # Add comments and their replies to the list
        for item in results['items']:
            comment = {
                'text': item['snippet']['topLevelComment']['snippet']['textDisplay'],
                'replies': []
            }

            # Add replies to the comment
            if 'replies' in item:
                for reply in item['replies']['comments']:
                    reply_text = reply['snippet']['textDisplay']
                    comment['replies'].append(reply_text)

            comments.append(comment)

        # Check if there is a nextPageToken
        if 'nextPageToken' in results and (max_pages is None or page_count < max_pages):
            page_token = results['nextPageToken']
            page_count += 1
        else:
            break

    return comments, credit_spent


for video_url in video_url_list:
    # Get video ID from the URL
    video_id = video_url.split('v=')[-1]

    # Fetch comments
    try:
        comments, credit_spent = get_video_comments(video_id, max_results_per_page=100, max_pages=10)
        print(f"Total credit spent: {credit_spent}")

        with open(f"./videos/{video_id}_comments.json", "w") as outfile:
            json.dump(comments, outfile, indent=4)
        print("Comments saved.")
    except HttpError as e:
        print(f"An error occurred: {e}")
