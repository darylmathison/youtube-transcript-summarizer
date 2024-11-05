import datetime
import os
import argparse
import re

from dogpile.cache import make_region
from youtube_transcript_api import YouTubeTranscriptApi
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_region():
    cache_dir = os.path.join(os.environ.get("HOME"), ".youtube_cache")
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    return make_region().configure(
        "dogpile.cache.dbm",
        arguments={"filename": os.path.join(cache_dir, "cachefile.dbm")},
        expiration_time=datetime.timedelta(days=1),
    )


region = create_region()

prompt = """Give a detailed summary of this YouTube video transcript, covering all the main points in about 250 words. Include the primary arguments, conclusions, and any noteworthy examples used.
### Here is my transcript in text:
{transcript}
"""

@region.cache_on_arguments()
def summarize(transcript):
    query = prompt.format(transcript=transcript)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query},
        ],
        temperature=0.25,
    )
    return response.choices[0].message.content

@region.cache_on_arguments()
def get_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)

def main():
    parser = argparse.ArgumentParser("Summarizes YouTube videos")
    parser.add_argument("url", help="URL of YouTube video")
    args = parser.parse_args()

    print(
        f"Summarizing YouTube video: {args.url}"
    )

    video_id_regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(video_id_regex, args.url)

    if match:
        video_id = match.group(1)
    else:
        video_id = None

    if video_id:
        transcript = "\n".join([ record["text"] for record in get_transcript(video_id)])
        summary = summarize(transcript)
        print(summary)

if __name__ == "__main__":
    main()