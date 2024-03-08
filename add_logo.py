import moviepy.editor as mp

def add_logo(video_clip_paths,logo,output_path):
    
    video=mp.VideoFileClip(video_clip_paths)
    logo=(mp.ImageClip(logo)
            .set_duration(video.duration)
            .resize(height=40)
            # .margin(left=20,top=20,opacity=0)
            # .set_position(('left','top'))
        )
    
    logo.margin
    
    final=mp.CompositeVideoClip([video,logo])
    final.write_videofile(output_path)
add_logo("Video/m2.mp4",'Video/need.png',"hum.mp4")


