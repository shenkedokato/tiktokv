from moviepy.editor import concatenate_videoclips, VideoFileClip
import os 

def concatenate(video_clip_paths, output_path):
    clips=[]
    clip=os.listdir(video_clip_paths)
    for i in range(0,len(clip)):
        st=str(clip[i])
        if (st.find('.mp4'))!=-1:
            clips.append(VideoFileClip(video_clip_paths+"/"+clip[i]))
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path)
if __name__ =="__main__":
    concatenate("Video", "Video/concate.mp4")
    