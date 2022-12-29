from pytube import YouTube

url = 'https://www.youtube.com/watch?v=XXXXXXXXXXX'

yt = YouTube(url)

video = yt.get('mp4', '720p')

video.download('./')
