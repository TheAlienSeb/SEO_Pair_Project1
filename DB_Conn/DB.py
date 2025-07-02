import requests
import pandas as pd
import sqlalchemy as db
from datetime import date, timedelta

#pulls ID for 500 top stories
# response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
# topStories = response.json()
import sys
import json, pathlib
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent        # …/SEO_Pair_Project1
scripts_dir  = project_root / "Scripts"                      # …/SEO_Pair_Project1/Scripts

sys.path.append(str(project_root))    # you already had this
sys.path.append(str(scripts_dir))     # ← **add this line**
from Youtube import fetch_trending_videos
def Grab_Titles():
    items = fetch_trending_videos()

    # 2. build DataFrame
    df = pd.json_normalize(items)
    # columns now look like:
    # ['id', 'snippet.title', 'snippet.publishedAt', 'contentDetails.caption', …]

    # 3. keep only the parts you care about
    
    cols = ["id",
            "snippet.title",
            "snippet.publishedAt",
            "snippet.channelTitle",
            "snippet.description",
            "contentDetails.duration",
            "contentDetails.caption",
            "statistics.viewCount",
            "statistics.likeCount"]
    df = df[cols]

    # 4. convert caption flag to a real boolean and filter
    df["has_caption"] = df["contentDetails.caption"] == "true"
    captioned = df[df["has_caption"]]

    engine = db.create_engine('sqlite:///SumVids.db')

    df.to_sql('summaries', con=engine, if_exists='replace', index=False)


    today_str      = date.today().isoformat()               # '2025-07-03'
    yesterday_str  = (date.today() - timedelta(days=1)).isoformat()

    sql = '''
    SELECT "id" as ID, "snippet.title" AS Title, "snippet.channelTitle" AS Channel_Name, "statistics.viewCount" AS Views, "statistics.likeCount" AS Likes
    FROM   summaries
    WHERE  "snippet.publishedAt" LIKE :today || '%'
    OR  "snippet.publishedAt" LIKE :yesterday || '%'
    '''
    
    with engine.connect() as conn:
        rows = conn.execute(
            db.text(sql),
            {"today": today_str, "yesterday": yesterday_str}
        ).fetchall()
    df = df.rename(columns=lambda c: c.split('.')[-1])
    print()
    print(pd.DataFrame(rows).astype(str).to_string(index=False, header=True, justify='left'))



