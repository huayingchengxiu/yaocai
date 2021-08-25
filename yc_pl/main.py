# coding:utf-8

import tkinter as tk
import tkinter.font as tkfont
from PIL import Image, ImageTk
import tkwin as tw
import sing1

class App:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("%dx%d" % (600, 400))   # 窗体尺寸
		tw.center_window(self.root)               # 将窗体移动到屏幕中央
		self.root.iconbitmap('logo1.ico')  # 窗体图标
		self.root.title("Python-药材频率查询")
		self.root.resizable(False, False)          # 设置窗体不可改变大小
		self.no_title = True
		self.show_title()
		self.body()

	def body(self):
		# ---------------------------------------------------------------------
		# 背景图片
		# ---------------------------------------------------------------------
		self.img = ImageTk.PhotoImage(file="bg2.png")
		canvas = tk.Canvas(self.root)
		canvas.create_image(30, 200, image=self.img)  # 屏幕背景在图片中的位置
		canvas.pack(expand=tk.YES, fill=tk.BOTH)

		# ---------------------------------------------------------------------
		# 标题栏
		# ---------------------------------------------------------------------
		f1 = tk.Frame(canvas)
		im1 = tw.image_label(f1, "logo.png", 86, 70, False)
		im1.configure(bg="#d1c7b7")
		im1.bind('<Button-1>', self.show_title)
		im1.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.Y)

		ft1 = tkfont.Font(family="微软雅黑", size=24, weight=tkfont.BOLD)
		tk.Label(f1, text='Python-药材频率查询', height=2, fg="white", font=ft1, bg="#733a31")\
			.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
		im2 = tw.image_label(f1, "close.png", 86, 72, False)
		im2.configure(bg="#d1c7b7")
		im2.bind('<Button-1>', self.close)
		im2.pack(side=tk.RIGHT, anchor=tk.NW, fill=tk.Y)
		f1.pack(fill=tk.X)

		# ---------------------------------------------------------------------
		# 功能按钮组
		# ---------------------------------------------------------------------
		ft2 = tkfont.Font(family="微软雅黑", size=18, weight=tkfont.BOLD)
		tk.Button(canvas, text="进入系统", bg="#6950a1", command=self.show_single, font=ft2, height=2, fg="white", width=20)\
			.pack(side=tk.LEFT, expand=tk.YES, anchor=tk.CENTER, padx=5)

	def show_title(self, *args):
		self.root.overrideredirect(self.no_title)
		self.no_title = not self.no_title

	def show_single(self):
		sing1.Window(self.root)

	def close(self, *arg):
		if tw.show_confirm("确认退出吗 ?"):
			self.root.destroy()


if __name__ == "__main__":
	app = App()
	app.root.mainloop()
