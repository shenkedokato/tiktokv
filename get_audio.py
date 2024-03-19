from moviepy.editor import VideoFileClip

def get_audio(video_clip_path, output_path):
    video=VideoFileClip(video_clip_path)
    audio=video.audio
    audio.write_audiofile(output_path)
    
get_audio("video/m6.mp4", "hai.mp3")
