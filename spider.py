from bs4 import BeautifulSoup
import os
import requests
import urllib.request#下载文件用
import time#加上时间戳，防止重复

if 'images' not in os.listdir():
	os.makedirs("images")
headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
def time_num():
	time_num=str(time.time())
	time_num_new=time_num.split('.')
	return time_num_new[1]

for cnt in range(0,91,30):
	url='https://movie.douban.com/celebrity/1016930/photos/?type=C&start=%s&sortby=like&size=a&subtype=a'%cnt
	req=requests.get(url=url)
	req.encoding='utf-8'
	html=req.text#获得源代码
	bf=BeautifulSoup(html,'html.parser')
	element=bf.find('ul',class_='poster-col3 clearfix').find_all('li')
	#极为牛B的办法↓
	for e in element:
		imgurl_origin=e.find('img').get('src')#找到原图片地址
		imgurl_list=list(imgurl_origin)#将字符串变成列表
		imgurl_list[37]='l'#替换字符
		imgurl_target=''.join(imgurl_list)#变回字符串

		fileName=e.find('div',class_='prop').text.strip()


		urllib.request.urlretrieve(url=imgurl_target,filename="images/"+fileName+"_"+time_num()+".jpg")
		print("Download Completed! %s"%(fileName))

