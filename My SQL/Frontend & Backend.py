from tkinter import *
import tkinter.messagebox
import mysql.connector
import time

global sd
class Project_Backend:
    def __init__(self):
        # Establishing MySQL database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootkshitij",
            database="musicify_db"
        )

    def AddMusicRec(self,track_id,track_name=None,Artist=None,duration=None,Album_id=None):  
        cursor = self.connection.cursor() 
        cursor.execute("INSERT INTO Track(track_id,track_name,artist_name,duration,album_id) VALUES (%s,%s, %s, %s,%s)",(track_id, track_name, Artist, duration, Album_id))  # Updated SQL query
        self.connection.commit()
        cursor.close()

    def AddArtistRec(self,Artist_id,Artist_country,Artist,):  
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Artist(artist_id,country,artist_name) VALUES (%s,%s,%s)", (Artist_id, Artist_country, Artist))  
        self.connection.commit()
        cursor.close()

    def ViewMusicData(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Track")
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def ViewArtistData(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Artist")
        data = cursor.fetchall()
        cursor.close()
        return data

    def DeleteMusicRec(self, track_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Track WHERE track_id = %s", (track_id,))
        self.connection.commit()
        cursor.close()

    def UpdateMusicRec(self, track_id, track_name, Artist, duration, album_id, rating):  # Added rating parameter
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Track SET track_name = %s,artist_name = %s, duration = %s, album_id = %s, rating = %s WHERE track_id = %s",
                       (track_name, Artist, duration, album_id, rating, track_id))  # Updated SQL query
        self.connection.commit()
        cursor.close()

    def SearchMusicData(self, track_id=None, track_name=None,Artist=None, duration=None, album_id=None, rating=None):  # Added rating parameter
        cursor = self.connection.cursor()
        query = "SELECT * FROM Track WHERE 1=1"
        parameters = []
        if track_id:
            query += " AND track_id = %s"
            parameters.append(track_id)
        if track_name:
            query += " AND track_name = %s"
            parameters.append(track_name)
        if Artist:
            query += "AND artist_name= %s"
            parameters.append(Artist)
        if duration:
            query += " AND duration = %s"
            parameters.append(duration)
        if album_id:
            query += " AND album_id = %s"
            parameters.append(album_id)
        if rating:  # Added condition for rating parameter
            query += " AND rating = %s"
            parameters.append(rating)
        cursor.execute(query, parameters)
        data = cursor.fetchall()
        cursor.close()
        return data

    
class Music:
    def __init__(self, root):
        self.root=root
        self.root.title("Musicify: Harmonize Your World")
        self.root.geometry("1250x1000")
        self.root.config(bg="black")

        Track_Name=StringVar()
        Track_ID=StringVar()
        Artist=StringVar()
        Artist_id=StringVar()
        Duration=StringVar()
        Album_id=StringVar()
        Artist_country=StringVar()
        Rating=StringVar()
        

        # Functions
        def iExit():
            iExit=tkinter.messagebox.askyesno("Musicify", "Are you sure???")
            if iExit>0:
                root.destroy()
            return

        def clcdata():
            self.txtTrack_ID.delete(0,END)
            self.txtTrack_Name.delete(0,END)
            self.txtArtist.delete(0,END)
            self.txtArtist_id.delete(0,END)
            self.txtAlbum_id.delete(0,END)
            self.txtDuration.delete(0,END)
            self.txtArtist_country.delete(0,END)
            self.txtRating.delete(0,END)

        def disTrackdata():
            MusicList.delete(0,END)
            backend = Project_Backend()  # Creating an instance of Project_Backend
            for row in backend.ViewMusicData():
                MusicList.insert(END, row)

        def disArtistdata():
            MusicList.delete(0,END)
            backend = Project_Backend()  # Creating an instance of Project_Backend
            for row in backend.ViewArtistData():
                MusicList.insert(END, row)

        def musicrec(event):
            try:
                searchmusic = MusicList.curselection()[0]
                sd = MusicList.get(searchmusic)
                self.txtTrack_ID.delete(0,END)
                self.txtTrack_ID.insert(END,sd[0])
                self.txtTrack_Name.delete(0,END)
                self.txtTrack_Name.insert(END,sd[1])
                self.txtArtist.delete(0,END)
                self.txtArtist.insert(END,sd[2])
                self.txtDuration.delete(0,END)
                self.txtDuration.insert(END,sd[3])
                self.txtAlbum_id.delete(0,END)
                self.txtAlbum_id.insert(END,sd[4])
                self.txtRating.delete(0,END)
                self.txtRating.insert(END,sd[5])
            except IndexError:
                pass

        def deldata():
            if(len(Track_ID.get())!=0):
                backend = Project_Backend()  # Creating an instance of Project_Backend
                backend.DeleteMusicRec(sd[0])
                clcdata()
                disTrackdata()  # Display updated data after deletion

        def searchdb():
            MusicList.delete(0,END)
            backend = Project_Backend()
            for row in backend.SearchMusicData(Track_ID.get(), Track_Name.get(),Artist.get(), Duration.get(), Rating.get()):
                MusicList.insert(END, row)


        def addArtistdata():
                backend = Project_Backend()  # Creating an instance of Project_Backend
                backend.AddArtistRec(Artist_id.get(), Artist_country.get(), Artist.get())
                disArtistdata()  # Display updated data after updating

        def addTrackdata():
                backend = Project_Backend()  # Creating an instance of Project_Backend
                backend.AddMusicRec(Track_ID.get(), Track_Name.get(), Artist.get(), Duration.get(), Album_id.get())
                disTrackdata() # Display updated data after updating

        # Frames
        MainFrame=Frame(self.root, bg="black")
        MainFrame.grid()

        TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
        TFrame.pack(side=TOP)

        self.TFrame=Label(TFrame, font=('Arial', 35, 'bold'), text="Musicify", bg="black", fg="Purple")
        self.TFrame.grid() 

        BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Track Info\n", fg="white")
        DFrameL.pack(side=LEFT)

        DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Details\n", fg="white")
        DFrameR.pack(side=RIGHT) 

        #Labels & Entry Box
        self.lblTrack_ID=Label(DFrameL, font=('Arial', 18, 'bold'), text="Track ID:", padx=2, pady=2, bg="black", fg="Purple")
        self.lblTrack_ID.grid(row=0, column=0, sticky=W)
        self.txtTrack_ID=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Track_ID, width=39, bg="black", fg="white")
        self.txtTrack_ID.grid(row=0, column=1) 

        self.lblTrack_Name=Label(DFrameL, font=('Arial', 18, 'bold'), text="Track Name:", padx=2, pady=2, bg="black", fg="Purple")
        self.lblTrack_Name.grid(row=1, column=0, sticky=W) 
        self.txtTrack_Name=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Track_Name, width=39, bg="black", fg="white")
        self.txtTrack_Name.grid(row=1, column=1)

        self.lblArtist=Label(DFrameL, font=('Arial', 18, 'bold'), text="Artist:", padx=2, pady=2, bg="black", fg="Purple")
        self.lblArtist.grid(row=3, column=0, sticky=W) 
        self.txtArtist=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Artist, width=39, bg="black", fg="white")
        self.txtArtist.grid(row=3, column=1)

        self.lblArtist_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="Artist id:", padx=2, pady=2, bg="black", fg="Purple")
        self.lblArtist_id.grid(row=4, column=0, sticky=W) 
        self.txtArtist_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Artist_id, width=39, bg="black", fg="white")
        self.txtArtist_id.grid(row=4, column=1)

        self.lblDuration=Label(DFrameL, font=('Arial', 18, 'bold'), text="Duration (Secs):", padx=2, pady=2, bg="black", fg="Purple")
        self.lblDuration.grid(row=5, column=0, sticky=W) 
        self.txtDuration=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Duration, width=39, bg="black", fg="white")
        self.txtDuration.grid(row=5, column=1)

        self.lblAlbum_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="Album id:", padx=2, pady=2, bg="black", fg="Purple")
        self.lblAlbum_id.grid(row=6, column=0,sticky=W) 
        self.txtAlbum_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Album_id, width=39, bg="black", fg="white")
        self.txtAlbum_id.grid(row=6, column=1)

        self.lblArtist_country=Label(DFrameL, font=('Arial', 18, 'bold'), text="Country:", padx=2, pady=2, bg="black", fg="Purple")
        self.lblArtist_country.grid(row=7, column=0,sticky=W) 
        self.txtArtist_country=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Artist_country, width=39, bg="black", fg="white")
        self.txtArtist_country.grid(row=7, column=1)

        self.lblRating=Label(DFrameL, font=('Arial', 18, 'bold'), text="Rating:", padx=2, pady=2, bg="black", fg="Purple")
        self.lblRating.grid(row=8, column=0,sticky=W) 
        self.txtRating=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Rating, width=39, bg="black", fg="white")
        self.txtRating.grid(row=8, column=1)

        #ListBox & ScrollBar
        sb=Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        MusicList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
        MusicList.bind('<<ListboxSelect>>', musicrec)
        MusicList.grid(row=0, column=0, padx=8)
        sb.config(command=MusicList.yview) 

        #Buttons
        self.btnadd=Button(BFrame, text="Add Track", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="Purple", command=addTrackdata)
        self.btnadd.grid(row=0, column=0)

        self.btnadd=Button(BFrame, text="Add Artist", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="Purple", command=addArtistdata)
        self.btnadd.grid(row=0, column=1)

        self.btndis=Button(BFrame, text="Play", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="Purple", command=disTrackdata)
        self.btndis.grid(row=0, column=2)

        self.btnclc=Button(BFrame, text="Stop", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="Purple", command=clcdata)
        self.btnclc.grid(row=0, column=3)

        self.btnse=Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="Purple", command=searchdb)
        self.btnse.grid(row=0, column=4)

        self.btnx=Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="Purple", command=iExit)
        self.btnx.grid(row=0, column=5)

if __name__ == '__main__':
    root = Tk()
    datbase = Music(root)
    root.mainloop()