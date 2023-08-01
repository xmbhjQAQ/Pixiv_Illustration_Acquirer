import requests
import json
import webbrowser
import sys, os
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

os.makedirs('./image/', exist_ok=True)
i = 0
j = 0

Mode = input('NSFW OR SFW? Please input 1 (nsfw) OR 0 (sfw):')
if (Mode != '1' and Mode != '0'):
    print("输入非法！")
    os.system("pause")
    sys.exit()

sum = int(input('How much you want:'))
if (sum > 10):
    print("Limited, try using a smaller number and then restart the program. PS: Range: [1,10]")
    os.system("pause")
    sys.exit()

downloaded_urls = []  # 所有urls保存与此

if (Mode == '0'):
    tag = input('Send your tag1 please:')
    payload = {'tag1': tag}
    url = 'https://pixiv-ab.tk/api/pixiv/daily/tag/'
    url2 = url + tag
    while i < sum:
        t = time.time()  # 时间戳
        t = str(int(t))
        url3 = url2 + '?t=' + t
        url4 = requests.get(url3)
        print(url4)
        if (url4.status_code == 404):  # 判断是否存在
            print('没这个tag，再输一个试试吧')
            os.system("pause")
            sys.exit()
        text = url4.text
        data = json.loads(text)
        urls = data['url']
        split_link = urls.split("/", 3)
        final_url = "https://pix.nagisa.icu/" + split_link[3]
        print(final_url)

        # 检测图片是否之前下载过
        if final_url in downloaded_urls:
            print('啊哦，api返回了个已下载的图片捏，重来！')
            j=j+1
            if(j==5):
                print('啊哦，看来这个tag只有这些图片了，只能停下了呢....')
                os.system("pause")
                sys.exit()
            continue

        downloaded_urls.append(final_url)  # 将api返回的urls保存到downloaded_urls

        timeout_seconds = 10
        print('正在下载第', str(i + 1), '张图片，共计', str(sum), '张图片')
        r = requests.get(final_url, headers=headers, timeout=timeout_seconds)
        if (r.status_code == 404):
            print('我超！假图！再来一张！')  # 判断是否有图片因为API更新延迟造成的404
            i = i - 1
            continue
        webbrowser.open(final_url)

        path = './image/img' + str(i + 1) + '.png'
        with open(path, 'wb') as f:
            f.write(r.content)
        print('图片', str(i + 1), '已保存至程序所在目录的img文件夹内')
        i = i + 1

elif (Mode == '1'):
    tag = input('Send your tag1 please:')
    payload = {'tag1': tag}
    url = 'https://pixiv-ab.tk/api/pixiv/r18/tag/'
    url2 = url + tag
    while i < sum:
        t = time.time()  # 时间戳
        t = str(int(t))
        url3 = url2 + '?t=' + t
        url4 = requests.get(url3)
        print(url4)
        if (url4.status_code == 404):  # 判断是否存在
            print('没这个tag，再输一个试试吧')
            os.system("pause")
            sys.exit()
        text = url4.text
        data = json.loads(text)
        urls = data['url']
        split_link = urls.split("/", 3)
        final_url = "https://pix.nagisa.icu/" + split_link[3]
        print(final_url)

        # 检测图片是否之前下载过
        if final_url in downloaded_urls:
            print('啊哦，api返回了个已下载的图片捏，重来！')
            j=j+1
            if(j==5):
                print('啊哦，看来这个tag只有这些图片了，只能停下了呢....')
                os.system("pause")
                sys.exit()
            continue

        downloaded_urls.append(final_url)  # 将api返回的urls保存到downloaded_urls

        timeout_seconds = 20
        r = requests.get(final_url, headers=headers, timeout=timeout_seconds)
        if (r.status_code == 404):
            print('我超！假图！再来一张！')  # 判断是否有图片因为API更新延迟造成的404
            i = i - 1
            continue
        webbrowser.open(final_url)

        path = './image/img' + str(i + 1) + '.png'
        with open(path, 'wb') as f:
            f.write(r.content)
        print('正在下载第', str(i + 1), '张图片，共计', str(sum), '张图片')
        print('图片', str(i + 1), '已保存至程序所在目录的img文件夹内')        
        i = i + 1
print('所有图片下载完成了捏')
os.system("pause") 
sys.exit()
