from tkinter import *

ws = Tk()
ws.title('Media Server List')
ws.geometry('400x300')

var = StringVar()


def showSelected():
    countries = []
    cname = lb.curselection()
    for i in cname:
        op = lb.get(i)
        countries.append(op)
    for val in countries:
        # print(val)

        if val == "Shotcut":
            import webbrowser
            webbrowser.open("https://shotcut.org/download/?utmzz=utmccn%3D%28not+set%29&webuid=whrz1p")

        if val == "OpenShot Video Editor":
            import webbrowser
            webbrowser.open("https://www.openshot.org/download/?utmzz=utmccn%3D%28not+set%29&webuid=whrz1p")

        if val == "DaVinci Resolve 18":
            import webbrowser
            webbrowser.open("https://www.blackmagicdesign.com/products/davinciresolve/?utmzz=utmccn%3D(not%20set)&webuid=whrz1p")

        if val == "Video Editor":
            import webbrowser
            webbrowser.open("https://icecreamapps.com/Video-editor/?utmzz=utmccn%3D%28not+set%29&webuid=whrz1p")

        if val == "Digital Video Editor":
            import webbrowser
            webbrowser.open("https://www.nchsoftware.com/videopad/?utmzz=utmccn%3D%28not+set%29&webuid=whrz1p")

        if val == "HitFilm":
            import webbrowser
            webbrowser.open("https://fxhome.com/product/hitfilm?utmzz=utmccn%3D%28not+set%29&webuid=whrz1p")


show = Label(ws, text="Select Your Country", font=("Times", 14), padx=10, pady=10)
show.pack()

lb = Listbox(ws, selectmode="multiple")
lb.pack(padx=10, pady=10, expand=YES, fill="both")

torrent = ["Shotcut", "OpenShot Video Editor", "DaVinci Resolve 18", "EVideo Editor", "Digital Video Editor", "HitFilm"]

for item in range(len(torrent)):
    lb.insert(END, torrent[item])
    lb.itemconfig(item, bg="#bdc1d6")

Button(ws, text="Show Selected", command=showSelected).pack()

ws.mainloop()