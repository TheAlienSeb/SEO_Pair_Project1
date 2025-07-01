import requests
import pandas as pd
import sqlalchemy as db

#pulls ID for 500 top stories
# response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
# topStories = response.json()

import json, pathlib

data = json.loads(
    (pathlib.Path(__file__).resolve().parent.parent           # …/project-root/
     / "JSON_Sample" / "Response.txt")                       # add folders / file
    .read_text(encoding="utf-8")
)

df = pd.json_normalize(data["items"])
# columns now look like:
# ['id', 'snippet.title', 'snippet.publishedAt', 'contentDetails.caption', …]

# 3. keep only the parts you care about
cols = ["id",
        "snippet.title",
        "snippet.publishedAt",
        "contentDetails.duration",
        "contentDetails.caption",
        "statistics.viewCount",
        "statistics.likeCount"]
df = df[cols]

# 4. convert caption flag to a real boolean and filter
df["has_caption"] = df["contentDetails.caption"] == "true"
captioned = df[df["has_caption"]]

engine = db.create_engine('sqlite:///SumVids.db')

df.to_sql('summeries', con=engine, if_exists='replace', index=False)


with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM summeries;")).fetchall()
   print(pd.DataFrame(query_result))




