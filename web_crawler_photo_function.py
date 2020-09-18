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
        url = 'https://zh.pngtree.com/so/' + photo_name
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




