import urllib.request
from pytube import YouTube
import re
import os

def SearchResults(Title,max_results):
    ListofVideos = []
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={Title.strip().replace(' ','')}")
    video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
    video_ids= list(dict.fromkeys(video_ids))
    for videos in video_ids:
        ListofVideos.append("https://www.youtube.com/watch?v="+videos)
    
    return ListofVideos[0:max_results]


def GetNames(Link):
    video = YouTube(Link)
    return video.title
    
def DownloadVideo(StreamChoice):
    dispath = os.getcwd()
    PathforDownload = dispath.strip()+"\Vids"
    StreamChoice.download(output_path = PathforDownload)
    return

def GetResolution(Link):
    yt = YouTube(Link)
    StreamList = yt.streams.filter(file_extension="mp4",progressive="True")
    StreamList = list(dict.fromkeys(StreamList))
    print("Choose a resolution to download: ")
    i = 1
    for stream in StreamList:
        print(f"{i} resolution: {stream.resolution}")
        i = i+1
    while True:
        try:
            ResolutionChoice = int(input("Your choice: "))
            if(0 > ResolutionChoice or ResolutionChoice > len(StreamList)):
                raise Exception
            else:
                return StreamList[ResolutionChoice-1]
        except:
            print("Enter a valid choice for resolution..")

def GetVidsDownloaded():
    path = os.getcwd()
    files = os.listdir(path.strip()+"\Vids")
    print("Videos downloaded are: ")
    for _ in files:
        print(_.split(".")[0])