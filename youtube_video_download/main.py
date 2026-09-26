import yt_dlp as yt
import os


def MakeDownloadFolder():

    target_path = os.path.join(os.getcwd(), "downloads")

    os.makedirs(target_path, exist_ok=True)

    print('Downloads folder created successfully')

    return target_path


def Settings_format():
    target_path = MakeDownloadFolder()

    ydl_opts = {
        "format" : "bestvideo",
        "outtmpl" : os.path.join(target_path, "%(title)s.%(ext)s")
    }

    return ydl_opts

def DownloadVideo(url):
    ydl_opts = Settings_format()
    
    try:
        with yt.YoutubeDL(ydl_opts) as yd:
            yd.download([url])
    except Exception as e:
        print(f'Error {e} as raised')
    else:
        print('Your youtube video downloaded successfully')


if __name__ == '__main__':
    URL = input("Enter a Youtube video to download: ")
    if URL:
        DownloadVideo(URL)
    else:
        print("Kindly enter the valid youtube video url")
