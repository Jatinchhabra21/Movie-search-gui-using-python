from tkinter import *
from tkinter.ttk import *
from api import get_movie,get_poster
from tkinter import messagebox as mb
from PIL import ImageTk,Image
from io import BytesIO
import textwrap

class Application(Frame):

    def __init__(self,master=None):

        super().__init__(master)
        self.master=master
        self.master.title('Search')
        self.master.iconbitmap('search.ico')
        self.master.geometry('400x90+500+250')
        self.master.maxsize(width=400,height=90)
        self.createWidgets()

    def prettyData(self):
        plot = self.data['Plot']
        plot = textwrap.wrap(plot,width=52,break_on_hyphens=False)
        self.data['Plot'] = '\n'.join(plot)

    def create_new_window(self):
        self.new = Tk()
        self.new.withdraw()

    def displayData(self):

        if self.data['Title'] == '':
            mb.showinfo('No Info', "Please check the title you entered, seems like info for {} is not available!".format(self.data['title']))
        
        self.new.deiconify()
        self.showTitle_Label = Label(self.new,text='Title')
        self.showRelease_Label = Label(self.new,text='Release Date')
        self.showGenre_Label = Label(self.new,text='Genre')
        self.showRating_Label = Label(self.new,text='Rated')
        self.showDirector_Label = Label(self.new,text='Director')
        self.showActors_Label = Label(self.new,text='Actors')
        self.showimdb_Label = Label(self.new, text='IMDB Rating')

        self.showTitle_Text = Text(self.new,width=35,height=1)
        self.showRelease_Text = Text(self.new,width=35,height=1)
        self.showGenre_Text = Text(self.new,width=35,height=1)
        self.showRating_Text = Text(self.new,width=35,height=1)
        self.showDirector_Text = Text(self.new,width=35,height=1)
        self.showActors_Text = Text(self.new,width=35,height=1)
        self.showimdb_Text = Text(self.new,width=35,height=1)
        self.plotText = Text(self.new,width=50,height=10)

        self.showTitle_Label.grid(row=1,column=0,sticky='W',padx=15,pady=10,ipadx=10)
        self.showRelease_Label.grid(row=2,column=0,sticky='W',padx=15,pady=(0,10),ipadx=10)
        self.showGenre_Label.grid(row=3,column=0,sticky='W',padx=15,pady=(0,10),ipadx=10)
        self.showRating_Label.grid(row=4,column=0,sticky='W',padx=15,pady=(0,10),ipadx=10)
        self.showDirector_Label.grid(row=5,column=0,sticky='W',padx=15,pady=(0,10),ipadx=10)
        self.showActors_Label.grid(row=6,column=0,sticky='W',padx=15,pady=(0,10),ipadx=10)
        self.showimdb_Label.grid(row=7,column=0,sticky='W',padx=15,pady=(0,10),ipadx=10)

        self.showTitle_Text.grid(row=1,column=1,sticky='W',pady=10,padx=10,ipadx=10)
        self.showRelease_Text.grid(row=2,column=1,sticky='W',pady=(0,10),padx=10,ipadx=10)
        self.showGenre_Text.grid(row=3,column=1,sticky='W',pady=(0,10),padx=10,ipadx=10)
        self.showRating_Text.grid(row=4,column=1,sticky='W',pady=(0,10),padx=10,ipadx=10)
        self.showDirector_Text.grid(row=5,column=1,sticky='W',pady=(0,10),padx=10,ipadx=10)
        self.showActors_Text.grid(row=6,column=1,sticky='W',pady=(0,10),padx=10,ipadx=10)
        self.showimdb_Text.grid(row=7,column=1,sticky='W',pady=(0,10),padx=10,ipadx=10)
        self.plotText.grid(row=8,column=0,sticky='W',pady=(0,10),padx=15,ipadx=10,columnspan=2)


        self.showTitle_Text.insert(INSERT,self.data['Title'])
        self.showRelease_Text.insert(INSERT,self.data['Released'])
        self.showGenre_Text.insert(INSERT,self.data['Genre'])
        self.showRating_Text.insert(INSERT,self.data['Rated'])
        self.showDirector_Text.insert(INSERT,self.data['Director'])
        self.showActors_Text.insert(INSERT,self.data['Actors'])
        self.showimdb_Text.insert(INSERT,self.data['imdbRating'])
        self.plotText.insert(INSERT,self.data['Plot'])

        self.canvas = Canvas(self.new,height=441,width=300)

        self.img = ImageTk.PhotoImage(master=self.canvas,image=Image.open(BytesIO(self.r.content)))

        self.canvas.grid(row=9,column=0,pady=10,columnspan=3)
        self.canvas.create_image(0,0,anchor=NW,image=self.img)
        self.canvas.image = self.img
        self.new.mainloop()

    def getData(self):
        try:
            self.data = get_movie(self.search.get(),self.type.get())
            self.new.title(self.data['Title'])
            self.new.iconbitmap('search.ico')
        except TclError:
            self.create_new_window()
            self.data = get_movie(self.search.get(),self.type.get())
            self.new.title(self.data['Title'])
            self.new.iconbitmap('search.ico')
        except AttributeError:
            self.create_new_window()
            self.data = get_movie(self.search.get(),self.type.get())
            self.new.title(self.data['Title'])
            self.new.iconbitmap('search.ico')
        self.prettyData()
        self.getPoster()
        self.displayData()

    def getPoster(self):
        try:
            self.r = get_poster(self.data['Poster'])
        except KeyError:
            mb.showerror(title='Error',message='Empty Searchbox')

    def call_getData(self,event):
        self.getData()

    def createWidgets(self):

        self.search = StringVar()
        self.searchEntry = Entry(self.master,textvariable=self.search,width=30)
        self.searchEntry.grid(row=0,column=0,padx=15,pady=10,ipadx=10,sticky='W')

        self.searchButton = Button(self.master,text='Search',command=self.getData)
        self.searchButton.grid(row=0,column=1,pady=10,padx=5,ipadx=10,columnspan=2,sticky='W')

        self.type = StringVar()

        self.movieRadio = Radiobutton(self.master,variable=self.type,value='Movie',text='Movie')
        self.seriesRadio = Radiobutton(self.master,variable=self.type,value='Series',text='Series')

        self.movieRadio.grid(row=1,column=0,pady=(0,10),padx=15,sticky='W')
        self.seriesRadio.grid(row=1,column=0,pady=(0,10),padx=15,sticky='E')

        self.searchEntry.bind('<Return>',self.call_getData)
        self.searchButton.bind('<Return>',self.call_getData)

root = Tk()
app = Application(root)
app.mainloop()