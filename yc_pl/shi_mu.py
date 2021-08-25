from pyecharts.charts import Radar,Pie
from pyecharts import options as opts
# 使用 snapshot-selenium 渲染图片
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
import csv_clean
from PIL import Image
import os
import time
dataset_path= os.path.abspath('')
datafile2 = os.path.join(dataset_path,'tu_png')

def tus(xs,ys):
    na_m = csv_clean.data_name() # 面药名字
    nu_b = csv_clean.data_number()  # 面药次数
    na_m1 = csv_clean.data_name1()  # 目药名字
    nu_b1 = csv_clean.data_number1()  # 目药次数
    for i in range(6,8):
        if i == 6:
            pie_tu = datafile2+'\pie'+str(i)+'.png'
            # na_m = csv_clean.data_name()
            # nu_b = csv_clean.data_number()
            c = (
                Pie(init_opts=opts.InitOpts(theme=ThemeType.WHITE, bg_color='#f2eada'))
                .add("",[list(z) for z in zip(na_m,nu_b)],rosetype="radius")
                .set_global_opts(title_opts=opts.TitleOpts(title="Pie-药材频率"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            )
            make_snapshot(snapshot, c.render(), pie_tu)
            im = Image.open(pie_tu)
            out = im.resize((xs,ys),Image.ANTIALIAS)  #调整
            out.save(pie_tu)

            radar_tu = datafile2+'\pie'+str(i+1)+'.png'
            c1 = (
                Radar(init_opts = opts.InitOpts(theme = ThemeType.WHITE,bg_color = '#f2eada'))
                .add_schema(
                    schema = [opts.RadarIndicatorItem(name = i,max_ = 30) for i in na_m[:10]],
                    textstyle_opts = opts.TextStyleOpts(color = '#f15a22'))
                .add(series_name = '药材频率',data = [nu_b],color = "#2a5caa",
                     areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),
                     linestyle_opts = opts.LineStyleOpts(width = 1))
                .set_series_opts(label_opts = opts.LabelOpts(is_show = True))
                .set_global_opts(legend_opts = opts.LegendOpts(selected_mode = "single"),
                                 title_opts = opts.TitleOpts(title = "Radar-药材雷达图")))
            make_snapshot(snapshot, c1.render(), radar_tu)
            im = Image.open(radar_tu)
            out = im.resize((xs,ys),Image.ANTIALIAS)  #调整
            out.save(radar_tu)

        elif i == 7:
            pie_t = datafile2+r'\radar'+str(i)+'.png'
            # na_m1 = csv_clean.data_name1()
            # nu_b1 = csv_clean.data_number1()
            c3 = (
                Pie(init_opts = opts.InitOpts(theme = ThemeType.WHITE,bg_color = '#f2eada'))
                .add("",[list(z) for z in zip(na_m1,nu_b1)],rosetype = "radius")
                .set_global_opts(title_opts = opts.TitleOpts(title = "Pie-药材频率"))
                .set_series_opts(label_opts = opts.LabelOpts(formatter = "{b}: {c}"))
            )
            make_snapshot(snapshot,c3.render(),pie_t)
            im = Image.open(pie_t)
            out = im.resize((xs,ys),Image.ANTIALIAS)  #调整
            out.save(pie_t)

            radar_t = datafile2+r'\radar'+str(i+1)+'.png'
            c4 = (
                Radar(init_opts = opts.InitOpts(theme = ThemeType.WHITE,bg_color = '#f2eada'))
                .add_schema(
                    schema = [opts.RadarIndicatorItem(name = i,max_ = 15) for i in na_m1[:10]],
                    textstyle_opts = opts.TextStyleOpts(color = '#f15a22'))
                .add(series_name = '药材频率',data = [nu_b1],color = "#2a5caa",
                     areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),
                     linestyle_opts = opts.LineStyleOpts(width = 1))
                .set_series_opts(label_opts = opts.LabelOpts(is_show = True))
                .set_global_opts(legend_opts = opts.LegendOpts(selected_mode = "single"),
                                 title_opts = opts.TitleOpts(title = "Radar-药材雷达图"))
            )
            make_snapshot(snapshot,c4.render(),radar_t)
            im = Image.open(radar_t)
            out = im.resize((xs,ys),Image.ANTIALIAS)  #调整
            out.save(radar_t)
            time.sleep(1)