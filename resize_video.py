from moviepy.editor import VideoFileClip,vfx
import moviepy.video.fx.all as fx

clip=VideoFileClip("Video/m2.mp4").fx(fx.resize, 0.5)
clip.write_videofile("final.mp4")

