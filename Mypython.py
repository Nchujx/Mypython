python 爬虫

一般读取网页
"""
from urllib import request
resp = request.urlopen(http://www.baidu.com)
print(resp.read())
#下载 urlretrieve
request.urlretrieve("http://www.baidu.com","1.html") 

"""

添加请求头
"""
from urllib import request
url = ""
header = {
    
}
"""

使用代理爬虫
"""
快代理 https://www.kuaidaili.com/free/
代理云 http://www.dailiyun.com
from urllib import request
url = "http://httpbinm.org/ip"
#1.使用 ProxyHandler 传入代理构建 handler
handler = request.ProxyHandler({'http':'223.241.78.43:8010'})
#2.使用 handler 构建 opener
opener = request.build_opener(handler)
#3.使用 opener 发送请求
resp = opener.open(url)
print(resp.read())
"""

未使用cookie访问
"""
from urllib import request
url = "https://www.52pojie.cn/home.php?mod=space&uid=1277341&do=profile&from=space"
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4050.0 Safari/537.36 Edg/82.0.423.0",
    "Cookie"

}
req = request.Request(url=url,headers=header)
resp = request.urlopen(req)
#print(resp.read().decode('gbk'))
with open('52.html','w') as fp:
    fp.write(resp.read().decode('gbk'))
"""


使用cookie访问
"""
from urllib import request
url = "https://www.52pojie.cn/forum.php?mod=guide&view=newthread"
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4050.0 Safari/537.36 Edg/82.0.423.0",
"Cookie":"__gads=ID=c1d24c3e2fed96cc:T=1589175075:S=ALNI_MYu2QLf8EgpbLdcVijZLPuQfMS83g; htVD_2132_connect_is_bind=1; htVD_2132_nofavfid=1; htVD_2132_ignore_rate=1; Hm_lvt_46d556462595ed05e05f009cdafff31a=1591778838; htVD_2132_smile=301D1; htVD_2132_home_readfeed=1593569952; KF4=kG2V0G; htVD_2132_atarget=1; htVD_2132_sid=0; htVD_2132_atlist=1073100%2C909963%2C962476; htVD_2132_lastviewtime=1277341%7C1599483571; htVD_2132_saltkey=NoypPW1O; htVD_2132_lastvisit=1599610010; htVD_2132_auth=01afHxhSRPbhl%2B9CV7VAUTUU2QojRmK%2FAX8ye4eJGafJFvw7cWcRBEEzPea3CnXpL%2BwUHMSxwwVHe38t0xfDVcF8VQWm; htVD_2132_noticonf=1277341D1D3_3_1; htVD_2132_ttask=1277341%7C20200914; htVD_2132_forum_lastvisit=D_62_1597838525D_10_1598495771D_41_1598512638D_65_1599729468D_16_1599963520D_66_1600049398D_72_1600049410D_15_1600049417; htVD_2132_visitedfid=8D21D65D66D15; htVD_2132_viewid=tid_1266860; htVD_2132_ulastactivity=1600057891%7C0; htVD_2132_lastcheckfeed=1277341%7C1600057891; htVD_2132_st_p=1277341%7C1600057896%7Cf4b5b6a2a3adf96baca5d761481ba6e1; htVD_2132_lastact=1600058799%09plugin.php%09"
}
req = request.Request(url=url,headers=header)
resp = request.urlopen(req)
#print(resp.read().decode('gbk'))
with open('52.html','w',encoding='gbk') as fp:
    fp.write(resp.read().decode('gbk'))

'''requests 发送 post 请求 '''
import request
data = {


}
headers = {
    "Cookie":"",
    "User-Agent":"",
    "":"",
}
"""

request 代理
"""
proxy = {
    "http":"10.1.88.4"
    }
url = ""
response = request.post(url)
#print(response.text)
print(response.json()) #返回字典形式

"""

request爬虫
"""
import requests
url = "https://www.baidu.com"
response = requests.get(url)
print(response.cookies.get_dict())  #以字典形式获取cookie信息
"""

session 会话信息登录
""""
import requests
url = "https://***.Login"
data = {"email":"","password":""}
headers = {
    "User-Agent":"",
    "Cookies":""
}
#登录
session = requests.session()
session.post(url = url,data=data,headers=headers)
#访问个人中心
resp = session.get("",verify=False)  #不被信任ssl证书
print(resp.text)
"""
xpath
"""
xpath helper
使用方式：
使用//获取整个页面当中的元素，然后写标签名，然后再写谓词进行提取
//div[@class="s_position"]
//div[@class="pic" and id=""]

1./和//区别
/是只获取子节点，//获取子孙节点
2.某个属性包含了多个值，可用contains
//div[contains(@class,'job_detail')]
"""

lxml
"""
from lxml import etree
text = """
html
"""

def parse_text():
    parser = etree.HTMLParser()
    htmlel = etree.HTML(text,parser=parser)  #使用HTML解析
    print(etree.tostring(htmlel, encoding=('utf-8')).decode('utf-8'))  #默认是UNICODE，先编码，再解码为utf-8
def parse_file():
    htmlel = etree.parse("tencent.html")
    print(etree.tostring(htmlel, encoding=('gbk')).decode('gbk'))
if __name__ == "__main__":
    parse_text()
"""


编码与解码
"""
import urllib.parse
text = "http://v.stu.nchu.edu.cn/2020/0926/阳光电影www.ygdy8.com.监视资本主义：智能陷阱.BD.1080p.中英双字幕.mp4"
en_text = urllib.parse.quote(text)
de_text = urllib.parse.unquote(text)
print(text)
print(en_text)
print(de_text)
"""


爬取校园网所有视频链接
"""
from urllib import request
from lxml import etree
#爬取
header = {
    "Cookie":"nchusso=UID=18014211%40stu.nchu.edu.cn&Sname=%e5%95%86%e6%95%96%e5%8d%8e&Sign=OgdCNbZxPSOnnR3bVMv4sqfJ7FTICsGnu3gIlWRXx17gvbupD21AKiW4%2bMzFpvR5yaXB2dwPzWs5%2bezv%2fmpTRtH%2fvNku79OTUSiaFRzjAxiT%2b366bTvChz91X0ovxD5DjK2cjkn2pePlOGOgysFSrbAmKE0ADzTKBncDN3iY35o%3d&Password=d07zKsDNYFE10FzkfoMj80sTaQRDghu37Ww0ZvczhC0rFyrH56%2bCiAkMQHJhHs4s%2fTEka33%2fbwE3KlBbOMLNnFbVvnaS78QkW7UAjZ1HRhOnC3evwtohrYtWn%2fgYCGmAQZdgtkO%2f8wPScYqCIvR5pW5X%2fej%2fSJMDtw78BT1qB00%3d&EndTime=2020%2f9%2f28+23%3a25%3a44&Websites=35%2c11; ASP.NET_SessionId=5ng1gyckkhdpvpqxe3diuhab; Hm_lvt_7b6b7838ea6c62b676abdfd6aae3b36a=1601288275,1601288341; Hm_lpvt_7b6b7838ea6c62b676abdfd6aae3b36a=1601288341"
    #这里填你自己的cookie
}
def spider(i):
    url = "http://movie.stu.nchu.edu.cn/Movie.aspx?MovieID={}".format(i)
    req = request.Request(url=url, headers=header)
    resp = request.urlopen(req)
    html = resp.read().decode('utf-8')
    parser = etree.HTMLParser()
    html = etree.HTML(html, parser=parser)
    # 读取  生成 目录.txt
    divs = html.xpath("//div[@class='product']/input/@value")
    for div in divs:
        print("已爬取{}个视频,{}".format(i,div))
        with open("目录2.txt", "a", encoding='utf-8') as f:
            f.write(div)
            f.write("\n")
if __name__ == "__main__":
    for i in range(4600,4635):
        spider(i)
"""


response.text :网页返回的数据自动解码为unicode
response.content :返回原始数据，bytes，当text返回为乱码时需要手动解码

字典的使用方法
"""
movie = {}
movie['title'] = title
movie['cover'] = cover
movie[pic] = pic


"""

字符串替换
"""
info.replace("@年  代","")。strip()   #替换，去除文本前后空格
"""

电影天堂爬虫
"""
#爬取
from lxml import etree
import requests
BaseUrl = "https://www.dy2018.com"
Detail_Url_List = []
HEADER = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4050.0 Safari/537.36 Edg/82.0.423.0",
    }

def get_detail_urls(url):
    response = requests.get(url, headers=HEADER)
    text = response.content.decode("gbk")
    #text =response.text    编码有乱码时可以用自带解析方式
    # 解析
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a[2]/@href")
    for detail_url in detail_urls:
        detail_url = BaseUrl+detail_url
        Detail_Url_List.append(detail_url)

def spider():
    movies = []
    for i in range(2,3):
        url = "https://www.dy2018.com/1/index_{}.html".format(i)
        get_detail_urls(url)
    for Detail_Url in Detail_Url_List:
        print(Detail_Url)
        movie = parse_detail_page(Detail_Url)
        movies.append(movie)
        print(movie)
        """
    for i in movies:
        print(i)
        """




def parse_detail_page(url):
    response = requests.get(url=url,headers=HEADER)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    """
    brs = html.xpath("//div[@class='title_all']/h1/text()")[0]  #title
    print(brs)
    #pic src
    pics = html.xpath("//div[@id='Zoom']/img/@src")[0]
    print(pics)
    """
    movie = {}
    Zooms = html.xpath("//div[@id='Zoom']")[0]
    brs = Zooms.xpath(".//text()")
    for br in brs:
        if br.startswith("◎译　　名"):
            br = br.replace("◎译　　名","").strip()
            movie['Ename'] = br
        elif br.startswith("◎片　　名"):
            br = br.replace("◎片　　名", "").strip()
            movie['name'] = br
        elif br.startswith('◎年　　代'):
            br = br.replace("◎年　　代", "").strip()
            movie['year'] = br
        elif br.startswith('◎产　　地'):
            br = br.replace("◎产　　地", "").strip()
            movie['area'] = br
        elif br.startswith('◎类　　别'):
            br = br.replace("◎类　　别", "").strip()
            movie['class'] = br
        elif br.startswith('◎片　　长'):
            br = br.replace("◎片　　长", "").strip()
            movie['time'] = br
        elif br.startswith('◎文件大小'):
            br = br.replace("◎文件大小", "").strip()
            movie['file_size'] = br
        elif br.startswith('◎导　　演'):
            br = br.replace("◎导　　演", "").strip()
            movie['director'] = br
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url

    return movie


if __name__ == "__main__":
    
    spider()






"""


爬虫4K彼岸图网
"""
import requests
from lxml import etree
BaseUrl = "http://pic.netbian.com"
#爬取单个页面
Header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4050.0 Safari/537.36 Edg/82.0.423.0",
    "Cookie":"__cfduid=dad713eef9bc1a57a7b9f1c60157654701600916376; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1600949917,1600953314; zkhanecookieclassrecord=%2C53%2C54%2C55%2C66%2C",
    "Referer":"http://pic.netbian.com/4kdongman/"
}

url = "http://pic.netbian.com/4kfengjing/"
response = requests.get(url=url,headers=Header)
text = response.content.decode('gbk')
#解析

html = etree.HTML(text)
pics = html.xpath("//ul[@class='clearfix']//li/a/@href")
for pic in pics:
    print(BaseUrl+pic)





"""











