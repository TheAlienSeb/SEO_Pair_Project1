# Trend-Digest

![Icon of arrow pointing with an upwards trend](https://cdn.iconscout.com/icon/free/png-256/free-trending-icon-download-in-svg-png-gif-file-formats--up-arrow-direction-growth-user-interface-pack-icons-1502173.png "Trending Icon")

**Your gateway to understanding what's trending on YouTube—without the clutter**

**Trend-Digest** is a CLI that fetches the top trending videos in your region in real time, and provides readable summaries for each of them. 
We know that a large demographic of people struggle to view the hours of footage that pile up on Youtube. Especially in an age where flashy, fast-paced videos get the most attention, it is crucial that a tool can deliver relevant, digestible stories.
(i.e. people want a fast, easy way to experience youtube without the bloat/clickbait/flashy visuals)

- Deaf or hard-of-hearing users  
- Non-native English speakers  
- Neurodivergent individuals  
- Busy people who want quick insights

---

## Interfaces

### People
- Users who prefer reading over watching
- Users with accessibility needs
- Anyone looking for a quick summary

### Systems (APIs)

- **YouTube Data API V3** – supplies the channel profiles and statistics for trending videos
- **Gemini API** – converts video transcripts into short summaries

### Hardware
- This is all run in just your terminal!

---

## Inputs 
A single CLI command called fetch/summarize
- Will prompt user for region code (e.g. US)
- Will prompt user for number of top trending videos (between 1 - 50)

---

## Outputs

Outputs will be in the following format:
- Title - (Channel Name) (Viewer Statistics)
- Summary of the video
All to be printed to the terminal and saved into a database on a video basis

---

## Step-by-step

Here is a high level overview of how this script works:
- Fetch: Call YouTube videos.list?chart=mostPopular → get top 10 video IDs with corresponding titles/channels
- Pull captions: For each ID, fetch the video transcript
- Gemini Feed: Prepare text for Gemini, consider length of transcript and break it down as needed
- Summarize: Send chunks to Gemini, reinvoke Gemini again as needed to efficiently handle summary
- Output: Save the entry in a database, then pretty-print them in the terminal.

---

## Program Risks

How do we handle exceptionally long videos, or videos without captions? Currently, we have set to display "no captions found" in the extreme cases so as not to disrupt the output flow

---

## How will you know you’re successful?

We will know if we have achieved our goal when we are able to print solid, coherent summaries for the correct corresponding videos. Being able to understand and get a rundown on all the videos is the ultimate use for this tool.

---

## How our data is stored
Using pandas, we will store two tables:
First is the initial list with the initial top 10. 

Table1 = TrendingList

Each record contains: ID, Title, Views, Desc, (The Layout)

Next is the records of the video summaries
Table2 = Summarized videos


Each Video: IOD


Current Goals:


Connecting Youtube

Filtering Youtube for "caption only" trending videos

Connecting Gemini API to take transcripts of the trending videos 

Create DB to hold the trending videos as well as its summerized text













