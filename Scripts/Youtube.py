#GET https://www.googleapis.com/youtube/v3/search

# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

# -*- coding: utf-8 -*-
"""
List the top-trending YouTube videos (no OAuth needed).
"""

from googleapiclient.discovery import build
from youtube_transcript_api import yttapi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

API_KEY = "AIzaSyBaPuR_fwX1StVhMuWHQU3JHDIAEKFSYQk"      # ←—— paste the key you created in Google Cloud
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def main():
    regionCode = input("Enter region code (e.g. US, GB, IN): ").strip().upper()
    maxResults = input("Enter a # of desired results (1 - 50): ").strip()
    
    youtube = build(
        API_SERVICE_NAME,
        API_VERSION,
        developerKey=API_KEY          # <-- key goes here instead of credentials object
    )

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode=regionCode,              # change to e.g. "TW" or "GB" if you want
        maxResults=maxResults                 # optional; default 5, max 50
    )

    response = request.execute()

    # print(response)
    for i, item in enumerate(response["items"], 1):
        title   = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        views   = item["statistics"]["viewCount"]
        video_id = item["id"]
        url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"{i:2}. {title}  —  {channel}  ({views} views)")

        try:
            transcript = yttapi.get_transcript(video_id)
            transcript_text = ' '.join([entry['text'] for entry in transcript[:5]])  # Show first 5 entries
            print("    Transcript (first few lines):", transcript_text)
        except (TranscriptsDisabled, NoTranscriptFound):
            print("    Transcript not available.")

if __name__ == "__main__":
    main()
