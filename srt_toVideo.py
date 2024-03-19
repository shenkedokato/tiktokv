import ffmpeg
from ffmpeg import *

def add_subtitle_to_video(soft_subtitle, subtitle_file,  subtitle_language):
    video_input_stream = ffmpeg.input("video/m6.mp4")
    subtitle_input_stream = ffmpeg.input("hai.srt")
    output_video = f"output.mp4"
    subtitle_track_title = subtitle_file.replace(".srt", "")

    if soft_subtitle:
        stream = ffmpeg.output(video_input_stream, subtitle_input_stream, output_video,vcodec='libx264')
        stream.run(overwrite_output=True)
    else:
        stream = ffmpeg.output(video_input_stream, output_video,

                               vf=f"subtitles={subtitle_file}")

        ffmpeg.run(stream, overwrite_output=True)


add_subtitle_to_video(
    soft_subtitle=True,
    subtitle_file="hai.srt",
    subtitle_language="en"
)