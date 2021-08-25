# _*_ coding: utf-8/GBK/gb18030 _*_
#@Time    :2021/8/24 21:24 *
import os
import re
import jieba.analyse
import time

def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    sentence_depart = jieba.cut(sentence.strip())
    # 导入停用词列表
    stopwords = ['治目','远视','出方','瞳子','一斗','又方','仰卧','治下','筛','曝干','也','二两','一合','瘥','KT',
                 '七枚','以水二升','四味','细书','暗方','不明','明目','主之','如','丸','各','千金','敷目','治眼',
                 '一两','食后','三味','二味','方寸','百日','精为','二合','六铢','一升','末','三两','洗面','捣',
                 '煎','本','治面','半两','二味','令','去','一升','滓','酒服']
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr
# 获取文件路径
dataset_path= os.path.abspath('..')
datafile2 = os.path.join(dataset_path, 'yc_pl\gu_csv')

for i in range(6,8):
    #  验证权重高的次,出现次数
    if i == 6:
        data_fi = datafile2+'\yf_mu'+str(i)+'.csv'
        with open(data_fi,'r',encoding = 'utf8') as f:
            fl = f.read()
        # 使用结巴分词取出权重
        tags = jieba.analyse.extract_tags(seg_depart(fl),withWeight = False)

        def data_number():
            number = [len(re.findall(j, seg_depart(fl))) for j in tags][:10]
            return number

        def data_name():
            name = [re.findall(j, seg_depart(fl))[0] for j in tags][:10]
            return name

    elif i == 7:
        data_f = datafile2+'\yf_mu'+str(i)+'.csv'
        with open(data_f,'r',encoding = 'utf8') as f:
            fli = f.read()
        # 使用结巴分词取出权重
        tags1 = jieba.analyse.extract_tags(seg_depart(fli),withWeight = False)

        def data_number1():
            number1 = [len(re.findall(y, seg_depart(fli))) for y in tags1][:10]
            return number1

        def data_name1():
            name1 = [re.findall(y, seg_depart(fli))[0] for y in tags1][:10]
            return name1

