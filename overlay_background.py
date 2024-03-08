import cv2
import moviepy.editor as mpe

lowerThird = "video/m2.mp4"
videoFile = "video/m1.mp4"
outputFile = "video/alpha.mp4"


def vdo_with_alpha(lowerThird, videoFile, outputFile):
    tmpVid = cv2.VideoCapture(videoFile)
    framespersecond = float(tmpVid.get(cv2.CAP_PROP_FPS))
    
    # video_clip = mpe.VideoFileClip(videoFile, target_resolution=(200, 500))
    video_clip = mpe.VideoFileClip(videoFile)
    
    overlay_clip = mpe.VideoFileClip(lowerThird).set_position((100, 60)).resize(0.75)
    
    final_video = mpe.CompositeVideoClip([ video_clip,overlay_clip])
    
    final_video.write_videofile(outputFile)



vdo_with_alpha(lowerThird, videoFile, outputFile)