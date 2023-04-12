
# 🚀 YouTube Video Downloader & Metadata Extractor 🌟

This Python script allows you to download YouTube videos along with their metadata, including information such as duration, likes, views, and comments. It uses the `yt_dlp` library for downloading videos and metadata, and the YouTube Data API for fetching comments.

## 📚 Table of Contents

-   [Requirements](https://github.com/brunoboto96/youtube-comments-dl-python-fast#requirements)
-   [Setup](https://github.com/brunoboto96/youtube-comments-dl-python-fast#setup)
-   [Usage](https://github.com/brunoboto96/youtube-comments-dl-python-fast#usage)
-   [Disclaimer](https://github.com/brunoboto96/youtube-comments-dl-python-fast#disclaimer)

## 📦 Requirements

-   Python 3.6 or higher
-   `yt_dlp` library
-   `google-api-python-client` library
-   `python-dotenv` library
-   A YouTube Data API key

## 🔧 Setup

1.  Clone this repository:
    
    
    `git clone https://github.com/yourusername/youtube-video-downloader.git` 
    
2.  Change into the project directory:
    
    
    `cd youtube-video-downloader` 
    
3.  Install the required libraries:
    
    
    `pip install yt_dlp google-api-python-client python-dotenv` 
    
4.  Create a `.env` file in the project directory and add your YouTube Data API key:
    
    
    `YOUTUBE_API_KEY=your_api_key_here` 
    

## 🚀 Usage

1.  Update the `video_url_list` variable in the Python script with the URLs of the videos you want to download:
    
    
    `video_url_list = [
        'https://www.youtube.com/watch?v=example1',
        'https://www.youtube.com/watch?v=example2'
    ]` 
    
2.  Run the script:
    
    
    `python youtube_video_downloader.py` 
    
3.  Videos will be downloaded to the `videos` folder, and the metadata and comments will be saved as JSON files in the same folder.
    

## ⚠️ Disclaimer

Please note that downloading copyrighted material without permission is illegal in many jurisdictions. You should only use this script to download content that you are authorized to access and store. By using this script, you are solely responsible for complying with applicable laws and regulations.

----------

🎉 Congratulations! You now have a fully functional YouTube video downloader and metadata extractor! Enjoy and use responsibly! 🌟