## 用requests下載網路圖片
import requests
def download_pic(url, path):
    pic=requests.get(url)
    path+=url[url.rfind('.'):]
    f=open(path,'wb')
    f.write(pic.content)
    f.close()

#url='https://png.pngtree.com/png-clipart/20190411/ourmid/pngtree-hand-painted-elements-of-sleeping-plush-dog-png-image_926553.jpg'
#pic_path="downd"
#download_pic(url,pic_path)

##--------下載指定數量的圖片---------
import requests
from bs4 import BeautifulSoup

def get_photolist(photo_name, download_num):
    page=1 #網頁初始頁數
    photo_list=[] #建立圖片空陣列

    while True:
        url = 'https://zh.pngtree.com/so/' + photo_name+'/'+str(page)
        # 設定連結
        html = requests.get(url)
        html.encoding = 'utf-8'
        bs = BeautifulSoup(html.text, 'lxml')  # 解析網頁
        photo_item = bs.find_all('div', {'class': "mb-picbox"})

        if len(photo_item)==0:
            return None
        for i in range(len(photo_item)):
            photo=photo_item[i].find('img')['data-original'] #尋找標籤img並取出'src'之中的內容
            if photo in photo_list:
                return photo_list
            if photo == '/static/img/blank.gif':
                photo=photo_item[1].find('img')['data-lazy']
            photo_list.append(photo)
            if len(photo_list)>=download_num:
                return photo_list
        page+=1

## 分門別類的儲存圖片
import os
def creat_folder(photo_name):
    folder_name=input('請輸入要儲存的資料夾:')
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("資料夾不存在，建立資料夾:"+folder_name)
    else:
        print("找到資料夾:"+folder_name)

    if not os.path.exists(folder_name+os.sep+photo_name):
        os.mkdir(folder_name+os.sep+photo_name)
        print('建立資料夾:'+photo_name)
    else:
        print(photo_name+"資料夾已存在")
    return folder_name
## 建立多執行緒的函式_城市一次最多只能開啟100個執行緒
import threading
def get_photobythread(folder_name,photo_name, photo_list):
    download_num=len(photo_list)
    q=int(download_num/100) #取商數
    r=download_num % 100 #取餘數

    for i in range(q): #用商數當作迴圈的重複次數，一次開啟100個執行緒，同一時間下載100張圖片
         threads=[]
         for j in range(100):
             threads.append(threading.Thread(target=download_pic,args=(photo_list[i*100+j],folder_name+os.sep+photo_name+os.sep+str(i*100+j+1))))
             threads[j].start()
         for j in threads:
             j.join()
         #print(int((i+1)*100/download_num*100),'%') # 顯示當前進度


    threads=[]
    for i in range(r):
        threads.append(threading.Thread(target=download_pic,args=(photo_list[q*100+i],folder_name+os.sep+photo_name+os.sep+str(q*100+i+1))))
        threads[i].start()
    for i in threads:
        i.join()
        print("100%")












