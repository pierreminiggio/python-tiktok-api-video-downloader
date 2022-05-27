import sys
from TikTokApi import TikTokApi

args = sys.argv
argsLength = len(args)

defaultVideoNumber = 20

if argsLength != 2:
    print('use like this : python main.py [video_url]')
    sys.exit()

video_url = args[1]

with TikTokApi() as api:
    data = api.video(id=video_url.split('/')[-1]).bytes()
    with open('video.mp4', 'wb') as output:
        output.write(data)
