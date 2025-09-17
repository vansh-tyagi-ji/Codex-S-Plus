try:
    # First, we import the library's top-level module
    import youtube_transcript_api

    # Now, we ask it to show us its file location
    print("--- SCRIPT STARTED ---")
    print(f"Python is importing 'youtube_transcript_api' from: {youtube_transcript_api.__file__}")
    print("--- SCRIPT FINISHED ---")

except Exception as e:
    print(f"An error occurred during import: {e}")