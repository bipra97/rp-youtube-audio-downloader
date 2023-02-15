from pytube import YouTube
from pytube import Search
import os
import wave
import struct


download_path = r"C:\Users\{0}\Downloads\Sunday_Suspense".format(os.getlogin())
url_txt_path = r'C:\Users\{0}\OneDrive\Desktop\url.txt'.format(os.getlogin())

#download and coverting the file from .mp4 to .mp3
def download_video(download_path,strs):
    
    old_file_name = strs[1].download(output_path=download_path)
    new_file_name = old_file_name.replace('.mp4','.mp3')
    os.rename(old_file_name, new_file_name)
    print("Downloaded!!!")


#Searching a keyword and getting the videoId to make the youtube URL
# def search_download():
#     search_results = Search("Taranath Tantrik")
#     s = search_results.results
#     for i in range(0, len(s)):
#         string = str(s[i])
#         string = string[41:].replace(">","")
#         url = 'https://www.youtube.com/watch?v='+ string
#         yt = YouTube(url)
#         strs = yt.streams.filter(only_audio=True)
#         download_video(download_path,strs)

#open the url.txt file to get the URLs of videos
with open(url_txt_path) as f:
    lines = f.readlines()

for i in range(0,len(lines)):
    yt = YouTube(lines[i])
    strs = yt.streams.filter(only_audio=True)
    download_video(download_path,strs)



# stream =  yt.streams.get_audio_only()
# stream.download(output_path=download_path)



