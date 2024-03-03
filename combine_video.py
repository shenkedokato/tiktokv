from moviepy.editor import VideoFileClip, clips_array

def split_screen_video(video_clip_paths, overlay_clip, output_path):
    video=VideoFileClip(video_clip_paths)
    overlay=VideoFileClip(overlay_clip)
    combined=clips_array([[video,overlay]])
    combined.write_videofile(output_path)

split_screen_video("Video/m2.mp4","Video/m1.mp4","hailong.mp4")