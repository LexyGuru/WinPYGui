from tkinter import *


@staticmethod
def teszt():
    ws = Tk()
    ws.title('Video Editor List')
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

            if val == "Electronics Arts":
                import webbrowser
                webbrowser.open("https://www.ea.com/ea-app")

            if val == "Steam":
                import webbrowser
                webbrowser.open("https://store.steampowered.com/")

            if val == "Epic Games":
                import webbrowser
                webbrowser.open("https://www.epicgames.com/site/de/home")

            if val == "Battle.net":
                import webbrowser
                webbrowser.open("https://www.blizzard.com/en-us/apps/battle.net/desktop")

            if val == "Microsoft Game Pass":
                import webbrowser
                webbrowser.open("https://www.xbox.com/en-US/xbox-game-pass/pc-game-pass")

            if val == "Ubisoft":
                import webbrowser
                webbrowser.open("https://ubisoftconnect.com/")

    show = Label(ws, text=data_lang_json[lang][0]['Weblink']['Select_Your_Apps'], font=("Times", 14), padx=10, pady=10)
    show.pack()

    lb = Listbox(ws, selectmode="multiple")
    lb.pack(padx=10, pady=10, expand=YES, fill="both")

    torrent = ["Electronics Arts",
               "Steam",
               "Epic Games",
               "Battle.net",
               "Microsoft Game Pass",
               "Ubisoft"]

    for item in range(len(torrent)):
        lb.insert(END, torrent[item])
        lb.itemconfig(item, bg="#bdc1d6")

    Button(ws, text=data_lang_json[lang][0]['Weblink']['Show_Selected'], command=showSelected).pack()

    ws.mainloop()


teszt()