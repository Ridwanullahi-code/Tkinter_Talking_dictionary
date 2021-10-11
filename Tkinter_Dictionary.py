#<=========== import all modules here ==============>
from tkinter import*  #<===== tkinter module =========> 
from tkinter import ttk #<===== import tkinter.ttk module ======>
from PIL import ImageTk,Image #<===== import PIL module for image =======>
import pyttsx3 #<====== import pyttsx3 module to convert text to speech =====>
from  random_words import RandomWords  #<======= import random_words module to get random words ======>
from PyDictionary import PyDictionary #<======= from PyDictionary module import Pydictionary function ==>
from nltk.corpus import wordnet #< module to get synonyms and antomyms of words =========>

#<======== function to get random words ===========>
def generate_word():
	global word
	rw = RandomWords()
	word = rw.random_word().capitalize()
#<===== function to find meaning of random word ==========>
def find_word_meaning():
	global result1,e2,e3
	e2 = combo2.get()
	e3 = search_entry.get()

	if e2 == "SEARCH":
		dictionary = PyDictionary()
		meaning = dictionary.meaning(e3)
		for n,v in meaning.items():
			re = str(v)[2:-1]
			revove_qoute = re.replace("'","")
			result1 = f'{n}: {revove_qoute}'
	else:
		dictionary = PyDictionary()
		meaning = dictionary.meaning(word)
		for n,v in meaning.items():
			re = str(v)[2:-1]
			revove_qoute = re.replace("'","")
			result1 = f'{n}: {revove_qoute}'
#<======== function to get antonyms of word ==========>
def antonym_find():
	global result2
	antonyms = []

	if e2 == "SEARCH":	
		for syn in wordnet.synsets(e3):
		    for lm in syn.lemmas():
		        if lm.antonyms():
		            antonyms.append(lm.antonyms()[0].name())

		remove_quote = (str(list(set(antonyms)))[1:-1]).replace("'","")
		result2 = f'Antonyms: {remove_quote}'

	else:
		for syn in wordnet.synsets(word):
		    for lm in syn.lemmas():
		        if lm.antonyms():
		            antonyms.append(lm.antonyms()[0].name())

		remove_quote = (str(list(set(antonyms)))[1:-1]).replace("'","")
		result2 = f'Antonyms: {remove_quote}'
#<====== function to get synonyms of word ===========>
def synonym_find():
	global result3
	synonyms = []

	if e2 == "SEARCH":
		for syn in wordnet.synsets(e3):
		    for lm in syn.lemmas():
		             synonyms.append(lm.name())
		
		remove_quote2 = (str(list(set(synonyms)))[1:-1]).replace("'","")
		result3 = f'Synonyms: {remove_quote2}'

	else:
		for syn in wordnet.synsets(word):
		    for lm in syn.lemmas():
		             synonyms.append(lm.name())
		
		remove_quote2 = (str(set(list(synonyms)))[1:-1]).replace("'","")
		result3 = f'Synonyms: {remove_quote2}'


def Display_text():
	if e2 == "SEARCH":
		join = f'Word: {e3.capitalize()}\n{result1}\n{result2}\n{result3}'
		text2.insert(END,join)

	else:
		join = f'Word: {word}\n{result1}\n{result2}\n{result3}'
		text2.insert(END,join)
#<========= function to next get next word ======>
def next_button():
	generate_word()
	find_word_meaning()
	antonym_find()
	synonym_find()
	print(Display_text())

def Convert_button():
	rate_val = rate_slider.get()
	engine = pyttsx3.init()
	e1 = text2.get(1.0,END)
	voices = engine.getProperty("voices")
	rate = engine.getProperty('rate')
	combo_val = combo.get()
	engine.setProperty('rate',rate_val)

	if combo_val == "MALE":
		engine.setProperty("voice",voices[0].id)
		engine.say(e1)
		engine.runAndWait()

	else:
		engine.setProperty("voice", voices[1].id)
		engine.say(e1)
		engine.runAndWait()
#<========= function to clear everything ==========>
def clear_button():
	text2.delete(1.0,END)
#<====== function to hold all function defined ========>
def Dictionary_Speech():
	Display_root()
	Display_title()
	Display_dic()
	Display_audio()
	Display_button()
	root.mainloop()
#<=========== function to diaplay root ========>
def Display_root():
	global root,arrow_logo,speaker_logo
	root = Tk()
	root.geometry("835x468+335+172")
	root.title("Music App")
	root.resizable(width=NO,height=NO)
	root.config(bg="#F7F7F7")
	arrow_logo = ImageTk.PhotoImage(Image.open("arrow.png"))
	speaker_logo = ImageTk.PhotoImage(Image.open("speaker.png"))
	
#<======= function to display project title ==========>
def Display_title():
	title = Label(root,text="TALKING DICTIONARY",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	title.place(x=0,y=0,width=835)
#<========= function to diaplay all widget =======>
def Display_dic():
	global combo,text2,combo2,search_entry
	arrow = Label(root,image=arrow_logo)
	arrow.place(x=400,y=170)
	label = Label(root,text="DICTIONARY",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	label.place(x=70,y=70,width=230)
	text_frame = Frame(root,bg="white")
	text_frame.place(x=20,y=132,width=340,height=200)
	scrollbar = Scrollbar(text_frame,orient=VERTICAL)
	scrollbar.pack(side=RIGHT,fill="y")
	text2 = Text(text_frame,bg="white",font=("Arial",11,"bold"),yscrollcommand=scrollbar.set)
	text2.pack(side=LEFT)

	scrollbar.configure(command=text2.yview)
	choice = Label(root,text="CHOICE:",bg="#F7F7F7",font=("times new roman",12,"bold"))
	choice.place(x=1,y=340)
	combo2 = ttk.Combobox(root,font=("Roboto",11,"bold"),values=("SEARCH","RANDOM"))
	combo2.set("RANDOM")
	combo2.place(x=78,y=340,width=96)

	search_lb = Label(root,text="SEARCH:",bg="#F7F7F7",font=("times new roman",12,"bold"))
	search_lb.place(x=180,y=340)
	search_entry = Entry(root,bg="white",bd=4,font=("Roboto",12,"bold"),relief=GROOVE)
	search_entry.place(x=255,y=337,width=107,height=30)

	next = Button(root,text="NEXT",fg="white",bg='#000080',font=("Roboto",15,"bold"),command=next_button)
	next.place(x=90,y=410,width=170)
#<=========== function to display second widget ===========>
def Display_audio():
	global combo,rate_slider
	label = Label(root,text="AUDIO",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	label.place(x=600,y=70,width=230)
	speaker = Label(root,image = speaker_logo)
	speaker.place(x=670,y=130)
	sec_lb = Label(root,text="CHANGE VOICE:",bg="#F7F7F7",font=("times new roman",12,"bold"))
	sec_lb.place(x=600,y=300)
	combo = ttk.Combobox(root,font=("Roboto",11,"bold"),values=("MALE","FEMALE"))
	combo.set("MALE")
	combo.place(x=740,y=300,width=80)
	rate_lab = Label(root,text="CHANGE RATE: ",bg="#F7F7F7",font=("times new roman",12,"bold"))
	rate_lab.place(x=560,y=348)
	rate_slider = Scale(root,from_ =100, to=200, resolution=10,length=100,sliderlength=20,orient=HORIZONTAL)
	rate_slider.place(x=700,y=330)
#<==========function to display all buttons widget ================>	
def Display_button():
	convt = Button(root,text="CONVERT",fg="white",bg='#B200ED',font=("Roboto",15,"bold"),command=Convert_button)
	convt.place(x=400,y=280,width=160)
	clear = Button(root,text="CLEAR",fg="white",bg='red',font=("Roboto",15,"bold"),command=clear_button)
	clear.place(x=420,y=410,width=170)
print(Dictionary_Speech())