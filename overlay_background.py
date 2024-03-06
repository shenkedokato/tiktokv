import cv2
import moviepy.editor as mpe

lowerThird = "Video/need.png"
videoFile = "video/m2.mp4"
outputFile = "alpha.mp4"


def vdo_with_alpha(lowerThird, videoFile, outputFile):
    tmpVid = cv2.VideoCapture(videoFile)
    framespersecond = float(tmpVid.get(cv2.CAP_PROP_FPS))
    
    video_clip = mpe.VideoFileClip(videoFile, target_resolution=(200, 500))
    
    overlay_clip = mpe.ImageClip(lowerThird).set_duration(video_clip.duration)
    
    final_video = mpe.CompositeVideoClip([ overlay_clip,video_clip])
    
    final_video.write_videofile(
        outputFile,
        fps=framespersecond,
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
        threads=6
    )



vdo_with_alpha(lowerThird, videoFile, outputFile)