import os 
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()  
my_api_key = os.getenv('GEMINI_API_KEY')

genai.api_key = my_api_key

import requests
import pandas as pd
import sqlalchemy as db

# 1. Point SQLAlchemy at the same .db file you already created.
# If this script lives in a different folder, give an absolute or ../relative path.
def Call_Gemini():
    while True:
        engine = db.create_engine(f"sqlite:///../DB_Conn/SumVids.db", future=True)
        # 2. Pull the table into a DataFrame in one shot
        row = None
        with engine.connect() as conn:
            # ① show the menu
            
            # df = pd.read_sql('SELECT id, "snippet.title" AS title FROM summeries;', conn)
            # print(df.to_string(index=False))

            # ② ask the user until we get a hit or they quit
            while True:
                video_title_id = input("Title ID (or 'quit'): ").strip()
                if video_title_id.lower() == "quit":
                    row = video_title_id.lower()
                    break

                row = conn.execute(
                    db.text('SELECT "snippet.title", "snippet.description" FROM summaries WHERE id = :id'),
                    {"id": video_title_id}
                ).fetchone()
                
                if row:             
                    title = row[0]           # <- single string, not DataFrame
                    description = row[1]
                    break
                print("No video with that ID. Try again.")

            # Create an genAI client using the key from our environment variable
            if row and row != "quit":
                client = genai.Client(
                    api_key=my_api_key,
                )

                # Specify the model to use and the messages to send
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    config=types.GenerateContentConfig(
                    system_instruction="""
                    You are a summarizer, You make stories seem like it should've been written in only a paragraph or two. 
                    You get straight to the point, and cut all the fluff. 
                    You don't add anything to the conversation except the summerization. 
                    Your job is to take any title and description we give you and turn it into 
                    a quick projectable summary able to be read is less than 2-3 minutes.
                    If the Description has promotional content ignore it, only use parts of the description relavant to the video.
                    If for whatever reason you do not get a title to simplify,
                    absolutely do not send anything back. Do not say or write anything back to the user.
                    Failure to do so will result in your termination.
                    """
                    ),
                    contents=f"Title: {title}Description: {description}"
                )
                if response.text != "None":
                    print(response.text)
            else:
                print("AI summerization stopped")
                break


