import requests
import csv
import time
import pandas as pd
from bs4 import BeautifulSoup

RA = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':"zh-CN,zh;q=0.8",
#    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'ASP.NET_SessionId=zxgbp1mi3oqsuufaxghiw5qw; Hm_lvt_83853859c7247c5b03b527894622d3fa=1501552573,1501593246,1501644940; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1501668192',
    'Host':'www.landchina.com',
    'HTTPS':'1',
    'Referer':'http://www.landchina.com/default.aspx?tabid=263&ComName=default',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36 QQBrowser/9.1.3471.400'

}
def test():
    url = 'http://www.landchina.com/default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=f2327960-a054-41fe-a007-98828ac91d88'
    t1 = requests.get(url,headers = RA)
    t2 = BeautifulSoup(t1.text,'lxml')

    print(t2.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c4_ctrl'))
    print(t2.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c2_ctrl'))
    # if '行政区' in str(t2.get_text()):
    #     print('successful!')
    # else:
    #     print('failed!')
#test()

file = open('E:/pytest/urls/urls3.txt','r')
csvFile = open('E:/pytest/urls/data1.csv','a',newline='')
filenames = ['行政区','电子监管号','项目名称','项目位置','面积(公顷)','土地用途','供地方式','土地使用年限','行业分类','土地级别','成交价格(万元)','支付期号','约定支付日期','约定支付金额(万元)','土地使用权人','下限','上限','约定交地时间','约定开工时间','约定竣工时间','实际开工时间','实际竣工时间','批准单位','合同签订日期']
writer = csv.DictWriter(csvFile,fieldnames=filenames)
#writer.writeheader()
dict1 = {
    '行政区':'成都',
    '电子监管号':'0123456',
    '项目位置':'天府广场',
    '项目名称':'name'
}
#writer.writerow(dict1)
num = 0

for urls in file.readlines():
    num += 1
    url1 = urls.strip('\n')
    #print(url1)
    a1 = requests.get(url1,headers = RA)
    b1 = BeautifulSoup(a1.text,'lxml')
    if '行政区' in str(b1.get_text()):
        try:
            xzq = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c2_ctrl')
            dzjgh = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c4_ctrl')
            xmmc = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r17_c2_ctrl')
            xmwz = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r16_c2_ctrl')
            mj = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c2_ctrl')
            #tdly = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c4_ctrl')
            tdyt = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c2_ctrl')
            gdfs = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c4_ctrl')
            tdsynx = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c2_ctrl')
            hyfl = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c4_ctrl')
            tdjb = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c2_ctrl')
            cjjg = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c4_ctrl')
            zfqh = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c1_0_ctrl')
            ydzfrq = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c2_0_ctrl')
            ydzfje = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c3_0_ctrl')
            tdsyqr = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r9_c2_ctrl')
            ydrjlxx = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c2')
            ydrjlsx = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c4')
            ydjdsj = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r21_c4_ctrl')
            ydkgsj = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c2_ctrl')
            ydjgsj = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c4_ctrl')
            sjkgsj = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r10_c2')
            sjjgsj = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r10_c4')
            pzdw = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c2_ctrl')
            htqdrq = b1.select('#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c4_ctrl')

            data = {
                '行政区':xzq[0].get_text(),
                '电子监管号':dzjgh[0].get_text(),
                '项目名称':xmmc[0].get_text(),
                '项目位置':xmwz[0].get_text(),
                '面积(公顷)':mj[0].get_text(),
                #'土地来源':tdly[0].get_text(),
                '土地用途':tdyt[0].get_text(),
                '供地方式':gdfs[0].get_text(),
                '土地使用年限':tdsynx[0].get_text(),
                '行业分类':hyfl[0].get_text(),
                '土地级别':tdjb[0].get_text(),
                '成交价格(万元)':cjjg[0].get_text(),
                '支付期号':zfqh[0].get_text(),
                '约定支付日期':ydzfrq[0].get_text(),
                '约定支付金额(万元)':ydzfje[0].get_text(),
                '土地使用权人':tdsyqr[0].get_text(),
                '下限':ydrjlxx[0].get_text(),
                '上限':ydrjlsx[0].get_text(),
                '约定交地时间':ydjdsj[0].get_text(),
                '约定开工时间':ydkgsj[0].get_text(),
                '约定竣工时间':ydjgsj[0].get_text(),
                '实际开工时间':sjkgsj[0].get_text(),
                '实际竣工时间':'' if sjjgsj[0].get_text() == '\xa0' else sjjgsj[0].get_text(),
                '批准单位':pzdw[0].get_text(),
                '合同签订日期':htqdrq[0].get_text(),
            }
            # dataframe = pd.DataFrame(data)
            # dataframe.to_csv('E:/pytest/urls/data1.csv',index=True,sep='')
            print(data)
            writer.writerow(data)
            print('put %s in data successfully' %(num))
        except IndexError:
            print('%s page is not exist' % (num))
            continue
        except UnicodeEncodeError:
            print('%s page is not exist' % (num))
            continue
    else:
        print('%s page is not exist' %(num))
        break
    time.sleep(1)
csvFile.close()
file.close()

