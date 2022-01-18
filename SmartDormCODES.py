from tkinter import *
from tkinter import messagebox as ms
import sqlite3

# make database (if not exists already)
with sqlite3.connect('DORMSS.db') as conn:
    c = conn.cursor()

c.execute(
    'CREATE TABLE IF NOT EXISTS Rooms(CARD_NO TEXT NOT NULL ,FULLNAME TEXT NOT NULL, ROOM_NO TEXT NOT NULL,January TEXT NULL, February TEXT INTEGER,March TEXT INTEGER ,April TEXT INTEGER,May TEXT INTEGER ,June TEXT INTEGER ,July TEXT INTEGER ,August TEXT INTEGER ,September TEXT INTEGER ,October TEXT INTEGER ,November TEXT INTEGER ,December TEXT INTEGER );')
conn.commit()
conn.close()



class windowclass():
    frame: Frame
    image: PhotoImage

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master, background="#1f2732", width=400, height=350)
        self.bg_image = PhotoImage(file="home2.png")
        self.x = Label(self.frame, image=self.bg_image, bg="#1f2732").place(y=0, x=125)
        self.lbl = Label(self.frame, text="SMART DORMITORY SYSTEM", fg="white", bg="#1f2732",
                         font=("Tw Cen MT", 16))
        self.lbl.place(x=85, y=120)
        Button(self.frame, text="BOARDERS", height="2", width="20", fg="black", bg="#ffeb09",
               font=("Tw Cen MT", 14), command=self.command_Boarders).place(x=100, y=230)
        Button(self.frame, text="ADMIN", height="2", width="20", fg="black", bg="#ffeb09",
               font=("Tw Cen MT", 14), command=self.command_Admin).place(x=100, y=160)
        self.frame.pack()

        width = 400
        height = 350
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

    def command_Boarders(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        Boarders_Login(toplevel)

    def command_Admin(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        Admin_Menu(toplevel)


class Admin_Menu():
    frame: Frame

    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main, background="#1f2732", width=400, height=350)
        self.bg_image = PhotoImage(file="Admin.png")
        self.x = Label(self.frame, image=self.bg_image, bg="#1f2732").place(y=0, x=125)
        Label(self.frame, text="ADMINISTATOR", fg="white", bg="#1f2732", font=("Tw Cen MT", 14)).place(y=110, x=145)
        Button(self.frame, text="Boarders", textvariable="boarder_btn", height="1", width="20", bg="#ffeb09",
               font=("Tw Cen MT", 12), command=self.AdminBoarder).place(y=140, x=120)
        Button(self.frame, text="View List", textvariable="view_list_btn", height="1", width="20", bg="#ffeb09",
               font=("Tw Cen MT", 12), command=self.command_Admin).place(y=180, x=120)
        Button(self.frame, text="Record", height="1", width="20", bg="#ffeb09",
               font=("Tw Cen MT", 12), command=self.record).place(y=220, x=120)
        Button(self.frame, text="Transaction", height="1", width="20", bg="#ffeb09",
               font=("Tw Cen MT", 12), command=self.transac).place(y=260, x=120)
        Button(self.frame, text="BACK", height="1", width="20", bg="#ffeb09",
               font=("Tw Cen MT", 12), command=self.Back).place(y=300, x=120)
        self.frame.pack()

        width = 400
        height = 350
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.main.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.main.resizable(0, 0)

    def record(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        Record(toplevel)

    def Back(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        windowclass(toplevel)

    def AdminBoarder(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        Admin_Boarder(toplevel)

    def command_Admin(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        view_list(toplevel)

    def transac(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        transaction(toplevel)

class Admin_Boarder():
    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame = Frame(self.main, background="#1f2732", width=350, height=280)
        Label(self.frame, text="BOARDERS", fg="white", bg="#1f2732", font=("Tw Cen MT", 20)).place(y=30, x=125)
        Button(self.frame, text="Add", height="2", width="20", fg="black", bg="#ffeb09",
               font=("Tw Cen MT", 12), command=self.AddBoarder).place(y=100, x=90)
        Button(self.frame, text="Remove", height="2", width="20", fg="black", bg="#ffeb09",
               font=("Tw Cen MT", 12), command=self.RemoveBoarder).place(y=170, x=90)
        self.frame.pack()

        width = 350
        height = 280
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.main.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.main.resizable(0, 0)

    def AddBoarder(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        Add_Boarder(toplevel)

    def RemoveBoarder(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        Remove_Boarder(toplevel)

class view_list():

    def __init__(self, main):

        self.main = main
        self.frame = Frame(self.main, background="#2e3b4e", width=500, height=420)
        Label(self.frame, bg="#2e3b4e", fg="white", text="BOARDERS NAME", font=("Tw Cen MT", 18)).place(y=50, x=30)
        Label(self.frame, bg="#2e3b4e", fg="white", text="|CARD NUMBER", font=("Tw Cen MT", 18)).place(y=50, x=220)
        self.frames = Frame(self.main, background="#1f2732", width=200, height=350)
        Button(self.frames, text="Room1", height="2", width="25", font=("Tw Cen MT", 12), bg="#ffeb09",
               command=self.room1_list).place(x=0, y=40)
        Button(self.frames, text="Room2", height="2", width="25", font=("Tw Cen MT", 12), bg="#ffeb09",
               command=self.room2_list).place(x=0, y=100)
        Button(self.frames, text="Room3", height="2", width="25", font=("Tw Cen MT", 12), bg="#ffeb09",
               command=self.room3_list).place(x=0, y=160)
        Button(self.frames, text="Room4", height="2", width="25", font=("Tw Cen MT", 12), bg="#ffeb09",
               command=self.room4_list).place(x=0, y=220)
        Button(self.frames, text="BACK", height="2", width="25", font=("Tw Cen MT", 12), bg="#375681", fg="white",
               command=self.back).place(x=0, y=280)
        self.frames.place(y=0, x=0)
        self.frame.place(y=0, x=200)
        width = 600
        height = 350
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.main.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.main.resizable(0, 0)

    def room1_list(self):
        self.frame = Frame(self.main, background="#2e3b4e", width=500, height=220)
        self.print_Card = ''
        self.print_Name = ''
        # Query the database
        conn = sqlite3.connect('DORMSS.db')
        c = conn.cursor()
        find_boarders = "SELECT *, oid FROM Rooms WHERE ROOM_NO=?"
        c.execute(find_boarders, [('1')])
        records = c.fetchall()
        print(records)
        for record in records:
            self.print_Name += str(record[1]) + "\n\n"
            self.print_Card += str(record[0]) + "\n\n"
        self.query_label = Label(self.frame, bg="#2e3b4e", fg="white", text=self.print_Name,
                                 font=("Tw Cen MT", 12)).place(y=20, x=30)
        self.query_label = Label(self.frame, bg="#2e3b4e", fg="white", text=self.print_Card,
                                 font=("Tw Cen MT", 12)).place(y=20, x=230)
        # commit changes
        conn.commit()
        self.frame.place(y=80, x=200)

    def room2_list(self):
        self.frame = Frame(self.main, background="#2e3b4e", width=500, height=220)
        self.print_Card = ''
        self.print_Name = ''
        # Query the database
        conn = sqlite3.connect('DORMSS.db')
        c = conn.cursor()
        find_boarders = "SELECT *, oid FROM Rooms WHERE ROOM_NO=?"
        c.execute(find_boarders, [('2')])
        records = c.fetchall()
        print(records)
        for record in records:
            self.print_Name += str(record[1]) + "\n\n"
            self.print_Card += str(record[0]) + "\n\n"
        self.query_label = Label(self.frame, bg="#2e3b4e", fg="white", text=self.print_Name,
                                 font=("Tw Cen MT", 12)).place(y=20, x=30)
        self.query_label = Label(self.frame, bg="#2e3b4e", fg="white", text=self.print_Card,
                                 font=("Tw Cen MT", 12)).place(y=20, x=230)
        # commit changes
        conn.commit()
        self.frame.place(y=80, x=200)

    def room3_list(self):
        self.frame = Frame(self.main, background="#2e3b4e", width=500, height=220)
        self.print_Card = ''
        self.print_Name = ''
        # Query the database
        conn = sqlite3.connect('DORMSS.db')
        c = conn.cursor()
        find_boarders = "SELECT *, oid FROM Rooms WHERE ROOM_NO=?"
        c.execute(find_boarders, [('3')])
        records = c.fetchall()
        print(records)
        for record in records:
            self.print_Name += str(record[1]) + "\n\n"
            self.print_Card += str(record[0]) + "\n\n"
        self.query_label = Label(self.frame, bg="#2e3b4e", fg="white", text=self.print_Name,
                                 font=("Tw Cen MT", 12)).place(y=20, x=30)
        self.query_label = Label(self.frame, bg="#2e3b4e", fg="white", text=self.print_Card,
                                 font=("Tw Cen MT", 12)).place(y=20, x=230)
        # commit changes
        conn.commit()
        self.frame.place(y=80, x=200)

    def room4_list(self):
        self.frame = Frame(self.main, background="#2e3b4e", width=500, height=220)
        self.print_Card = ''
        self.print_Name = ''
        # Query the database
        conn = sqlite3.connect('DORMSS.db')
        c = conn.cursor()
        find_boarders = "SELECT *, oid FROM Rooms WHERE ROOM_NO=?"
        c.execute(find_boarders, [('4')])
        records = c.fetchall()
        print(records)
        for record in records:
            self.print_Name += str(record[1]) + "\n\n"
            self.print_Card += str(record[0]) + "\n\n"
        self.query_label = Label(self.frame, bg="#2e3b4e", fg="white", text=self.print_Name,
                                 font=("Tw Cen MT", 12)).place(y=20, x=30)
        self.query_label = Label(self.frame, bg="#2e3b4e", fg="white", text=self.print_Card,
                                 font=("Tw Cen MT", 12)).place(y=20, x=230)
        # commit changes
        conn.commit()
        self.frame.place(y=80, x=200)

    def back(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        Admin_Menu(toplevel)


class Record():
    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main, background="#2e3b4e", width=1180, height=420)

        self.NameColumn = Frame(self.frame, background="#2e3b4e", width=80, height=380)
        self.Jan = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Feb = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Mar = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Apr = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.May = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Jun = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Jul = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Aug = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Sep = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Oct = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Nov = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Dec = Frame(self.frame, background="#2e3b4e", width=80, height=420)

        Label(self.NameColumn, bg="#2e3b4e", fg="white", text="NAMES", font=("Tw Cen MT", 11)).place(y=10, x=20)
        Label(self.Jan, bg="#384e6f", fg="white", text="JANUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Feb, bg="#2e3b4e", fg="white", text="FEBRUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Mar, bg="#384e6f", fg="white", text="MARCH", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Apr, bg="#2e3b4e", fg="white", text="APRIL", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.May, bg="#384e6f", fg="white", text="MAY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jun, bg="#2e3b4e", fg="white", text="JUNE", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jul, bg="#384e6f", fg="white", text="JULY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Aug, bg="#2e3b4e", fg="white", text="AUGUST", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Sep, bg="#384e6f", fg="white", text="SEPTEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Oct, bg="#2e3b4e", fg="white", text="OCTOBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Nov, bg="#384e6f", fg="white", text="NOVEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Dec, bg="#2e3b4e", fg="white", text="DECEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)

        self.NameColumn.place(y=0, x=0)
        self.Jan.place(y=0, x=150)
        self.Feb.place(y=0, x=230)
        self.Mar.place(y=0, x=310)
        self.Apr.place(y=0, x=390)
        self.May.place(y=0, x=470)
        self.Jun.place(y=0, x=550)
        self.Jul.place(y=0, x=630)
        self.Aug.place(y=0, x=710)
        self.Sep.place(y=0, x=790)
        self.Oct.place(y=0, x=870)
        self.Nov.place(y=0, x=950)
        self.Dec.place(y=0, x=1030)

        self.frames = Frame(self.main, background="#1f2732", width=200, height=420)
        Label(self.frames, text="RECORDS", font=("Tw Cen MT", 18), fg="white", bg="#1f2732").place(x=50, y=40)
        Button(self.frames, text="Room1", height="2", width="25", font=("Tw Cen MT", 12), bg="#ffeb09", command = self.room1_record).place(x=0, y=100)
        Button(self.frames, text="Room2", height="2", width="25", font=("Tw Cen MT", 12), bg="#ffeb09", command = self.room2_record).place(x=0, y=160)
        Button(self.frames, text="Room3", height="2", width="25", font=("Tw Cen MT", 12), bg="#ffeb09", command = self.room3_record).place(x=0, y=220)
        Button(self.frames, text="Room4", height="2", width="25", font=("Tw Cen MT", 12), bg="#ffeb09", command = self.room4_record).place(x=0, y=280)
        Button(self.frames, text="BACK", height="2", width="25", font=("Tw Cen MT", 12), bg="#375681", fg="white", command = self.BACK).place(x=0, y=340)
        self.frames.place(y=0, x=0)
        self.frame.place(y=0, x=200)


        width = 1300
        height = 420
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.main.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.main.resizable(0, 0)

    def BACK(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        Admin_Menu(toplevel)

    def room1_record(self):
        self.boarder_name = ''
        self.January = ''
        self.February = ''
        self.March = ''
        self.April = ''
        self.Mays = ''
        self.June = ''
        self.July = ''
        self.August = ''
        self.September = ''
        self.October = ''
        self.November = ''
        self.December = ''
        self.NameColumn = Frame(self.frame, background="#2e3b4e", width=80, height=380)
        self.Jan = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Feb = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Mar = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Apr = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.May = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Jun = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Jul = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Aug = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Sep = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Oct = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Nov = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Dec = Frame(self.frame, background="#2e3b4e", width=80, height=420)

        Label(self.NameColumn, bg="#2e3b4e", fg="white", text="NAMES", font=("Tw Cen MT", 11)).place(y=10, x=20)
        Label(self.Jan, bg="#384e6f", fg="white", text="JANUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Feb, bg="#2e3b4e", fg="white", text="FEBRUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Mar, bg="#384e6f", fg="white", text="MARCH", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Apr, bg="#2e3b4e", fg="white", text="APRIL", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.May, bg="#384e6f", fg="white", text="MAY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jun, bg="#2e3b4e", fg="white", text="JUNE", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jul, bg="#384e6f", fg="white", text="JULY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Aug, bg="#2e3b4e", fg="white", text="AUGUST", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Sep, bg="#384e6f", fg="white", text="SEPTEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Oct, bg="#2e3b4e", fg="white", text="OCTOBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Nov, bg="#384e6f", fg="white", text="NOVEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Dec, bg="#2e3b4e", fg="white", text="DECEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)

        self.NameColumn.place(y=0, x=0)
        self.Jan.place(y=0, x=150)
        self.Feb.place(y=0, x=230)
        self.Mar.place(y=0, x=310)
        self.Apr.place(y=0, x=390)
        self.May.place(y=0, x=470)
        self.Jun.place(y=0, x=550)
        self.Jul.place(y=0, x=630)
        self.Aug.place(y=0, x=710)
        self.Sep.place(y=0, x=790)
        self.Oct.place(y=0, x=870)
        self.Nov.place(y=0, x=950)
        self.Dec.place(y=0, x=1030)

        conn = sqlite3.connect('DORMSS.db')
        c = conn.cursor()
        find_boarders = "SELECT *, oid FROM Rooms WHERE ROOM_NO = '1'"
        c.execute(find_boarders)
        self.records = c.fetchall()

        self.display2()

    def room2_record(self):
        self.boarder_name = ''
        self.January = ''
        self.February = ''
        self.March = ''
        self.April = ''
        self.Mays = ''
        self.June = ''
        self.July = ''
        self.August = ''
        self.September = ''
        self.October = ''
        self.November = ''
        self.December = ''
        self.NameColumn = Frame(self.frame, background="#2e3b4e", width=80, height=380)
        self.Jan = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Feb = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Mar = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Apr = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.May = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Jun = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Jul = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Aug = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Sep = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Oct = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Nov = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Dec = Frame(self.frame, background="#2e3b4e", width=80, height=420)

        Label(self.NameColumn, bg="#2e3b4e", fg="white", text="NAMES", font=("Tw Cen MT", 11)).place(y=10, x=20)
        Label(self.Jan, bg="#384e6f", fg="white", text="JANUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Feb, bg="#2e3b4e", fg="white", text="FEBRUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Mar, bg="#384e6f", fg="white", text="MARCH", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Apr, bg="#2e3b4e", fg="white", text="APRIL", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.May, bg="#384e6f", fg="white", text="MAY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jun, bg="#2e3b4e", fg="white", text="JUNE", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jul, bg="#384e6f", fg="white", text="JULY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Aug, bg="#2e3b4e", fg="white", text="AUGUST", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Sep, bg="#384e6f", fg="white", text="SEPTEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Oct, bg="#2e3b4e", fg="white", text="OCTOBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Nov, bg="#384e6f", fg="white", text="NOVEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Dec, bg="#2e3b4e", fg="white", text="DECEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)

        self.NameColumn.place(y=0, x=0)
        self.Jan.place(y=0, x=150)
        self.Feb.place(y=0, x=230)
        self.Mar.place(y=0, x=310)
        self.Apr.place(y=0, x=390)
        self.May.place(y=0, x=470)
        self.Jun.place(y=0, x=550)
        self.Jul.place(y=0, x=630)
        self.Aug.place(y=0, x=710)
        self.Sep.place(y=0, x=790)
        self.Oct.place(y=0, x=870)
        self.Nov.place(y=0, x=950)
        self.Dec.place(y=0, x=1030)

        conn = sqlite3.connect('DORMSS.db')
        c = conn.cursor()
        find_boarders = "SELECT *, oid FROM Rooms WHERE ROOM_NO = '2'"
        c.execute(find_boarders)
        self.records = c.fetchall()

        self.display2()

    def room3_record(self):
        self.boarder_name = ''
        self.January = ''
        self.February = ''
        self.March = ''
        self.April = ''
        self.Mays = ''
        self.June = ''
        self.July = ''
        self.August = ''
        self.September = ''
        self.October = ''
        self.November = ''
        self.December = ''
        self.NameColumn = Frame(self.frame, background="#2e3b4e", width=80, height=380)
        self.Jan = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Feb = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Mar = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Apr = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.May = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Jun = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Jul = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Aug = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Sep = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Oct = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Nov = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Dec = Frame(self.frame, background="#2e3b4e", width=80, height=420)

        Label(self.NameColumn, bg="#2e3b4e", fg="white", text="NAMES", font=("Tw Cen MT", 11)).place(y=10, x=20)
        Label(self.Jan, bg="#384e6f", fg="white", text="JANUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Feb, bg="#2e3b4e", fg="white", text="FEBRUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Mar, bg="#384e6f", fg="white", text="MARCH", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Apr, bg="#2e3b4e", fg="white", text="APRIL", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.May, bg="#384e6f", fg="white", text="MAY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jun, bg="#2e3b4e", fg="white", text="JUNE", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jul, bg="#384e6f", fg="white", text="JULY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Aug, bg="#2e3b4e", fg="white", text="AUGUST", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Sep, bg="#384e6f", fg="white", text="SEPTEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Oct, bg="#2e3b4e", fg="white", text="OCTOBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Nov, bg="#384e6f", fg="white", text="NOVEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Dec, bg="#2e3b4e", fg="white", text="DECEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)

        self.NameColumn.place(y=0, x=0)
        self.Jan.place(y=0, x=150)
        self.Feb.place(y=0, x=230)
        self.Mar.place(y=0, x=310)
        self.Apr.place(y=0, x=390)
        self.May.place(y=0, x=470)
        self.Jun.place(y=0, x=550)
        self.Jul.place(y=0, x=630)
        self.Aug.place(y=0, x=710)
        self.Sep.place(y=0, x=790)
        self.Oct.place(y=0, x=870)
        self.Nov.place(y=0, x=950)
        self.Dec.place(y=0, x=1030)

        conn = sqlite3.connect('DORMSS.db')
        c = conn.cursor()
        find_boarders = "SELECT *, oid FROM Rooms WHERE ROOM_NO = '3'"
        c.execute(find_boarders)
        self.records = c.fetchall()

        self.display2()

    def room4_record(self):
        self.boarder_name = ''
        self.January = ''
        self.February = ''
        self.March = ''
        self.April = ''
        self.Mays = ''
        self.June = ''
        self.July = ''
        self.August = ''
        self.September = ''
        self.October = ''
        self.November = ''
        self.December = ''
        self.NameColumn = Frame(self.frame, background="#2e3b4e", width=80, height=380)
        self.Jan = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Feb = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Mar = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Apr = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.May = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Jun = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Jul = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Aug = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Sep = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Oct = Frame(self.frame, background="#2e3b4e", width=80, height=420)
        self.Nov = Frame(self.frame, background="#384e6f", width=80, height=420)
        self.Dec = Frame(self.frame, background="#2e3b4e", width=80, height=420)

        Label(self.NameColumn, bg="#2e3b4e", fg="white", text="NAMES", font=("Tw Cen MT", 11)).place(y=10, x=20)
        Label(self.Jan, bg="#384e6f", fg="white", text="JANUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Feb, bg="#2e3b4e", fg="white", text="FEBRUARY", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Mar, bg="#384e6f", fg="white", text="MARCH", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Apr, bg="#2e3b4e", fg="white", text="APRIL", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.May, bg="#384e6f", fg="white", text="MAY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jun, bg="#2e3b4e", fg="white", text="JUNE", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Jul, bg="#384e6f", fg="white", text="JULY", font=("Tw Cen MT", 11)).place(y=10, x=10)
        Label(self.Aug, bg="#2e3b4e", fg="white", text="AUGUST", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Sep, bg="#384e6f", fg="white", text="SEPTEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Oct, bg="#2e3b4e", fg="white", text="OCTOBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Nov, bg="#384e6f", fg="white", text="NOVEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)
        Label(self.Dec, bg="#2e3b4e", fg="white", text="DECEMBER", font=("Tw Cen MT", 11)).place(y=10, x=0)

        self.NameColumn.place(y=0, x=0)
        self.Jan.place(y=0, x=150)
        self.Feb.place(y=0, x=230)
        self.Mar.place(y=0, x=310)
        self.Apr.place(y=0, x=390)
        self.May.place(y=0, x=470)
        self.Jun.place(y=0, x=550)
        self.Jul.place(y=0, x=630)
        self.Aug.place(y=0, x=710)
        self.Sep.place(y=0, x=790)
        self.Oct.place(y=0, x=870)
        self.Nov.place(y=0, x=950)
        self.Dec.place(y=0, x=1030)

        conn = sqlite3.connect('DORMSS.db')
        c = conn.cursor()
        find_boarders = "SELECT *, oid FROM Rooms WHERE ROOM_NO = '4'"
        c.execute(find_boarders)
        self.records = c.fetchall()
        # self.display1()


        self.display2()


    def display2(self):
        for record in self.records:
            self.boarder_name += str(record[1]) + "\n\n\n\n"
            self.January += str(record[3]) + "\n\n\n\n"
            self.February += str(record[4]) + "\n\n\n\n"
            self.March += str(record[5]) + "\n\n\n\n"
            self.April += str(record[6]) + "\n\n\n\n"
            self.Mays += str(record[7]) + "\n\n\n\n"
            self.June += str(record[8]) + "\n\n\n\n"
            self.July += str(record[9]) + "\n\n\n\n"
            self.August += str(record[10]) + "\n\n\n\n"
            self.September += str(record[11]) + "\n\n\n\n"
            self.October += str(record[12]) + "\n\n\n\n"
            self.November += str(record[13]) + "\n\n\n\n"
            self.December += str(record[14]) + "\n\n\n\n"
        Label(self.NameColumn, bg="#2e3b4e", fg="white", text=self.boarder_name, font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Jan, bg="#384e6f", fg="white", text=self.January,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Feb, bg="#2e3b4e", fg="white", text=self.February,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Mar, bg="#384e6f", fg="white", text=self.March,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Apr, bg="#2e3b4e", fg="white", text=self.April,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.May, bg="#384e6f", fg="white", text=self.Mays,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Jun, bg="#2e3b4e", fg="white", text=self.June,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Jul, bg="#384e6f", fg="white", text=self.July,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Aug, bg="#2e3b4e", fg="white", text=self.August,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Sep, bg="#384e6f", fg="white", text=self.September,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Oct, bg="#2e3b4e", fg="white", text=self.October,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Nov, bg="#384e6f", fg="white", text=self.November,font=("Tw Cen MT", 12)).place(y=80, x=20)
        Label(self.Dec, bg="#2e3b4e", fg="white", text=self.December,font=("Tw Cen MT", 12)).place(y=80, x=20)


class transaction():
    def __init__(self, main):
        self.main = main
        self.ID = StringVar()
        self.NAME = StringVar()
        self.CASH = StringVar()
        self.MONTH = StringVar()
        self.frame = Frame(self.main, background="#2e3b4e", width=400, height=350)
        Label(self.frame, text="  TRANSACTION", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 18)).place(x=100, y=20)
        Label(self.frame, text="  Card No. : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=85, y=80)
        Entry(self.frame, textvariable=self.ID).place(x=200, y=80)
        Label(self.frame, text="  Name : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=108, y=120)
        Entry(self.frame, textvariable=self.NAME).place(x=200, y=120)
        Label(self.frame, text="  ENTER CASH : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=60, y=160)
        Entry(self.frame, textvariable=self.CASH).place(x=200, y=160)
        Label(self.frame, text="  ENTER MONTH : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=40, y=200)
        Entry(self.frame, textvariable=self.MONTH).place(x=200, y=200)
        Button(self.frame, text="ENTER", height="1", width="15", fg="black", bg="#58a0ac",
               font=("Tw Cen MT", 12), command=self.paid).place(x=60, y=260)
        Button(self.frame, text="BACK", height="1", width="5", fg="black", bg="#ffeb09",
               font=("Tw Cen MT", 12), command=self.back).place(x=330, y=310)
        Button(self.frame, text="CLEAR", height="1", width="15", fg="black", bg="#d45c84",
               font=("Tw Cen MT", 12), command=self.clear).place(x=200, y=260)
        self.frame.pack()

        width = 400
        height = 350
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.main.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.main.resizable(0, 0)

    def clear(self):
        self.ID.set("")
        self.NAME.set("")
        self.CASH.set("")
        self.MONTH.set("")

    def back(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        Admin_Menu(toplevel)

    def paid(self):
        if int(self.CASH.get()) <2000:
            ms.showerror('Failed!', 'Insufficient Cash')
        else:
            self.Input_Transac()

    def Input_Transac(self):
        conns = sqlite3.connect('DORMSS.db')
        con = conns.cursor()
        find_user = "SELECT * FROM Rooms WHERE CARD_NO = ? and  FULLNAME = ?"
        con.execute(find_user, [(self.ID.get()), (self.NAME.get())])
        months = self.MONTH.get()
        result = con.fetchall()

        if result:
            if months == "January":
                self.updates()
            elif months == "February":
                self.updates()
            elif months == "March":
                self.updates()
            elif months == "April":
                self.updates()
            elif months == "May":
                self.updates()
            elif months == "June":
                self.updates()
            elif months == "July":
                self.updates()
            elif months == "August":
                self.updates()
            elif months == "September":
                self.updates()
            elif months == "October":
                self.updates()
            elif months == "November":
                self.updates()
            elif months == "December":
                self.updates()
            else:
                ms.showerror('Failed!', 'Invalid Input of Month. \nFirst Letter should be UPPERCASE')

        else:
            ms.showerror('Failed!', 'Invalid Input of Card number or Name.')

        conns.commit()

    def updates(self):
        conns = sqlite3.connect('DORMSS.db')
        con = conns.cursor()
        months = self.MONTH.get()
        con.execute("UPDATE Rooms SET (" + months + ") = ? WHERE CARD_NO =? and  FULLNAME = ?",
                    ("PAID", (self.ID.get()), (self.NAME.get())))
        # con.execute(monthly, [(self.CASH.get()),(self.ID.get()),(self.NAME.get())])
        ms.showinfo('Success!', 'Transaction Complete')
        self.ID.set("")
        self.NAME.set("")
        self.CASH.set("")
        self.MONTH.set("")
        conns.commit()



class Add_Boarder():
    def __init__(self, main):
        self.main = main
        self.card_no = StringVar()
        self.full_name = StringVar()
        self.room_no = StringVar()
        self.widget()

    def widget(self):
        self.frame = Frame(self.main, background="#2e3b4e", width=350, height=280)
        Label(self.frame, text="  ADD BOARDERS", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 18)).place(x=110, y=10)
        Label(self.frame, text="  Card No. : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=30, y=60)
        Entry(self.frame, textvariable=self.card_no).place(x=150, y=60)
        Label(self.frame, text="  Name : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=30, y=100)
        Entry(self.frame, textvariable=self.full_name).place(x=150, y=100)
        Label(self.frame, text="  Room No. : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=30, y=140)
        Entry(self.frame, textvariable=self.room_no).place(x=150, y=140)
        Button(self.frame, text="ADD", height="1", width="15", fg="black", bg="#58a0ac",
               font=("Tw Cen MT", 12), command=self.submit_boarders).place(x=40, y=200)
        Button(self.frame, text="BACK", height="1", width="15", fg="black", bg="#d45c84",
               font=("Tw Cen MT", 12), command=self.command3).place(x=180, y=200)
        self.frame.pack()
        width = 350
        height = 280
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.main.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.main.resizable(0, 0)

    def submit_boarders(self):
        with sqlite3.connect('DORMSS.db') as conn:
            c = conn.cursor()

        find_user = ('SELECT * FROM Rooms WHERE CARD_NO = ?')
        c.execute(find_user, [(self.card_no.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Card Number Taken Try a Different One.')
        else:
            find_boarders = ('select * from Rooms where ROOM_NO = ?')
            c.execute(find_boarders, [(self.room_no.get())])
            results = c.fetchall()
            row = len(results)
            if int(self.room_no.get()) >= 5:
                ms.showerror('Error!', 'Rooms 1 to 4 Only!')
            elif row not in range(0, 4):
                ms.showerror('Error!', 'Maximum number of Boarders has reach')
            else:
                insert = 'INSERT INTO Rooms(CARD_NO,FULLNAME,ROOM_NO) VALUES(?,?,?)'
                c.execute(insert, [(self.card_no.get()), (self.full_name.get()), (self.room_no.get())])
                # commit changes
                conn.commit()
                # closing connection
                conn.close()
                ms.showinfo('Successful', 'Successfully Added.')
                self.command3()
                self.card_no.set('')
                self.full_name.set('')
                self.room_no.set('')

    def command3(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        Admin_Menu(toplevel)


class Remove_Boarder():
    def __init__(self, main):
        self.main = main
        self.card_number = StringVar()
        self.boarder_name = StringVar()
        self.frame = Frame(self.main, background="#2e3b4e", width=350, height=280)
        Label(self.frame, text="  REMOVE BOARDERS", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 18)).place(x=60, y=40)
        Label(self.frame, text="  Card No. : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=30, y=100)
        Entry(self.frame, textvariable=self.card_number).place(x=150, y=100)
        Label(self.frame, text="  Name : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=30, y=150)
        Entry(self.frame, textvariable=self.boarder_name).place(x=150, y=150)
        Button(self.frame, text="REMOVE", height="1", width="15", fg="black", bg="#58a0ac",
               font=("Tw Cen MT", 12), command=self.remove).place(x=40, y=200)
        Button(self.frame, text="BACK", height="1", width="15", fg="black", bg="#d45c84",
               font=("Tw Cen MT", 12), command=self.command4).place(x=180, y=200)
        self.frame.pack()
        width = 350
        height = 280
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.main.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.main.resizable(0, 0)

    def command4(self):
        self.main.withdraw()
        toplevel = Toplevel(self.main)
        toplevel.geometry("350x350")
        Admin_Menu(toplevel)

    def remove(self):
        with sqlite3.connect('DORMSS.db') as conn:
            cons = conn.cursor()
        combine = ('SELECT * FROM Rooms WHERE CARD_NO = ? AND FULLNAME = ?')
        cons.execute(combine, [(self.card_number.get()), (self.boarder_name.get())])
        if cons.fetchall():
            deletion = ('DELETE FROM Rooms WHERE CARD_NO = ?')
            cons.execute(deletion, [self.card_number.get()])
            # commit changes
            conn.commit()
            # closing connection
            conn.close()
            ms.showinfo('Successful', 'Successfully Deleted.')
            self.card_number.set("")
            self.boarder_name.set("")
        else:
            ms.showerror('Failed', 'Data not Exist or Wrong Input.')


class Boarders_Login():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master, background="#1f2732", width=400, height=320)
        self.bg_image = PhotoImage(file="gate.png")
        self.x = Label(self.frame, image=self.bg_image, bg="#1f2732").place(y=0, x=130)
        self.lbl = Label(self.frame, text="GATE", fg="white", bg="#1f2732",
                         font=("Tw Cen MT", 16))
        self.lbl.place(x=180, y=125)
        Button(self.frame, text="ENTER", height="2", width="20", fg="black", bg="#ffeb09",
               font=("Tw Cen MT", 14), command=self.command).place(x=100, y=230)
        Button(self.frame, text="EXIT", height="2", width="20", fg="black", bg="#ffeb09",
               font=("Tw Cen MT", 14), command=self.command2).place(x=100, y=160)
        self.frame.pack()
        width = 400
        height = 320
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

    def command(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        login(toplevel)
    def command2(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        login2(toplevel)


class room():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master, background="#1f2732", width=400, height=370)
        self.lbl = Label(self.frame, text="ROOM", fg="white", bg="#1f2732", width="300", height="2",
                         font=("Tw Cen MT", 16))
        self.lbl.pack()
        Label(self.frame, text="", bg="#1f2732").pack()

        Button(self.frame, text="ROOM 1", height="1", width="20", bg="#ffeb09",
               font=("Tw Cen MT", 14), command=self.command1).pack()
        Label(self.frame, text="", bg="#1f2732").pack()
        Button(self.frame, text="ROOM 2", height="1", width="20", bg="#ffeb09",
               font=("Tw Cen MT", 14), command=self.command2).pack()
        Label(self.frame, text="", bg="#1f2732").pack()
        Button(self.frame, text="ROOM 3", height="1", width="20", bg="#ffeb09",
               font=("Tw Cen MT", 14), command=self.command3).pack()
        Label(self.frame, text="", bg="#1f2732").pack()
        Button(self.frame, text="ROOM 4", height="1", width="20", bg="#ffeb09",
               font=("Tw Cen MT", 14), command=self.command4).pack()
        Label(self.frame, text="", bg="#1f2732").pack()
        self.frame.pack()
        width = 400
        height = 310
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

    def command1(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        room1(toplevel)

    def command2(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        room2(toplevel)

    def command3(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        room3(toplevel)

    def command4(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        room4(toplevel)


class room1():
    def __init__(self, master):
        self.master = master
        self.ID = StringVar()
        self.NAME = StringVar()

        self.frame = Frame(self.master, background="#2e3b4e", width=350, height=280)
        Label(self.frame, text="  ROOM 1", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 18)).place(x=120, y=40)
        Label(self.frame, text="  Card No. : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=30, y=100)
        Entry(self.frame, textvariable=self.ID).place(x=150, y=100)
        Label(self.frame, text="  Name : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=55, y=150)
        Entry(self.frame, textvariable=self.NAME).place(x=150, y=150)
        Button(self.frame, text="ENTER", height="1", width="15", fg="black", bg="#58a0ac",
               font=("Tw Cen MT", 12), command=self.logging_in).place(x=40, y=200)
        Button(self.frame, text="BACK", height="1", width="15", fg="black", bg="#d45c84",
               font=("Tw Cen MT", 12), command=self.back).place(x=180, y=200)
        self.frame.pack()

        width = 350
        height = 280
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

    def logging_in(self):

        connect = sqlite3.connect('DORMSS.db')
        con = connect.cursor()

        find_user = "SELECT * FROM Rooms WHERE CARD_NO = ? and  FULLNAME = ? and ROOM_NO = ?"
        con.execute(find_user, [(self.ID.get()), (self.NAME.get()), '1'])
        result = con.fetchall()
        if result:
            ms.showinfo('Successful', 'Successfuly Login')
            self.command()
        else:
            ms.showerror('Failed!', 'Username or Password is Incorrect.')

    def command(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        windowclass(toplevel)

    def back(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        room(toplevel)


class room2():
    def __init__(self, master):
        self.master = master
        self.ID = StringVar()
        self.NAME = StringVar()

        self.frame = Frame(self.master, background="#2e3b4e", width=350, height=280)
        Label(self.frame, text="  ROOM 2", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 18)).place(x=120, y=40)
        Label(self.frame, text="  Card No. : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=30, y=100)
        Entry(self.frame, textvariable=self.ID).place(x=150, y=100)
        Label(self.frame, text="  Name : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=55, y=150)
        Entry(self.frame, textvariable=self.NAME).place(x=150, y=150)
        Button(self.frame, text="ENTER", height="1", width="15", fg="black", bg="#58a0ac",
               font=("Tw Cen MT", 12), command=self.logging_in).place(x=40, y=200)
        Button(self.frame, text="BACK", height="1", width="15", fg="black", bg="#d45c84",
               font=("Tw Cen MT", 12), command=self.back).place(x=180, y=200)
        self.frame.pack()

        width = 350
        height = 280
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

    def logging_in(self):

        connect = sqlite3.connect('DORMSS.db')
        con = connect.cursor()

        find_user = "SELECT * FROM Rooms WHERE CARD_NO = ? and  FULLNAME = ? and ROOM_NO = ?"
        con.execute(find_user, [(self.ID.get()), (self.NAME.get()), '2'])
        result = con.fetchall()
        if result:
            ms.showinfo('Successful', 'Successfuly Login')
            self.command()
        else:
            ms.showerror('Failed!', 'Username or Password is Incorrect.')

    def command(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        windowclass(toplevel)

    def back(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        room(toplevel)


class room3():

    def __init__(self, master):
        self.master = master
        self.ID = StringVar()
        self.NAME = StringVar()

        self.frame = Frame(self.master, background="#2e3b4e", width=350, height=280)
        Label(self.frame, text="  ROOM 3", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 18)).place(x=120, y=40)
        Label(self.frame, text="  Card No. : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=30, y=100)
        Entry(self.frame, textvariable=self.ID).place(x=150, y=100)
        Label(self.frame, text="  Name : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=55, y=150)
        Entry(self.frame, textvariable=self.NAME).place(x=150, y=150)
        Button(self.frame, text="ENTER", height="1", width="15", fg="black", bg="#58a0ac",
               font=("Tw Cen MT", 12), command=self.logging_in).place(x=40, y=200)
        Button(self.frame, text="BACK", height="1", width="15", fg="black", bg="#d45c84",
               font=("Tw Cen MT", 12), command=self.back).place(x=180, y=200)
        self.frame.pack()

        width = 350
        height = 280
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

    def logging_in(self):

        connect = sqlite3.connect('DORMSS.db')
        con = connect.cursor()

        find_user = "SELECT * FROM Rooms WHERE CARD_NO = ? and  FULLNAME = ? and ROOM_NO = ?"
        con.execute(find_user, [(self.ID.get()), (self.NAME.get()), '3'])
        result = con.fetchall()
        if result:
            ms.showinfo('Successful', 'Successfuly Login')
            self.command()
        else:
            ms.showerror('Failed!', 'Username or Password is Incorrect.')

    def command(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        windowclass(toplevel)

    def back(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        room(toplevel)


class room4():

    def __init__(self, master):
        self.master = master
        self.ID = StringVar()
        self.NAME = StringVar()

        self.frame = Frame(self.master, background="#2e3b4e", width=350, height=280)
        Label(self.frame, text="  ROOM 4", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 18)).place(x=120, y=40)
        Label(self.frame, text="  Card No. : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=30, y=100)
        Entry(self.frame, textvariable=self.ID).place(x=150, y=100)
        Label(self.frame, text="  Name : ", fg="white", bg="#2e3b4e", font=("Tw Cen MT", 14)).place(x=55, y=150)
        Entry(self.frame, textvariable=self.NAME).place(x=150, y=150)
        Button(self.frame, text="ENTER", height="1", width="15", fg="black", bg="#58a0ac",
               font=("Tw Cen MT", 12), command=self.logging_in).place(x=40, y=200)
        Button(self.frame, text="BACK", height="1", width="15", fg="black", bg="#d45c84",
               font=("Tw Cen MT", 12), command=self.back).place(x=180, y=200)
        self.frame.pack()

        width = 350
        height = 280
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

    def logging_in(self):

        connect = sqlite3.connect('DORMSS.db')
        con = connect.cursor()

        find_user = "SELECT * FROM Rooms WHERE CARD_NO = ? and  FULLNAME = ? and ROOM_NO = ?"
        con.execute(find_user, [(self.ID.get()), (self.NAME.get()), '4'])
        result = con.fetchall()
        if result:
            ms.showinfo('Successful', 'Successfuly Login')
            self.command()
        else:
            ms.showerror('Failed!', 'Username or Password is Incorrect.')

    def command(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        windowclass(toplevel)

    def back(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        room(toplevel)


class login():
    def __init__(self, master):
        self.master = master
        self.ID = StringVar()
        self.NAME = StringVar()

        self.frame = Frame(self.master, background="#1f2732", width=400, height=320)
        self.bg_image = PhotoImage(file="boarders.png")
        self.x = Label(self.frame, image=self.bg_image, bg="#1f2732").place(y=0, x=120)
        self.lbl = Label(self.frame, text="BOARDERS", fg="white", bg="#1f2732",
                         font=("Tw Cen MT", 16))
        self.lbl.place(x=140, y=123)
        Label(self.frame, text="    ID: ", fg="white", font=("Tw Cen MT", 14), bg="#1f2732").place(x=50, y=155)
        Label(self.frame, text="    NAME: ", fg="white", font=("Tw Cen MT", 14), bg="#1f2732").place(x=19, y=185)
        Entry(self.frame, textvariable=self.ID, width=32).place(x=100, y=160)
        Entry(self.frame, textvariable=self.NAME, width=32).place(x=100, y=190)

        Button(self.frame, text="OK", width="10",
               font=("Tw Cen MT", 13), command=self.logging_in, bg="#58a0ac").place(x=90, y=230)
        Button(self.frame, text="BACK", width="10",
               font=("Tw Cen MT", 13), command=self.command5, bg="#d45c84").place(x=200, y=230)

        self.frame.pack()

        width = 380
        height = 320
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

    def logging_in(self):

        conns = sqlite3.connect('DORMSS.db')
        con = conns.cursor()

        find_user = "SELECT * FROM Rooms WHERE CARD_NO = ? and  FULLNAME = ?"
        con.execute(find_user, [(self.ID.get()), (self.NAME.get())])
        result = con.fetchall()
        if result:
            self.command()
        else:
            ms.showerror('Failed!', 'Username or Password is Incorrect.')

    def command(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        room(toplevel)

    def command5(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        windowclass(toplevel)

    def close_windows(self):
        self.master.destroy()


class login2():
    def __init__(self, master):
        self.master = master
        self.ID = StringVar()
        self.NAME = StringVar()

        self.frame = Frame(self.master, background="#1f2732", width=400, height=320)
        self.bg_image = PhotoImage(file="boarders.png")
        self.x = Label(self.frame, image=self.bg_image, bg="#1f2732").place(y=0, x=120)
        self.lbl = Label(self.frame, text="BOARDERS", fg="white", bg="#1f2732",
                         font=("Tw Cen MT", 16))
        self.lbl.place(x=140, y=123)
        Label(self.frame, text="    ID: ", fg="white", font=("Tw Cen MT", 14), bg="#1f2732").place(x=50, y=155)
        Label(self.frame, text="    NAME: ", fg="white", font=("Tw Cen MT", 14), bg="#1f2732").place(x=19, y=185)
        Entry(self.frame, textvariable=self.ID, width=32).place(x=100, y=160)
        Entry(self.frame, textvariable=self.NAME, width=32).place(x=100, y=190)

        Button(self.frame, text="OK", width="10",
               font=("Tw Cen MT", 13), command=self.logging_in, bg="#58a0ac").place(x=90, y=230)
        Button(self.frame, text="BACK", width="10",
               font=("Tw Cen MT", 13), command=self.command, bg="#d45c84").place(x=200, y=230)

        self.frame.pack()

        width = 380
        height = 320
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.master.resizable(0, 0)

    def logging_in(self):

        conns = sqlite3.connect('DORMSS.db')
        con = conns.cursor()

        find_user = "SELECT * FROM Rooms WHERE CARD_NO = ? and  FULLNAME = ?"
        con.execute(find_user, [(self.ID.get()), (self.NAME.get())])
        result = con.fetchall()
        if result:
            ms.showinfo('Successful', 'Access Granted. You may now Exit')
            self.command()
        else:
            ms.showerror('Failed!', 'Username or Password is Incorrect.')

    def command(self):
        self.master.withdraw()
        toplevel = Toplevel(self.master)
        toplevel.geometry("350x350")
        windowclass(toplevel)


root = Tk()
cls = windowclass(root)
root.mainloop()
