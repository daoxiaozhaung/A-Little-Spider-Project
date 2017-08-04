import requests
import time
from bs4 import BeautifulSoup

url = 'http://www.landchina.com/default.aspx?tabid=263&ComName=default'

RA = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':"zh-CN,zh;q=0.8",
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'ASP.NET_SessionId=lceshm2jex0nemkx3hkfjgig; Hm_lvt_83853859c7247c5b03b527894622d3fa=1501552573,1501593246; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1501601850',
    'Host':'www.landchina.com',
    'HTTPS':'1',
    'Referer':'http://www.landchina.com/default.aspx?tabid=263&ComName=default',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36 QQBrowser/9.1.3471.400'

}

base = open('E:/pytest/urls/urls2.txt','a')
for num in range(165,201):
    data = {
        'TAB_QuerySubmitPagerData':'%s' %(num)
    }
    #print(data)
    a1 = requests.get(url,headers = RA,data = data)
    b1 = BeautifulSoup(a1.text,'lxml')
    href = b1.select('a')
    for i in href:
        a = i.get('href')
        if 'guid' in str(a):
            base.write('http://www.landchina.com/'+ a +'\n')
    print(data)
    time.sleep(1)
base.close()
#\35 54393E66F17105AE055000000000001 > td:nth-child(3) > a
#\35 47EF19428B424C5E055000000000001 > td:nth-child(3) > a
'''
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=554393E66F17105AE055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=547EF19428B424C5E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=547E2DFF6BEA2208E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=547E15C74C7021FEE055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=554452BDA12312FDE055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=54292403F7461E77E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=54292403F7541E77E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=701792e3-5953-4872-8702-dc0fc369d98e
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=7a947837-0e11-4927-b0aa-7e997aa6eef4
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=ef0114a6-49cc-48ab-b462-5abd6b92bbec
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=b7db515e-2479-49f6-a678-b0708ba61443
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=0774e729-3419-466c-9c09-301691fb1bb1
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=555C4CFC68FF5D27E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=555C7B5A8D495E0CE055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=555C8235B28D5DBCE055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=555C829591625E40E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=f92f80af-edd3-4c0d-89da-69049d203f73
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=c8a14b0f-1595-428f-a9b8-700c01976e5e
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=8567cb68-6d30-4a97-935c-5f101377588e
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=a3b2dfec-dbbd-4c31-acde-57c7aa0af4c7
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=f2327960-a054-41fe-a007-98828ac91d88
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=551ABAB96F3E1079E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=eaa39ca7-fc67-4f61-a04a-4ec992f45d7a
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=a762c209-210f-4c96-84d5-3586017bed2c
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=555930E0CDD553A1E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=552FFFBCAA225290E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=551CC9FE7D261723E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=552157D7FB0525A7E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=aa9226f8-bf44-498c-8e29-00d6b9b4c4d3
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=5f5289fe-c995-4b9a-aa82-b42b89e0231c
'''
'''
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=aa9226f8-bf44-498c-8e29-00d6b9b4c4d3
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=efe2ec57-d1ea-480e-943c-5f8efdd3d496
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=552FFFBCAA225290E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=212a18bb-ff30-4db7-a789-af9f60ec8ddf
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=3ffb52d1-f959-4a36-8c13-73fdaba35ceb
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=a0b7a6a0-6a04-448d-8e3c-e53b194f9408
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=ee91e0d2-921b-46ff-bbe4-df48f891d627
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=69da5a88-6b1d-4d15-8eb3-767b5a82bfd5
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=551CC9FE7D261723E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=552157D7FB0525A7E055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=5f5289fe-c995-4b9a-aa82-b42b89e0231c
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=0421d635-5f14-4e3a-af3f-ad24062a7bdc
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=3f0f5346-86d9-4aa9-9a69-14490445f085
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=5598CDD76D22180AE055000000000001
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=8e2d814b-0d27-47e6-90da-2c9d54359a91
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=e126aa58-3de4-4fd1-a6c6-7562f65c7997
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=6903dbbb-5308-4cf0-9a00-222d7c6a6851
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=389c95d7-f90c-4daf-be8e-6688533cd2f2
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=5925b397-714a-40b9-96b8-162aab8c0b1b
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=385ad0c4-45ee-4736-a335-9e9603f93113
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=60beada8-49c0-47d0-a541-390da32c9ab0
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=5831737c-ef25-485e-adbb-9a80bd49f3bb
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=e01c9f6c-d0d0-41b2-9c0e-cf9fdf9b1398
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=34941981-0cff-4d75-a0d0-538bc22187bd
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=b4d366cd-296c-45dc-aaa4-5b6b6dc5de64
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=05ae55a6-1670-410d-bcae-7ebb24e843b1
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=7af77540-5579-4944-ba01-18043a056ea8
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=2b55881e-fb50-4869-9858-e096fad8c140
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=65080881-5f1f-41f4-b63e-6de506c24fcf
default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=a50aa973-8e1f-4679-b728-3b2acdcebd69
'''