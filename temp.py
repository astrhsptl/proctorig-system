from moviepy.editor import *

clip1 = VideoFileClip("/home/nia/Desktop/proctorig-system/server/media/file13.webm")
clip2 = VideoFileClip("/home/nia/Desktop/proctorig-system/server/media/file14.webm")

final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("result.webm")