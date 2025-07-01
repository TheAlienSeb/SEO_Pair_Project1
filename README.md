## README file
1) Name of Project

Trend-Sifter

2) What problem are you solving?

A large demographic of people struggle to view the hours of footage that pile up on Youtube (deaf, non-native English speakers, neurodivergent users). Especially in an age where flashy, fast-paced videos get the most attention, it is crucial that a tool that can scrape what’s relevant and deliver it in a digestible way is created.
(i.e. some people want a fast, easy way to experience youtube without the bloat/clickbait/flashy visuals)

3) Who / What does the project interface with?

 People?

Users who want a quick run-down of what’s currently trending, users who prefer reading, along with deaf, neurodivergent, or non native english speaking users

other systems? (APIs)

YouTube Data API v3 – supplies the channel profiles and statistics for trending videos
Gemini API – converts video transcripts into short summaries

Hardware?
Basic capabilities

What are the inputs?
A single CLI command called fetch/summarize
Consider extra inputs for number of videos, region, and depth of summary


What are the outputs?

Title
Channel
Viewer Stats
Summary
^ Will be printed to the terminal and saved into a database per video

List 5 steps to go from input -> output

Fetch: Call YouTube videos.list?chart=mostPopular → get top 10 video IDs with corresponding titles/channels
Pull captions: For each ID, fetch the video transcript
Gemini Feed: Prepare text for Gemini, consider length of transcript and break it down as needed
Summarize: Send chunks to Gemini, reinvoke Gemini again as needed to efficiently handle summary
Output: Save the entry in a database, then pretty-print them in the terminal.

What’s the biggest risk?

Need to handle videos that are excessively long and videos without transcripts/captions. How will we output and save in these cases?

How will you know you’re successful?

We will know if we have achieved our goal when we are able to print solid, coherent summaries for the correct corresponding videos. Being able to understand and get a rundown on all the videos is the ultimate use for this tool.




Two tables, one for the initial list with the first top 10. 

Table1 = TrendingList

Each video: ID, Title, Views, Desc,  (The Layout)


Table2 = Summerized videos


Each Video: IOD







