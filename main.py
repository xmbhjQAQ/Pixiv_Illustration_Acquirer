import requests
import json
import webbrowser
import sys,os
import time
import urllib
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
os.makedirs('./image/', exist_ok=True)
cache=['0']*10
Mode=input('NSFW OR SFW?PLZ input 1(nsfw) OR 0(sfw):')
if(Mode!='1' and Mode!='0'):
  print("输入非法！")
  os.system("pause")
  sys.exit()
sum=int(input('How much you want:'))
if(sum>=10):
 print("limited,try using smaller number then try to restart it. ps:range:[1,10)")
 os.system("pause")
 sys.exit()
if(Mode=='0'): 
  tag=input('send your tag1 plz:')
  payload={'tag1':tag}
  url='https://pixiv-ab.tk/api/pixiv/daily/tag/'
  url2=url + tag
  for i in range(sum): 
   t = time.time()            #时间戳
   t = str(int(t))
   url3= url2 + '?t=' + t
   url4=requests.get(url3)
   print(url4)
   if(url4.status_code==404):             #判断是否存在
     print('没这tag，再输一个试试吧')
     os.system("pause")
     sys.exit()
   text=url4.text
   data=json.loads(text)
   urls = data['url']
   split_link = urls.split("/", 3)
   final_url= "https://pix.xmbhjqaq.icu/" + split_link[3]
   print(final_url)
   webbrowser.open(final_url)
   timeout_seconds = 5
   r = requests.get(final_url, headers=headers,timeout=timeout_seconds)
   path = './image/img'+str(i+1)+'.png'
   with open(path, 'wb') as f:
        f.write(r.content)
   print('图片已保存至程序所在目录的img文件夹内，共计',str(i+1),'张图片')     
if(Mode=='1'):
  tag=input('send your tag1 plz:')
  payload={'tag1':tag}
  url='https://pixiv-ab.tk/api/pixiv/r18/tag/'
  url2=url + tag
  for i in range(sum): 
   t = time.time()            #时间戳
   t = str(int(t))
   url3= url2 + '?t=' + t
   url4=requests.get(url3)
   print(url4)
   if(url4.status_code==404):             #判断是否存在
     print('没这tag，再输一个试试吧')
     os.system("pause")
     sys.exit()
   text=url4.text
   data=json.loads(text)
   urls = data['url']
   split_link = urls.split("/", 3)
   final_url= "https://pix.xmbhjqaq.icu/" + split_link[3]
   print(final_url)
   webbrowser.open(final_url)
   timeout_seconds = 5
   r = requests.get(final_url, headers=headers,timeout=timeout_seconds)
   path = './image/img'+str(i+1)+'.png'
   with open(path, 'wb') as f:
        f.write(r.content)
   print('图片已保存至程序所在目录的img文件夹内，共计',str(i+1),'张图片')
