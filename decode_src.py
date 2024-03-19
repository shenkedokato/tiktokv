import ffmpeg
from ffmpeg import *

def add_subtitle_to_video(soft_subtitle, subtitle_file, subtitle_language):
    # Define input streams
    video_input_stream = ffmpeg.input("video/m6.mp4")
    subtitle_input_stream = ffmpeg.input("hai.srt")

    # Define output video path
    output_video = f"output.mp4"

    # Extract subtitle track title
    subtitle_track_title = subtitle_file.replace(".srt", "")

    # Check if soft subtitles are to be added
    if soft_subtitle:
        # If soft subtitles, use `libx264` codec for video encoding
        stream = ffmpeg.output(video_input_stream, subtitle_input_stream, output_video, vcodec='libx264')
        # Run the ffmpeg command
        stream.run(overwrite_output=True)
    else:
        # If hard subtitles, use `subtitles` filter
        stream = ffmpeg.output(video_input_stream, output_video, vf=f"subtitles={subtitle_file}")
        # Run the ffmpeg command
        ffmpeg.run(stream, overwrite_output=True)

# Call the function to add subtitles to the video
add_subtitle_to_video(
    soft_subtitle=False,  # Add soft subtitles
    subtitle_file="hai.srt",  # Subtitle file path
    subtitle_language="en"  # Subtitle language
)