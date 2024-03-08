from moviepy.editor import VideoFileClip

def sub_video(video_clip_paths,start,end,output_path):
    input_video=VideoFileClip(video_clip_paths)
    input_video=input_video.subclip(start,end)
    input_video.write_videofile(output_path)
sub_video("video/m1.mp4", (0,1),(0,8),"vl.mp4")