from moviepy.editor import *
  
def speed_up_video(video_clip_paths,speedx,output_path):
    clip = VideoFileClip(video_clip_paths)  
    final_clip = clip.fx( vfx.speedx, speedx)  
    final_clip.write_videofile(output_path,fps=60)
if __name__ =="__main__":
    speed_up_video("Video/concate.mp4",2, "Video/concate.mp4")