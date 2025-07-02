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
from dotenv import load_dotenv
import os

load_dotenv()                # pulls key-value pairs out of .env into the real environment
# api_key = os.getenv("YOUTUBE_CLIENT_API")

# API_KEY = api_key # ←—— paste the key you created in Google Cloud
# API_SERVICE_NAME = "youtube"
# API_VERSION = "v3"

# def youtube() -> None:
#     youtube = build(
#         API_SERVICE_NAME,
#         API_VERSION,
#         developerKey=API_KEY          # <-- key goes here instead of credentials object
#     )

#     request = youtube.videos().list(
#         part="snippet,contentDetails,statistics",
#         chart="mostPopular",
#         regionCode="US",              # change to e.g. "TW" or "GB" if you want
#         maxResults=10                 # optional; default 5, max 50
#     )
#     #We found you cannot filter for captions through a top trending access point get request. Must first get the list of trending
#     #Then search (Search video endpoint) them, and make sure to only return the videos that have captions enabled
#     #2. If it’s somebody else’s video (most cases) → use an unofficial transcript puller
#     # Because the official API bars you from other people’s caption files, developers lean on the player caption end-point.
#     # A tiny library called youtube-transcript-api wraps that for you:


#     response = request.execute()

#     print(response)
#     for i, item in enumerate(response["items"], 1):
#         title   = item["snippet"]["title"]
#         channel = item["snippet"]["channelTitle"]
#         views   = item["statistics"]["viewCount"]
#         print(f"{i:2}. {title}  —  {channel}  ({views} views)")


from googleapiclient.discovery import build

API_SERVICE_NAME = "youtube"
API_VERSION      = "v3"
API_KEY          = os.getenv("YOUTUBE_CLIENT_API")

def fetch_trending_videos() -> list[dict]:
    VALID_CODES = {
        "AE","AR","AT","AU","AZ","BA","BE","BG","BH","BO","BR","BY","CA","CH","CL","CO","CR",
        "CZ","DE","DK","DO","DZ","EC","EE","EG","ES","FI","FR","GB","GE","GH","GR","GT","HK",
        "HN","HR","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KR","KW","KZ",
        "LB","LI","LK","LT","LU","LV","LY","MA","ME","MK","MT","MX","MY","NG","NI","NL","NO",
        "NZ","OM","PA","PE","PH","PK","PL","PR","PT","PY","QA","RO","RS","RU","SA","SE","SG",
        "SI","SK","SV","TH","TN","TR","TW","TZ","UA","UG","US","UY","VE","VN","YE","ZA","ZW"
    }   

    """Hit the YouTube Data API and return the raw `items` list."""
    while True:
        user_input = input("Choose how many trending videos you want (1-50): ").strip()
        try:
            max_results = int(user_input)
            if 1 <= max_results <= 50:
                break                       # ✅ got a good integer, exit loop
            else:
                print("Please enter a number from 1 to 50.")
        except ValueError:
            print("That’s not an integer. Try again.")
    while True:
        region_code = input("Enter a 2-letter region code (e.g. US, GB): ").strip().upper()
        if region_code in VALID_CODES:
            break                          # ✅ good code
        print("Invalid code—please try again.")

    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
    response = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode=region_code,
        maxResults=max_results     # API max is 50
    ).execute()
    return response["items"]

