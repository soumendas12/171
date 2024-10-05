from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("600x400")
india_image=ImageTk.PhotoImage(Image.open("India.png"))
usa_image=ImageTk.PhotoImage(Image.open("USA.jpg"))
india_label=Label(root,text="India")
india_label.place(relx=0.25,rely=0.01,anchor=CENTER)
india_clock=Label(root)
india_clock["image"]=india_image
india_clock.place(relx=0.25,rely=0.2,anchor=CENTER)
india_time=Label(root)
india_time.place(relx=0.25,rely=0.4,anchor=CENTER)

aus_image=ImageTk.PhotoImage(Image.open("Australia.jpg"))
jap_image=ImageTk.PhotoImage(Image.open("Japan.jpg"))
aus_label=Label(root,text="Australia")
aus_label.place(relx=0.25,rely=0.51,anchor=CENTER)
aus_clock=Label(root)
aus_clock["image"]=aus_image
aus_clock.place(relx=0.25,rely=0.7,anchor=CENTER)
aus_time=Label(root)
aus_time.place(relx=0.25,rely=0.9,anchor=CENTER)

jap_label=Label(root,text="Japan")
jap_label.place(relx=0.7,rely=0.51,anchor=CENTER)
jap_clock=Label(root)
jap_clock["image"]=jap_image
jap_clock.place(relx=0.7,rely=0.7,anchor=CENTER)
jap_time=Label(root)
jap_time.place(relx=0.7,rely=0.9,anchor=CENTER)

usa_label=Label(root,text="USA")
usa_label.place(relx=0.7,rely=0.01,anchor=CENTER)
usa_clock=Label(root)
usa_clock["image"]=usa_image
usa_clock.place(relx=0.7,rely=0.2,anchor=CENTER)
usa_time=Label(root)
usa_time.place(relx=0.7,rely=0.4,anchor=CENTER)

class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time : "+ current_time
        india_time.after(200,self.times)
class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time : "+ current_time
        usa_time.after(200,self.times)
class Australia():
    def times(self):
        home=pytz.timezone('Australia/ACT')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time : "+ current_time
        usa_time.after(200,self.times)
class Japan():
    def times(self):
        home=pytz.timezone('Asia/Tokyo')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time : "+ current_time
        usa_time.after(200,self.times)
        
obj_india=India()
obj_usa=USA()
obj_aus=Australia()
obj_jap=Japan()
india_btn=Button(root,text="Show Time",command=obj_india.times)
india_btn.place(relx=0.25,rely=0.45,anchor=CENTER)
usa_btn=Button(root,text="Show Time",command=obj_usa.times)
usa_btn.place(relx=0.7,rely=0.45,anchor=CENTER)
aus_btn=Button(root,text="Show Time",command=obj_aus.times)
aus_btn.place(relx=0.25,rely=0.94,anchor=CENTER)
jap_btn=Button(root,text="Show Time",command=obj_jap.times)
jap_btn.place(relx=0.7,rely=0.94,anchor=CENTER)
root.mainloop()