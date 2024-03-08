from moviepy.editor import *


class VideoFactory(VideoFileClip):
    def __init__(self, video_clip_path: str):
        super().__init__(video_clip_path)

    def add_audio(self, audio: AudioFileClip):
        """
        Mute audio before add audio to avoid CompositeAudio()
        CompositeAudio() : Combine all audios
        """
        self.set_audio(audio)

    def sub_video(self, start, end) -> VideoFileClip:
        """
        Expressed in seconds (15.35), in (min, sec), in (hour, min, sec), or as a
        string: '01:03:05.35'.
        If ``t_end`` is not provided, it is assumed to be the duration
        of the clip (potentially infinite).
        If ``t_end`` is a negative value, it is reset to
        ``clip.duration + t_end. ``. For instance: ::

            >>> # cut the last two seconds of the clip:
            >>> newclip = clip.subclip(0,-2)
        """
        result_sub = self.subclip(start, end)
        return result_sub

    def mute_audio(self):
        self.without_audio()

    def speed_up_video(self, speedx: float):
        self.fx(vfx.speedx, speedx)

    def split_screen_video(self, overlay_clip) -> CompositeVideoClip:
        """
        overlay_clip is a object in the class extends VideoClip
        clips_array return CompositeVideoClip()

        Format [[video1,video2]] to split vertical two video
        Format [[video1],[video2]] to split horizontal two video
        """

        # Duration of final video = duration of main video
        # If duration of overlay video < duration of main video, restart overlay video
        # Else cut overlay video
        if self.duration > overlay_clip.duration:
            sub_overlay = overlay_clip.subclip(0, self.duration - overlay_clip.duration)
            overlay_clip_final = concatenate_videoclips(
                [overlay_clip, sub_overlay], method="compose"
            )
        else:
            overlay_clip_final = overlay_clip.subclip(0, self.duration)

        return clips_array([[self], [overlay_clip_final]])

    def add_logo(
        self,
        logo_path: str,
        position: str = "right_bottom",
        height_logo: float = 40,
        color=(10, 12, 15),
    ) -> CompositeVideoClip:
        """
        4 Option position:
            - left_top
            - right_top
            - left_bottom
            - right_bottom
        """
        if position == "left_top":
            logo = (
                ImageClip(logo_path)
                .set_duration(self.duration)
                .resize(height=height_logo)
                .margin(left=20, top=20, opacity=0)
                .set_pos(("left", "top"))
            )
        elif position == "right_top":
            logo = (
                ImageClip(logo_path)
                .set_duration(self.duration)
                .resize(height=40)
                .margin(right=20, top=20, opacity=0)
                .set_pos(("right", "top"))
            )
        elif position == "right_bottom":
            logo = (
                ImageClip(logo_path)
                .set_duration(self.duration)
                .resize(height=40)
                .margin(right=20, bottom=20, opacity=0)
                .set_pos(("right", "bottom"))
            )
        elif position == "left_bottom":
            logo = (
                ImageClip(logo_path)
                .set_duration(self.duration)
                .resize(height=40)
                .margin(right=20, bottom=20, opacity=0)
                .set_pos(("left", "bottom"))
            )
        return CompositeVideoClip([self, logo], bg_color=color)

    def overlay_background(
        self, overlay_clip, position: tuple = (100, 60), sizex: float = 0.75
    ) -> CompositeVideoClip:
        """
        - overlay_clip is a object in the class extends VideoClip
        - Put main video among of overlay video
        - Set 2 argument position by tuple "()" like magin left_screen and top_screen
        - sizex is the percent of original frame main video
        """
        if self.duration > overlay_clip.duration:
            sub_overlay = overlay_clip.subclip(0, self.duration - overlay_clip.duration)
            overlay_clip_final = concatenate_videoclips(
                [overlay_clip, sub_overlay], method="compose"
            )
        else:
            overlay_clip_final = overlay_clip.subclip(0, self.duration)
        final_main_clip = self.set_position(position).resize(sizex)
        return CompositeVideoClip([overlay_clip, final_main_clip])

    def change_lum_contrast(
        self,
        brightness_factor: float = 0,
        lum: float = 0,
        contrast: float = 0,
        contrast_thr: float = 127,
    ):
        """
        vfx.colorx effect adjusts the color channels of the video based on the provided brightness factor

        - lum parameter controls the brightness of the video
        - contrast parameter adjusts the contrast
        - contrast_thr determines the threshold for contrast adjustment
        """
        brightness_factor = (
            brightness_factor  # Adjust as needed (higher values increase brightness)
        )
        color_adjusted_clip = self.fx(vfx.colorx, brightness_factor)
        final_clip = color_adjusted_clip.fx(
            vfx.lum_contrast, lum=lum, contrast=contrast, contrast_thr=contrast_thr
        )
        return final_clip

    def rotate_video(
        self, angle: float, unit: str = "deg", resample: str = "bicubic", expand=True
    ):
        """
        Change unit to 'rad' to define angles as radians.
        If the angle is not one of 90, 180, -90, -180 (degrees) there will be
        black borders. You can make them transparent with

        angle
          Either a value or a function angle(t) representing the angle of rotation

        unit
          Unit of parameter `angle` (either `deg` for degrees or `rad` for radians)

        resample
          One of "nearest", "bilinear", or "bicubic".

        expand
          Only applIf False, the clip will maintain the same True, the clip will be resized so that the whole
        """
        result = self.fx(vfx.rotate, angle, unit, resample, expand)
        return result

    def crop_video(
        self,
        x1=None,
        y1=None,
        x2=None,
        y2=None,
        width=None,
        height=None,
        x_center=None,
        y_center=None,
    ):
        """
        Returns a new clip in which just a rectangular subregion of the
        original clip is conserved. x1,y1 indicates the top left corner and
        x2,y2 is the lower right corner of the croped region.
        All coordinates are in pixels. Float numbers are accepted.

        To crop an arbitrary rectangle:

        >>> crop(clip, x1=50, y1=60, x2=460, y2=275)

        Only remove the part above y=30:

        >>> crop(clip, y1=30)

        Crop a rectangle that starts 10 pixels left and is 200px wide

        >>> crop(clip, x1=10, width=200)

        Crop a rectangle centered in x,y=(300,400), width=50, height=150 :

        >>> crop(clip,  x_center=300 , y_center=400,
                            width=50, height=150)

        Any combination of the above should work, like for this rectangle
        centered in x=300, with explicit y-boundaries:

        >>> crop(x_center=300, width=400, y1=100, y2=600)

        """
        result = self.fx(vfx.crop, x1, y1, x2, y2, width, height, x_center, y_center)
        return result


a = VideoFactory("Video/m2.mp4")
a.rotate(20).write_videofile("vl.mp4")
