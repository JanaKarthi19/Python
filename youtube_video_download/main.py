import yt_dlp as yt
import os


def MakeDownloadFolder() -> str:

    target_path = os.path.join(os.getcwd(), "downloads")

    os.makedirs(target_path, exist_ok=True)

    print('Downloads folder created successfully')

    return target_path


def Settings_format() -> str:
    target_path = MakeDownloadFolder()

    print('''
            In which your want to download your video: 
                    Option 1: Only Audio
                    Option 2: Audio + video + Subtitles
                    Option 3: Audio + Video without Subtitles
    ''')

    option = int(input("Enter a your option in number: "))

    
    ydl_opts = {
        "retries" : 10,
        "fragment_retries": 10,
        "ffmpeg_location" : r"C:\ffmpeg\bin",
        "outtmpl" : os.path.join(target_path, "%(title)s.%(ext)s"),
    }
    
    if option == 1:
        ydl_opts["format"] = "bestaudio/best"
        ydl_opts["postprocessors"] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',   # or 'm4a', 'wav'
                'preferredquality': '192',
            }]

    elif option == 2:
        ydl_opts["format"] = "bestvideo+bestaudio/best"
        ydl_opts["merge_output_format"] = "mkv"
        ydl_opts["subtitleslangs"] = ["en"]
        ydl_opts["writesubtitles"] = True

    elif option == 3:
        ydl_opts["format"] = "bestvideo+bestaudio/best"
        ydl_opts["merge_output_format"] = "mkv"

    else:
        print("⚠️Enter the valid Option")
        

    return ydl_opts

def DownloadVideo(url: str):
    ydl_opts = Settings_format()
    
    try:
        with yt.YoutubeDL(ydl_opts) as yd:
            yd.download([url])

    except Exception as e:
        print(f'🌋Error {e} as raised')
    else:
        print('Your video 📼 downloaded successfully✔️✔️')

def main():
    print('''
            \t\tYou can download videos form:

            \tVideo paltforms: YouTube, Vimeo, Dailymotion, 9GAG, 56.com, 7plus, 20min

            \tSocial Media: Facebook, Instagram, Twitter/X, TikTok, Reddit, VK

            \tMusic/Audio: SoundCloud, Bandcamp, Audius, Mixcloud, Apple Podcasts

            \tEducation/Courses: AcademicEarth, Coursera (limited), Khan Academy
        
            \tAdult Content: Pornhub, XVideos, 4tube, Beeg, BongaCams (many supported)
    ''')
    URL = input("Enter a video to download: ")
    if URL:
        DownloadVideo(URL)
    else:
        print("Kindly enter the valid youtube video url")

if __name__ == '__main__':
    main()
