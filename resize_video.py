from moviepy.editor import VideoFileClip,vfx

clip=VideoFileClip("Video/m2.mp4",target_resolution=(100, 200))
clip.write_videofile("final.mp4")

