import random
from requests_html import HTMLSession
import time
import os
from stylecloud import gen_stylecloud
import re
import jieba.analyse
from PIL import Image

user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
]


url = ['https://so.gushiwen.cn/guwen/bookv_46653FD803893E4F85F6FC53872B2062.aspx',
       'https://so.gushiwen.cn/guwen/bookv_46653FD803893E4FB33C09BE2F99E872.aspx']

herders = {"User-Agent": random.choice(user_agent)}
session =HTMLSession()

dataset_path= os.path.abspath('')
datafile2 = os.path.join(dataset_path)

def file_mu():
    for i in url:
        req =session.get(url=i, headers = herders)

        ret = req.html.xpath('//*[@id="html"]/body/div[2]/div/div/div[1]/div',first=True).text
        name=datafile2 +'\gu_csv\yf_mu' + i[-7:-6]+'.csv'
        with open(name,'w', encoding='utf8') as f:
            f.write(ret)
        time.sleep(1)
        with open(name,'r',encoding = 'utf8') as f:
            # result = " ".join(jieba.cut(f.read(),cut_all=False))  # 分词用空格隔开，全模式
            result = " ".join(jieba.cut(f.read()))  # 精确模式 cut_all=False
            # 返回权重列表,大家可以把False改成True打印一下结果试试,看看有什么不同
        stopwords = ['治目','上','和','中','之','以','方','二两','敷','也','瘥','赤','头','出','枚','着',
                     '煮','目','日','三','不明','为','主之','如','丸','各','如','治','一两','不','翼','服',
                     '洗面','一升','取','七枚','灸','远视','者','方寸','咀','匕','治','散','是','翳','有',
                     '至','一','子','大','勿','曝干','远视','出方','瞳子','一斗','又方','仰卧','治下','筛',
                     '曝干','也','一合','KT','七枚','以水二升','四味','细书','暗方','不明','明目','主之',
                     '如','丸','各','千金','敷目','治眼','食后','三味','百日','精为','二合','六铢','末',
                     '三两','捣','煎','本','治面','半两','二味','令','去','滓','酒服','曰','则','在','病']
        name1=datafile2 +r'\tu_png\yf_mu' + i[-7:-6]+'.png'
        gen_stylecloud(text = result,font_path = 'C:\Windows\Fonts\simkai.ttf',  # 选择展示字体
                       output_name = name1,  # 存取图名称
                       icon_name = 'fas fa-cloud',  # 词云形状名称https://fontawesome.com/v6.0/icons
                       custom_stopwords = stopwords  #停用词
                       )  # 必须加中文字体，否则格式错误
        im = Image.open(name1)
        x_s = 900 # 宽度
        y_s = 600  # 高度
        out = im.resize((x_s,y_s),Image.ANTIALIAS)  #调整
        out.save(name1)  # 保存
file_mu()