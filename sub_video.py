from moviepy.editor import VideoFileClip

def sub_video(video_clip_paths,start,end,output_path):
    input_video=VideoFileClip(video_clip_paths)
    final_clip=input_video.subclip(start,end)
    final_clip.write_videofile(output_path,fps=60)