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

API_KEY = ""      # ←—— paste the key you created in Google Cloud
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def main() -> None:
    youtube = build(
        API_SERVICE_NAME,
        API_VERSION,
        developerKey=API_KEY          # <-- key goes here instead of credentials object
    )

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",              # change to e.g. "TW" or "GB" if you want
        maxResults=10                 # optional; default 5, max 50
    )

    response = request.execute()

    print(response)
    for i, item in enumerate(response["items"], 1):
        title   = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        views   = item["statistics"]["viewCount"]
        print(f"{i:2}. {title}  —  {channel}  ({views} views)")

if __name__ == "__main__":
    main()
