from TikTokApi import TikTokApi

args = sys.argv
argsLength = len(args)

defaultVideoNumber = 20

if argsLength != 2:
    print('use like this : python main.py [video_url]')
    sys.exit()

video_url = args[1]

with TikTokApi() as api:
    data = api.get_video_no_watermark(video_url, return_bytes=1, language='en', proxy=None, custom_verifyFp='')
    with open('videos.mp4', 'wb') as output:
        output.write(data)
