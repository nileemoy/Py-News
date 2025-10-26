import requests
from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
import webbrowser
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")


class newsapp:
    def __init__(self):
        self.data = requests.get(
            f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}').json()

    # load GUI
        self.load_gui()

        # load news items
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('900x600')
        self.root.resizable(0, 0)
        self.root.config(bg='black')

    def load_news_item(self, index):

        # clear the old news
        pass

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):

        self.clear()

        # image

        img_url = self.data['articles'][index]['urlToImage']
        raw_data = urlopen(img_url).read()
        im = Image.open(io.BytesIO(raw_data)).resize((900, 250))
        ImageTk.PhotoImage(im)
        photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image=photo)
        label.pack()

        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white',
                        wraplength=900, justify='center')
        heading.pack(pady=(20, 10))
        heading.config(font=('verdana', 18))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=900, justify='center')
        details.pack(pady=(2, 10))
        details.config(font=('verdana', 15))

        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        prev = Button(frame, text='Prev', width=40, height=3,
                      command=lambda: self.load_news_item(index - 1))
        prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=41, height=3, command=lambda: self.open_link(
            self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        next = Button(frame, text='Next', width=40, height=3,
                      command=lambda: self.load_news_item(index + 1))
        next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)


obj = newsapp()
