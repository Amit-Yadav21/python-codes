from pytube import youtube
url='https://www.youtube.com/watch?v=QC4sgzVPAho'
my_video=youtube(url)
print("********vodoe title*********")
# get video title
print(my_video.title)

print("********thumbnail image*********")
# get thumbnail image
print(my_video.thumbnail_url)

print("********Download video*********")
# get stream resolution
my_video=my_video.streams.get_highest_resolution()

my_video.download()

