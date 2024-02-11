from pytube import YouTube
import ffmpeg
import os
import threading
from pytube import Playlist


def WoawTube():
    '''PROGRESS BAR'''
    # Function to be called while the download is in progress

    # Function to be called when download is complete

    '''DOWNLOAD FUNCTIONS'''
    # Download Adaptive 1080 + Audio and Merge
    def download_1080():
        print(f"\nDownloading {yt.title}...\n\n")
        try:
            stream = yt.streams.get_by_itag(137)# get video 1080
            
            stream.download()
            print("Processing... \n")

            # if there are symbols in the title we should remove them as pytube removes them at the end of the title
            
            title = yt.title # get the video title

            print("Downloading Audio File... \n")
            audio = yt.streams.get_by_itag(140).download()  # download audio
            print("Merging Files... \n")
            
            # Convert to ffmpeg object and merge audio and video
            video_stream = ffmpeg.input("video.mp4") # convert video to ffmpeg object
            audio_stream = ffmpeg.input(f"{title}.mp4") # convert audio to ffmpeg object
            ffmpeg.output(audio_stream, video_stream, f"{yt.title}.mp4").run() # merge with title of yt vid
            print("Finalising...\n\n")
            # Remove the audio and video file once merged
            os.remove(audio)
            os.remove("video.mp4")

            print("Download Complete\n\n")
            WoawTube()
        except AttributeError:
            download_720()

    # Download progressive 720
    def download_720():
        print(f"\nDownloading {yt.title}\n\n")
        try:
            stream = yt.streams.get_by_itag(22)
            stream.download()
            print("Download Complete\n\n")
            WoawTube()
        except AttributeError:
            download_360()

    # Download progressive 360
    def download_360():
        print(f"\nDownloading {yt.title}\n\n")
        try:
            stream = yt.streams.get_by_itag(18)
            stream.download()
            print("Download Complete\n\n")
            WoawTube()
        except AttributeError:
            print("Can not find this video, is that the correct link?\n\n")
            WoawTube()

    # Get highest quality audio
    def download_audio():
        # Start thread to prevent UI Hang
        threading.Thread().start()
        print(f"\nDownloading {yt.title}...")    
        # filter stream for audio only
        yt.streams.filter(only_audio=True)
        # try and get stream by itag 140 -mp4- and commence download
        try:
            yt.streams.get_by_itag(140).download() 
            print("Download Complete!\n\n")
            WoawTube()
        except AttributeError:
            print("Can not find this video, is that the correct link?\n\n")
            WoawTube()
   
    # Download highest available quality 
    def download_highest_quality_available():
        # try to find and download videos starting from 720 -> 420p -> 360p
        try:
            download_1080() # try to donwload 1080
            print("\n\ndownloading 1080\n")
        except AttributeError:
            print("1080 not found\n")
            download_720() # try to download 720 if 1080 fails
        except AttributeError:
            print("720 not found\n")
            download_360() # try to download 360 if 720 fails
        except AttributeError:
            print("Can not find this video, is that the correct link?\n\n") # if none are available (shouldn't happen) print failed

    '''DOWNLOAD FUNCTIONS END'''

    '''STARTUP LOGIC'''
      
    # Playlist or individual video?
    video_or_playlist = input("Would you like to download a:\n1.Single video\n2.Playlist?\n(select a number 1-2)\n\n")
    url = input("Paste the link here and then hit enter!\n\n")
    quality = input("\nSelect one of the options below (1-5):\n1.Highest available quality\n2.1080p\n3.720p\n4.360p\n5.Audio\n\n")

    # Check if playlist or single and quality
    if video_or_playlist == "1" and quality == "1":
        # Create Youtube object and add functions for tracking progress and compeletion
        yt = YouTube(
        url,
        use_oauth=False,
        allow_oauth_cache=True,
        #on_progress_callback=progress_func,
        #on_complete_callback=complete_func,
        )
        download_highest_quality_available()
    elif video_or_playlist == "1" and quality == "2":
        # Create Youtube object and add functions for tracking progress and compeletion
        yt = YouTube(
        url,
        use_oauth=False,
        allow_oauth_cache=True,
        #on_progress_callback=progress_func,
        #on_complete_callback=complete_func,
        )
        download_1080()
    elif video_or_playlist == "1" and quality == "3":
        # Create Youtube object and add functions for tracking progress and compeletion
        yt = YouTube(
        url,
        use_oauth=False,
        allow_oauth_cache=True,
        #on_progress_callback=progress_func,
        #on_complete_callback=complete_func,
        )
        download_720()
    elif video_or_playlist == "1" and quality == "4":
        # Create Youtube object and add functions for tracking progress and compeletion
        yt = YouTube(
        url,
        use_oauth=False,
        allow_oauth_cache=True,
        #on_progress_callback=progress_func,
        #on_complete_callback=complete_func,
        )
        download_360()
    elif video_or_playlist == "1" and quality == "5":
        # Create Youtube object and add functions for tracking progress and compeletion
        yt = YouTube(
        url,
        use_oauth=False,
        allow_oauth_cache=True,
        #on_progress_callback=progress_func,
        #on_complete_callback=complete_func,
        )
        download_audio()
    
    
    elif video_or_playlist == "2" and quality == "1":
        playlist = Playlist(url)
        for video in playlist.videos:
            print(f"Downloading {video.title}...\n")
            try:
                stream = yt.streams.get_by_itag(137)# get video 1080
                
                stream.download(filename = "video")
                print("Processing... \n")

                print("Downloading Audio File... \n")
                audio = yt.streams.get_by_itag(140).download()  # download audio
                print("Merging Files... \n")
                
                # Convert to ffmpeg object and merge audio and video
                video_stream = ffmpeg.input("video.mp4") # convert video to ffmpeg object
                audio_stream = ffmpeg.input(f"{title}.mp4") # convert audio to ffmpeg object
                ffmpeg.output(audio_stream, video_stream, f"{yt.title}.mp4").run() # merge with title of yt vid
                print("Finalising...\n\n")
                # Remove the audio and video file once merged
                os.remove(audio)
                os.remove("video.mp4")

                print("Download Complete\n\n")
                WoawTube()
            except AttributeError:
                video.streams.get_by_itag(22).download()
            except AttributeError:
                video.streams.get_by_itag(18).download()
            except AttributeError:
                print("Oh no, it seems something went wrong, please report it to Rayhaan :)")

    elif video_or_playlist == "2" and quality == "2":
        playlist = Playlist(url)
        for video in playlist.videos:
            print(f"Downloading {video.title}...\n")
            try:
                stream = yt.streams.get_by_itag(137)# get video 1080
                
                stream.download()
                print("Processing... \n")

                # if there are symbols in the title we should remove them as pytube removes them at the end of the title
            
                title = yt.title # get the video title

                print("Downloading Audio File... \n")
                audio = yt.streams.get_by_itag(140).download(filename = "video")  # download audio
                print("Merging Files... \n")
                
                # Convert to ffmpeg object and merge audio and video
                video_stream = ffmpeg.input("video.mp4") # convert video to ffmpeg object
                audio_stream = ffmpeg.input(f"{title}.mp4") # convert audio to ffmpeg object
                ffmpeg.output(audio_stream, video_stream, f"{yt.title}.mp4").run() # merge with title of yt vid
                print("Finalising...\n\n")
                # Remove the audio and video file once merged
                os.remove(audio)
                os.remove("video.mp4")

                print("Download Complete\n\n")
                WoawTube()
            except AttributeError:
                video.streams.get_by_itag(22).download()
            except AttributeError:
                video.streams.get_by_itag(18).download()
            except AttributeError:
                print("Oh no, it seems something went wrong, please report it to Rayhaan :)")

    elif video_or_playlist == "2" and quality == "3":
        playlist = Playlist(url)
        for video in playlist.video_urls:
            print(f"Downloading {video.title}\n")
            try:
                video.streams.get_by_itag(22).download()
            except AttributeError:
                video.streams.get_by_itag(18).download()
            except AttributeError:
                print("Oh no, it seems something went wrong, please report it to Rayhaan :)")

    elif video_or_playlist == "2" and quality == "4":
        playlist = Playlist(url)
        for video in playlist.videos:
            print(f"Downloading {video.title}\n")
            try:
                video.streams.get_by_itag(18).download()
            except AttributeError:
                print("Oh no, it seems something went wrong, please report it to Rayhaan :)")
            
    elif video_or_playlist == "2" and quality == "5":
        playlist = Playlist(url)
        for video in playlist.videos:
            # Create Youtube object and add functions for tracking progress and compeletion
            yt = YouTube(
            video,
            #on_progress_callback=progress_func,
            #on_complete_callback=complete_func,
            )
            print(f"Downloading {video.title}\n")
            video.streams.get_by_itag(140).download()

    else:
        print("Invalid Selection!\n\n")
        WoawTube()

WoawTube()

#yt.download(filename="filename",'/path/to/download/directory')
#pip install pytubefix==1.10.0