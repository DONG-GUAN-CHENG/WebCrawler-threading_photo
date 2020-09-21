## 先確定想要爬取的網站是否准許存取圖片
import requests
r=requests.get('https://zh.pngtree.com/so/狗/2')
if r.status_code==200: #200表示請求成功，404表示請求失敗，當請求失敗也可用reason查看原因
    print('准許存取',r.text) #用text屬性來取得網頁原始碼
else:
    print('不予存取',r.status_code,r.reason)# 用status.code來查看HTTP狀態碼，並用reason查看原因

## 爬蟲主程式
import web_crawler_photo_function as w
import os
import time
while True: #以while迴圈。可以在找不到圖片時，讓使用者重新輸入關鍵字，直到有搜尋結果為止
    photo_name= input("請輸入要下載的圖片名稱")
    download_num= int(input("請輸入要下載的數量:"))
    photo_list=w.get_photolist(photo_name,download_num) #以先前撰寫的函式取得圖片連結狗

    if photo_list == None:
        print("找不到圖片，請換關鍵字後再嘗試")
    else:
        if len(photo_list)<download_num:
            print("找到的相關圖片僅有",len(photo_list),"張")
        else:
            print("取得所有圖片連結")
        break

folder_name=w.creat_folder(photo_name)

#未開啟多執行緒執行圖片下載
start_time = time.time()
print("開始下載...")
for i in range(len(photo_list)):
    w.download_pic(photo_list[i], folder_name+os.sep+photo_name+os.sep+str(i+1)) #以撰寫的函式依序將所有圖片下載下來
#w.get_photobythread(folder_name,photo_name,photo_list)
end_time = time.time()
print("\n下載完畢",'\n未開啟多執行緒執行時間:',str(end_time - start_time), ' s')


#開啟多執行緒執行圖片下載
start_time = time.time()
print("\n開始下載...")
w.get_photobythread(folder_name,photo_name,photo_list)
end_time = time.time()
print("\n下載完畢",'\n開啟多執行緒執行時間:',str(end_time - start_time), ' s')
