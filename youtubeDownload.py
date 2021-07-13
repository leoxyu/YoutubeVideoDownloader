# basic youtube video downloading script using pytube api
# https://pytube.io/
from pytube import YouTube

videoURL = input("Enter Youtube URL: \n")
video = YouTube(videoURL)

print("\nTitle: " + video.title)
print(video.author)

option = input("\nContinue? (y/n) \n")
if option == "y":
    filename = input("\nFilename (leave blank for video title): ")
    if filename == "":
        print("\nDownloading...", end="\r")
        video.streams.get_highest_resolution().download(r"C:\Users\Leo\Desktop\YoutubeDownload\output", video.title)
    else:
        print("\nDownloading...", end="\r")
        video.streams.get_highest_resolution().download(r"C:\Users\Leo\Desktop\YoutubeDownload\output", filename)
    print("Done.                 ")
    
elif option == "n":
    print("Aborted")
else:
    print("Invalid input")
