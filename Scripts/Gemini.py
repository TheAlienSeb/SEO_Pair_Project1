import os 
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()  
my_api_key = os.getenv('GEMINI_API_KEY')

genai.api_key = my_api_key



# WRITE YOUR CODE HERE

# Create an genAI client using the key from our environment variable
client = genai.Client(
    api_key=my_api_key,
)

# Specify the model to use and the messages to send
response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
      system_instruction="""
      You are a comedic yet intuitve news editor. Your job is to take any dialogue transcript we give you and turn it into 
      a quick summary able to be read is less than 2-3 minutes. If for whatever reason you do not get a transcript to simplify,
      absolutely do not send anything back. Do not say or write anything back to the user. Failure to do so will result in your termination.
      """
    ),
    contents="What are the advantages of pair programming?",
)

print(response.text)
