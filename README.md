# youtube-transcript-summarizer
This uses ChatGPT and a YouTube transcript api to summarize videos.

## Inspiration
[5 AI Projects You Can Build This Weekend (with Python)](https://towardsdatascience.com/5-ai-projects-you-can-build-this-weekend-with-python-c57724e9c461)

## Requirements 
* Python 3.12
* An OpenAI account with an API key.  Instructions are at https://platform.openai.com/docs/quickstart

## Usage
```
usage: Summarizes YouTube videos [-h] url
Summarizes YouTube videos: error: the following arguments are required: url
```

## Arguments

### url
The url of a YouTube video.  The quickest way to get this is clicking the 'Share' button.

## Expected Output
A text summary should print on the screen.  The results are cached for a day so repeated calls for the next 24 hours should come back faster and not use up your OpenAI account.

## Example
```
python ./youtube-summerizer.py 'https://youtu.be/NhAP-b0FCqg?si=O0Cpo7BuJaHWtwUT'

Summarizing YouTube video: https://youtu.be/NhAP-b0FCqg?si=O0Cpo7BuJaHWtwUT
In this YouTube video, the creator demonstrates how to build a plywood cutting jig using minimal tools: a circular saw, a hand drill, and basic hand tools. The video addresses viewers' requests for a construction guide after showcasing the jig's functionality. The centerpiece of the jig is a knockdown sawhorse, designed for easy assembly and disassembly without hardware. It consists of eight wooden parts, including legs, a rail, and a loading arm, primarily made from 2x lumber and plywood. The creator explains the angles involved in constructing the sawhorse, emphasizing that while it may seem complex, it is manageable with a circular saw. The video details the process of cutting compound angles and creating a cutting jig that allows the circular saw to function like a miter saw. The creator also shares tips for drilling square holes and rounding corners using the circular saw. 
Throughout the video, the creator highlights the importance of precision in cutting and assembly, using jigs and guides to ensure accuracy. The final assembly involves attaching legs, spacers, and gussets, with careful attention to the positioning of tapered cleats to facilitate loading plywood.
The conclusion emphasizes that both the sawhorse built with basic tools and one made with a full workshop yield similar results, showcasing that creativity and resourcefulness can often replace the need for expensive tools. The video encourages viewers to embrace ingenuity in their woodworking projects.
```

## Improvements in the Future

* The ability to point to a list of videos and all get summarized at once.