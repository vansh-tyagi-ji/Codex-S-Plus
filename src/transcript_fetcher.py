import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
video_url = "https://www.youtube.com/watch?v=kCc8FmEb1nY"  

print("Starting transcript fetch...")

# 6. Use a try...except block to gracefully handle errors
try:
   
    video_id = video_url.split("v=")[1].split("&")[0] # <-- FILL THIS IN

    transcript_list = [] 
    fetcher = YouTubeTranscriptApi()
    transcript_list = fetcher.fetch(video_id)

    full_transcript = "" # <-- FILL THIS IN
    for dict in transcript_list:
        full_transcript += dict.text + " "
    print("Transcript fetched successfully!")
    print("-" * 20) # A separator line for clean output
    print(full_transcript)

except Exception as e:
    print("\nAn error occurred:")
    print(e)
    print("\nThis could be because the video does not have a transcript available.")