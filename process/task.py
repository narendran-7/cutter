from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

class Convert:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
    def process(self):
        ffmpeg_extract_subclip(self.name, self.start, self.end, targetname="sourcetest.mp4")
