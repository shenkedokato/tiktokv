from moviepy.editor import VideoFileClip

def mute_audio(video_clip_paths,output_path):
    final=VideoFileClip(video_clip_paths).without_audio()
    final.write_videofile(output_path)

mute_audio("Video/m2.mp4","vl.mp4")