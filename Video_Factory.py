from moviepy.editor import VideoFileClip,AudioFileClip

class VideoFactory:
    def __init__(self,video_clip_path):
        self.video=VideoFileClip(video_clip_path)
        self.audio=video.audio

    def add_audio(self,audio_clip_path):
        audio=AudioFileClip(audio_clip_path)
        return self.video.set_audio(audio)

    def sub_video(start,end):
        return self.video.subclip(start,end)

    def mute_audio():
        return self.video.without_audio()
    
    def speed_up_video(speedx):
        return self.video.fx( vfx.speedx, speedx) 

    def split_screen_video(overlay_clip):
        overlay=VideoFileClip(overlay_clip)
        self.video=clips_array([[self.video],[overlay]])
        return video
        
    def add_logo(self,logo_path):
        logo=(mp.ImageClip(logo)
            .set_duration(video.duration)
            .resize(height=50)
            .margin(right=20,top=20,opacity=0)
            .set_pos('right','top'))
        video=mp.CompositeVideoClip([video,logo])

a= VideoFactory("Video/m1.mp4")
a.sub_video
a.video.write_videofile("vl.mp4")






