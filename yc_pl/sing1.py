# _*_ coding: utf-8/GBK/gb18030 _*_
#@Time    :2021/8/24 16:09 *

import tkinter as tk
from tkinter import ttk
import tkwin as tw
from PIL import ImageTk,Image
import time
import os
import gu_mu
import shi_mu

class Window:
    def __init__(self,parent):
        self.parent = parent
        self.win = tk.Toplevel()
        self.win.geometry("%dx%d" % (1200,900))  # 窗体尺寸
        self.win['bg'] = '#bed742'
        tw.center_window(self.win)  # 将窗体移动到屏幕中央
        self.win.title("病情用药频率查询")  # 窗体标题
        # root.grab_set()
        self.win.resizable()

        self.tabControl = ttk.Notebook(self.win)  # 建立选项卡控件
        ttk.Style().configure(".", font=("华文行楷", 24))
        self.tab1 = ttk.Frame(self.tabControl)  # 创建选项卡
        self.tabControl.add(self.tab1,text='面病')  # 使选项卡可见
        self.tab2 = ttk.Frame(self.tabControl)  # 创建第二个选项卡
        self.tabControl.add(self.tab2,text='目病')
        self.tabControl.pack(expand=1,fill="both",padx=15,pady=10)    # 展示选项卡组件

        dataset_path= os.path.abspath('')
        datafi_0 = os.path.join(dataset_path,r'tu_png\23.jpg')
        photo = ImageTk.PhotoImage(Image.open(datafi_0))
        datafi1 = os.path.join(dataset_path,'tu_png\yf_mu6.png')
        photo1 = ImageTk.PhotoImage(Image.open(datafi1))
        datafi2 = os.path.join(dataset_path,r'tu_png\pie6.png')
        photo2 = ImageTk.PhotoImage(Image.open(datafi2))
        datafi3 = os.path.join(dataset_path,r'tu_png\pie7.png')
        photo3 = ImageTk.PhotoImage(Image.open(datafi3))

        datafi11 = os.path.join(dataset_path,'tu_png\yf_mu7.png')
        photo11 = ImageTk.PhotoImage(Image.open(datafi11))
        datafi22 = os.path.join(dataset_path,r'tu_png\radar7.png')
        photo22 = ImageTk.PhotoImage(Image.open(datafi22))
        datafi33 = os.path.join(dataset_path,r'tu_png\radar8.png')
        photo33 = ImageTk.PhotoImage(Image.open(datafi33))

        # # # 点击按钮显示组件
        def click():
            gu_mu.file_mu()
            shi_mu.tus(1050,650)
            action.configure(text='完成')
        def click_0():
            a_label=tk.Label(mighty,text="云图",compound=tk.BOTTOM,width=1050,height=650,
                             image=photo1,anchor='n',font=("华文行楷",20),)
            a_label.grid(column=0, row=1, padx=20, pady=10)
        def click_1():
            a_label1=tk.Label(mighty,text="pie可视化",compound=tk.BOTTOM,width=1050,height=650,
                              image=photo2,anchor='n',font=("华文行楷",20))
            a_label1.grid(column=0, row=1, padx=20, pady=10)
        def click_2():
            a_label1=tk.Label(mighty,text="radar可视化",compound=tk.BOTTOM,width=1050,height=650,
                              image=photo3,anchor='n',font=("华文行楷",20))
            a_label1.grid(column=0, row=1, padx=20, pady=10)

        def click1():
            action.configure(text='完成')
        def click_00():
            a_label=tk.Label(mighty1,text="云图",compound=tk.BOTTOM,width=1050,height=650,
                             image=photo11,anchor='n',font=("华文行楷",20),)
            a_label.grid(column=0, row=1, padx=20, pady=10)
        def click_11():
            a_label1=tk.Label(mighty1,text="pie可视化",compound=tk.BOTTOM,width=1050,height=650,
                              image=photo22,anchor='n',font=("华文行楷",20))
            a_label1.grid(column=0, row=1, padx=20, pady=10)
        def click_22():
            a_label1=tk.Label(mighty1,text="radar可视化",compound=tk.BOTTOM,width=1050,height=650,
                              image=photo33,anchor='n',font=("华文行楷",20))
            a_label1.grid(column=0, row=1, padx=20, pady=10)

        a_label=tk.Label(self.tab1,image=photo, anchor='n',width=1200,height=800)
        a_label.grid(column=0, row=0, padx=20, pady=10)
        action = ttk.Button(a_label, text='查询',command=click)
        action.grid(column=1, row=1,padx=58, pady=4)
        action1 = ttk.Button(a_label, text='云图',command=click_0)
        action1.grid(column=2, row=1,padx=58, pady=4)
        action2 = ttk.Button(a_label, text='pie可视化',command=click_1)
        action2.grid(column=3, row=1,padx=58, pady=4)
        action3 = ttk.Button(a_label, text='radar可视化',command=click_2)
        action3.grid(column=4, row=1,padx=58, pady=4)
        mighty = ttk.LabelFrame(self.tab1, text='结果')
        mighty.grid(column=0, row=2, padx=0, pady=4)

        a_label1=tk.Label(self.tab2,image=photo, anchor='n',width=1200,height=800)
        a_label1.grid(column=0, row=0, padx=20, pady=10)
        action1 = ttk.Button(a_label1, text='查询',command=click1)
        action1.grid(column=1, row=1,padx=58, pady=4)
        action4 = ttk.Button(a_label1, text='云图',command=click_00)
        action4.grid(column=2, row=1,padx=58, pady=4)
        action5 = ttk.Button(a_label1, text='pie可视化',command=click_11)
        action5.grid(column=3, row=1,padx=58, pady=4)
        action6 = ttk.Button(a_label1, text='radar可视化',command=click_22)
        action6.grid(column=4, row=1,padx=58, pady=4)
        mighty1 = ttk.LabelFrame(self.tab2, text='结果')
        mighty1.grid(column=0, row=2, padx=0, pady=4)

        self.win.iconbitmap('logo1.ico')
        self.win.mainloop()
