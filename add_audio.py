from moviepy.editor import VideoFileClip, AudioFileClip
from get_audio import *

def add_audio(video_clip_path,audio_clip_path,output_path):
    audio=AudioFileClip(audio_clip_path)
    video=VideoFileClip(video_clip_path)
    final_clip=video.set_audio(audio)
    final_clip.write_videofile(output_path)

