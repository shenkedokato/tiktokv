from moviepy.editor import VideoFileClip

def crop_video(video_clip_paths,height,width,output_path):
    video= VideoFileClip(video_clip_paths)
    crop_X=(video.w/2)-width/2
    crop_y=(video.h/2)-height/2
    video=video.crop(x1=crop_X,y1=crop_y,width=width,height=height)
    video.write_videofile(output_path)

if __name__ =="__main__":
    crop_video("Video/m2.mp4",200,500, "hh.mp4")