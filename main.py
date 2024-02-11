from pytube import YouTube

# https://www.youtube.com/watch?v=mChh2WwT4Tk, https://www.youtube.com/watch?v=N9uFOFyuT1M&list=PLzn0qdi6JpdsRbtwRp1-vPqciiAhKJndg, https://www.youtube.com/watch?v=HDamg-oZ__4

def youtube_downloader():
    
    def bulk_download():
        videos = list(input("Paste videos links seperated by ','\n\n").split(","))
        print(videos)
         # Ask user which video 
        selected_video = input(f"Below are the available options:\nLow Quality: 360p\nMedium Quality: 720p\nAudio: audio only\n\nSelect your prefered option:\nL = Low\nM = Medium\nA = Audio\n")
        print("\nProcessing, please wait...")

        for video in videos:
            video = YouTube(video)
            # 360p
            low_quality = video.streams.get_by_itag('18')

            # 720p
            medium_quality = video.streams.get_by_itag('22')

            # 1080p -> need to figure out ffmpeg for adaptive streams
            #high_quality = video.streams.get_by_itag('137')

            # get highest quality audio file
            audio = video.streams.get_audio_only()
                       
            # Download low quality
            if selected_video == "l" or selected_video == "L":
                if low_quality == "None":
                    print("Not Available")
                    pass
                else:
                    print(f"Downloading {video.title}")
                    low_quality.download("./")
                    print("done")
                    

            # Download medium quality
            if selected_video == "m" or selected_video == "M":
                if medium_quality == "None":
                    print("Not Available")
                    pass
                else:
                    print(f"Downloading {video.title}")
                    medium_quality.download("./")
                    print("done")
                    

            # Download audio only
            if selected_video == "a" or selected_video == "A":
                if audio == "None":
                    print("Not Available")        
                    pass
                else:
                    print(f"Downloading {video.title}")
                    audio.download("./")
                    print("done")
        youtube_downloader()            

    # funtion to ask user if they want to download another video
    def another_video():
        answer = input("Would you like to download another video?\n\nY = Yes\nN = No")
        if answer == "Y" or answer == "y":
            youtube_downloader()

        elif answer == "N" or answer == "n":
            pass
        else:
            another_video()

    # Download bulk or single
    bulk_single = input("Bulk or signle?\n\nB = Bulk\nS = Single\n\n")
    if bulk_single == "B" or bulk_single == "b":
        bulk_download()
    elif bulk_single == "s" or bulk_single == "S":
        pass
    else:
        youtube_downloader()

    # Get link from user
    link = input("Insert Video Url: ")
    print("\nRetrieving meta data, please wait...")
    
    # Create video object
    video = YouTube(link)
    
    # 360p
    low_quality = video.streams.get_by_itag('18')

    # 720p
    medium_quality = video.streams.get_by_itag('22')

    # 1080p -> need to figure out ffmpeg for adaptive streams
    #high_quality = video.streams.get_by_itag('137')

    # get highest quality audio file
    audio = video.streams.get_audio_only()
    
    # see which streams are available
    if low_quality == "None":
        low_quality_option = "Unavailabe"
    else:
        low_quality_option = "360p"

    if medium_quality == "None":
        medium_quality_option = "Unavailabe"
    else: 
        medium_quality_option = "720p"

    if audio == "None":
        audio = "Unavailabe"
    else:
        audio_option = "mp4"


    # Ask user which video 
    selected_video = input(f"Below are the available options:\nLow Quality: {low_quality_option}\nMedium Quality: {medium_quality_option}\nAudio: {audio_option}\n\nSelect your prefered option:\nL = Low\nM = Medium\nA = Audio\n")

    # Download low quality
    if selected_video == "l" or selected_video == "L":
        if low_quality == "None":
            print("Not Available")
            youtube_downloader()
        else:
            print("Downloading, please wait...")
            low_quality.download("./")
            print("done")
            youtube_downloader()

    # Download medium quality
    if selected_video == "m" or selected_video == "M":
        if medium_quality == "None":
            print("Not Available")
            youtube_downloader()
        else:
            print("Downloading, please wait...")
            medium_quality.download("./")
            print("done")
            youtube_downloader()

    # Download audio only
    if selected_video == "a" or selected_video == "A":
        if audio == "None":
            print("Not Available")        
            youtube_downloader()
        else:
            print("Downloading, please wait...")
            audio.download("./")
            print("done")
            youtube_downloader()

    
youtube_downloader()
