from tkinter import * 
import tkinter.font as font
import sqlite3
from tkinter import messagebox 
import os
from functools import partial
import time
from tk_html_widgets import HTMLLabel
import markdown



class Data(): 

	#Changes the Font for the whole app
	def Font(): 
		return "Baskerville"

	#get list of users in database
	def UserList():
		conn = sqlite3.connect('Notes_Database.db')

		c = conn.cursor()
		c.execute("SELECT *,oid FROM users") 
		
		UserList = []
		records = c.fetchall() 
		for record in records: 
			
			UserList.append(record[0])
					
		conn.commit()
		conn.close()
		return UserList  

	#get list of Notes in database
	def NoteList():
		conn = sqlite3.connect('Notes_Database.db')

		c = conn.cursor()
		c.execute("SELECT *,oid FROM NOTES") 
		Notelist = []
		records = c.fetchall() 
		for record in records: 
			
			Notelist.append(record)
					
		conn.commit()
		conn.close()
		return Notelist  

	def GetRecords(): 
		conn = sqlite3.connect('Notes_Database.db')
		c = conn.cursor()
		c.execute("SELECT *,oid FROM users")  
		records = c.fetchall()  
		conn.commit()
		conn.close()
		return records

	#Shows Info For Debuging 
	def ShowInfo(): 
		print(f"USERINFO: {Data.GetRecords()}")
		print(f"USERLIST: {Data.UserList()}") 
		print(f"NOTELIST: {Data.NoteList()}")


	def ResetUsers(): 
		conn = sqlite3.connect('Notes_Database.db')
		c = conn.cursor()
		c.execute("DELETE FROM users")  
		records = c.fetchall()  
		conn.commit()
		conn.close()  
	#Resets all Notes Info in Database
	def ResetNotes(): 
		conn = sqlite3.connect('Notes_Database.db')
		c = conn.cursor()
		c.execute("DELETE FROM NOTES")  
		records = c.fetchall()  
		conn.commit()
		conn.close()  

	#Adds New user when Signing up
	def AddUser(Name, PasswordValue): 

		conn = sqlite3.connect('Notes_Database.db')

		c = conn.cursor()

		c.execute("INSERT INTO users VALUES (:Username, :Password)",  

			{ 

			'Username': Name, 
			'Password': PasswordValue

				}
					
		)  
		conn.commit()
		conn.close   
	#Add new note when creating note
	def AddNote(Name, Title): 	
			conn = sqlite3.connect('Notes_Database.db')

			c = conn.cursor()

			c.execute("INSERT INTO NOTES VALUES (:Username, :Title, :TextValue)",  

				{ 

				'Username': Name, 
				'Title':  Title,
				'TextValue': ""
					}
						
			)  
			conn.commit()
			conn.close   

	#Deletes Notes From Database
	def DeleteNote(Name,Title):  
		conn = sqlite3.connect('Notes_Database.db')

		c = conn.cursor()

		c.execute("DELETE FROM NOTES WHERE Username = :Username AND Title = :Title",  

			{ 

				'Username': Name, 
				'Title':  Title
			}
						
				)  
		conn.commit()
		conn.close   

	
	#Views Note from Database
	def ViewNote(Name, NoteTitle): 
		root = Tk() 
		root.title(f"{NoteTitle}") 
		root.geometry("1600x1000") 
		
		myFont = font.Font(family=f"{Data.Font()}" , size = 75)
		myFont2 = font.Font(family=f"{Data.Font()}" , size = 45)
		myFont3 = font.Font(family=f"{Data.Font()}" , size = 20)
		TitleLabel = Label(root, text=f"{NoteTitle}", font=myFont, pady=15, padx=15)
		TitleLabel.pack()
		myframe1 = LabelFrame(root) 
		myframe1.pack()

		def Save(Name,NoteTitle): 
			TextValue = EditBox.get("1.0", 'end')

			conn = sqlite3.connect('Notes_Database.db')

			c = conn.cursor()

			c.execute("UPDATE NOTES SET NoteData = :TextValue WHERE Username = :Username AND Title = :Title",  

			{ 

			'Username': Name, 
			'Title':  NoteTitle,
			'TextValue': TextValue
				}
			)  

			conn.commit()

			root.destroy()
			Data.ViewNote(Name, NoteTitle)

		def Back(Name): 
			root.destroy()
			Pages.MyNotes(Name) 
		SaveButton = Button(myframe1, text="Save", font=myFont2, command= lambda: Save(Name, NoteTitle))
		SaveButton.grid(row=0, column=1) 
		def DeleteButtonFunc(Name, NoteTitle): 
			response = messagebox.askyesno("Delete Note", "Are You Sure You want to Delete?")
			if response == True: 
				root.destroy()
				Data.DeleteNote(Name,NoteTitle) 
				Pages.Home(Name)
		DeleteButton = Button(myframe1, text="Delete", font=myFont2, command= lambda: DeleteButtonFunc(Name, NoteTitle))
		DeleteButton.grid(row=0,column=3)
		def Share(): 
			NoteID = []
			for note in Data.NoteList(): 
				if note[1] == NoteTitle: 
					NoteID.append(note[3]) 

			NoteValue = NoteID[0] * 187 * 72 
			
			os.system(f"touch file.md")
			with open(f"file.md", "r+") as file:
				file.write(f"{EditBox.get('1.0', 'end')}") 
			os.system("open file.md") 
			time.sleep(5)
			os.system("rm file.md")
		
		ShareButton = Button(myframe1, text="Share", font=myFont2, command=Share)
		ShareButton.grid(row=0, column=4)
		BackButton = Button(myframe1, text="Back", font=myFont2, command= lambda: Back(Name))
		BackButton.grid(row=0, column=5)   
		MainFrame = LabelFrame(root, width=1000, height=300, bd=6)
		MainFrame.pack()
		EditBoxFrame = LabelFrame(MainFrame, width=500, height=300, bd=6)
		EditBoxFrame.grid(row=0, column=0)
		EditBox = Text(EditBoxFrame, width=65, height=28)
		EditBox.pack()
		EditBox.configure(font=myFont3)  
		ShowBoxFrame = LabelFrame(MainFrame, width=500, height=300, bd=6)
		ShowBoxFrame.grid(row=0,column=1) 

		

		UserNoteList = []
		NoteList = Data.NoteList()
		for Note in NoteList: 
			if Note[0] == Name: 
				UserNoteList.append(Note) 

		MainNote = ""
		for Note in UserNoteList: 	
			if Note[1] == NoteTitle: 
				MainNote = Note[2] 
		
		EditBox.insert(END, f"{MainNote}")	


		html = markdown.markdown(MainNote).replace("<p>", "<p style='font-size:20px;'>")
		html2 = html.replace("<h1>", "<h1 style='font-size: 60px'>")
		html3 = html2.replace("<h2>", "<h2 style='font-size: 40px'>")
		html4 = html3.replace("<h3>", "<h3 style='font-size: 30px'>")
		html5 = html4.replace("<ol>", "<ol style='font-size:20px;'>")
		html6 = html5.replace("<ul>", "<ul style='font-size:20px;'>")

		ShowBox = HTMLLabel(ShowBoxFrame, html=html6, width=100, height=50)
		ShowBox.pack()	


		mainloop()




	def EditPassword(Name, NewPassword): 

			conn = sqlite3.connect('Notes_Database.db')

			c = conn.cursor()

			c.execute("UPDATE Users SET Password = :Password WHERE Username = :Username",  

			{ 

			'Username': Name, 
			'Password':  NewPassword,
				}
			)  

			conn.commit()
			conn.close  

			messagebox.showinfo("Password", "Your Password has been succesfully changed") 

	def RemoveAccount(Name): 

			conn = sqlite3.connect('Notes_Database.db')

			c = conn.cursor()

			c.execute("DELETE FROM Users WHERE Username = :Username",  

			{ 

			'Username': Name
				} 
			)   


			c.execute("DELETE FROM Notes WHERE Username = :Username",  

			{ 

			'Username': Name
				} 
			)   
 
			conn.commit()
			conn.close  

			messagebox.showinfo("Account Deleted", "Your Account has been Deleted") 




class Pages(): 


	#Sign Up Page
	def signUp(): 
		root = Tk() 
		root .title("Sign Up") 
		root .geometry("1600x1000") 

		def submit(Name):   

			if Password.get() == Confirm.get(): 
				if Username.get() == "": 
					messagebox.showerror("Username Error","Please Enter a Valid Username")
				else:  

					Userlist = Data.UserList()

					if Username.get() in Userlist: 
						messagebox.showerror("Username Error","User Allready Exists")
					
					else:  
						Data.AddUser(f"{Username.get()}", f"{Password.get()}")
						root.destroy()
						Pages.Home(Name)
			else: 
				messagebox.showerror("Passowrd Error","The Passwords do not Match")


		myFont = font.Font(family=f"{Data.Font()}" , size = 75)
		myFont2 = font.Font(family=f"{Data.Font()}" , size = 15)
		MainFrame= LabelFrame(root, bd=0, pady=90)
		MainFrame.pack()
		title_label = Label(MainFrame, text="Sign Up",  font=myFont, padx=400, pady=45)
		title_label.pack()
		frame = LabelFrame(MainFrame, bd=0) 
		frame.pack()

		Username = Entry(frame, width=30)
		Username.grid(row=0, column=1, padx=20)
		Password = Entry(frame, width=30, show="*")
		Password.grid(row=1, column=1)
		Confirm = Entry(frame, width=30, show="*")
		Confirm.grid(row=2, column=1)
		def SubmitBind(event): 
			submit(Username.get())

		Confirm.bind('<Return>', SubmitBind)
		Username_label = Label(frame, text="Username:", font=myFont2) 
		Username_label.grid(row=0, column=0) 
		Password_label = Label(frame, text="Password:", font=myFont2) 
		Password_label.grid(row=1, column=0) 
		Confirm_label = Label(frame, text="Confirm Password:", font=myFont2) 
		Confirm_label.grid(row=2, column=0)  


		def back(): 
			root.destroy()
			Main.Start()
		signUpButton = Button(frame, text="Sign Up", command=lambda: submit(Username.get()))  
		signUpButton.grid(row=3, column=0, columnspan=2)  
		BackButton = Button(frame, text="Back", command=back) 
		BackButton.grid(row=3,column=1, padx=10)
			
		mainloop()


	#Login Page
	def LogIn(): 
		LoginPage = Tk() 
		LoginPage .title("Log In") 
		LoginPage .geometry("1600x1000") 

		#check if password matches password for user in database
		def  VarifyUser(Name, Password):   
			conn = sqlite3.connect('Notes_Database.db')

			c = conn.cursor()
			NameValue = str(Name)
			c.execute("SELECT * FROM users") 
			
			AllInfo = c.fetchall() 
			Userlist = Data.UserList()
			PasswordList = []
			for info in AllInfo: 
				PasswordList.append(info[1])


			if Name in Userlist: 	
				LocationValue = Userlist.index(f'{Name}')
				if PasswordList[LocationValue] == Password: 
						LoginPage.destroy()
						Pages.Home(Name)

				else: 
					messagebox.showerror("Password Error","Password is Incorrect")
						
			else:  

				if Name == 'Admin' and Password == '123':  	
					root = Tk()
					root.title("Debug Window") 

					showUsers = Button(root, text="Show Info", command=Data.ShowInfo)
					showUsers.pack() 

					DeleteUsers = Button(root, text="Reset Users", command=Data.ResetUsers)
					DeleteUsers.pack()  

					ResetNotes = Button(root, text="Reset Notes", command=Data.ResetNotes)
					ResetNotes.pack() 

					def Clear(): 
						os.system("clear") 	

					ClearButton = Button(root, text="Clear", command=Clear)
					ClearButton.pack()

					root.mainloop()

				else: 
					messagebox.showerror("Username Error","User Does Not Exist") 

			conn.commit()
			conn.close  

		myFont = font.Font(family=f"{Data.Font()}" , size = 75)
		myFont2 = font.Font(family=f"{Data.Font()}" , size = 17)
		MainFrame = LabelFrame(LoginPage, bd=0, pady=90)
		MainFrame.pack()
		title_label = Label(MainFrame, text="Log In",  font=myFont, padx=400, pady=45)
		title_label.pack()
		frame = LabelFrame(MainFrame) 
		frame.pack()
		frame.configure(bd=0)

		Username = Entry(frame, width=30)
		Username.grid(row=0, column=1, padx=20)
		def LoginEvent(event): 
			VarifyUser(Username.get(), Password.get())
		Password = Entry(frame, width=30, show="*")
		Password.grid(row=1, column=1)
		Password.bind('<Return>', LoginEvent)
		

		Username_label = Label(frame, text="Username:", font=myFont2) 
		Username_label.grid(row=0, column=0) 
		Password_label = Label(frame, text="Password:", font=myFont2) 
		Password_label.grid(row=1, column=0) 
		

		def back(): 
			LoginPage.destroy()
			Main.Start()
		LogInButton = Button(frame, text="Log In", command=lambda: VarifyUser(Username.get(), Password.get()))  
		LogInButton.grid(row=2, column=0,columnspan=2)  
		
		BackButton = Button(frame, text="Back", command=back) 
		BackButton.grid(row=2,column=1)
			
		mainloop()


	#HomePage
	def Home(Name): 
		root = Tk() 
		root .title("Home") 
		root .geometry("1600x1000") 

		myFont = font.Font(family=f"{Data.Font()}" , size = 75)
		myFont2 = font.Font(family=f"{Data.Font()}" , size = 45)
		myFont3 = font.Font(family=f"{Data.Font()}" , size = 15)
		Main_Frame = LabelFrame(root, bd=0, pady=50)
		Main_Frame.pack()
		title_label = Label(Main_Frame, text=f"Welcome {Name}",  font=myFont, padx=400, pady=0)
		title_label.pack()
	
		ButtonFrame = LabelFrame(root, bd=0) 
		ButtonFrame.pack()


		frame1 = LabelFrame(ButtonFrame)
		frame1.pack() 
		frame2 = Label(ButtonFrame, padx = 100 )
		frame2.pack()
		frame3 = LabelFrame(ButtonFrame)
		frame3.pack()  
		frame4 = Label(ButtonFrame, padx = 100 )
		frame4.pack()
		frame5 = LabelFrame(ButtonFrame)
		frame5.pack()  
		frame6 = Label(ButtonFrame, padx = 100 )
		frame6.pack()
		frame7 = LabelFrame(ButtonFrame)
		frame7.pack()  


		def LogOut(): 
			with open("StayLoggedIn.txt", "w+") as File: 
				File.write("Off")	
			root.destroy()
			Main.Start()
	
		def CreateNoteFunc(Name): 
			root.destroy()
			Pages.CreateNote(Name)
		
		def MyNotesFunc(Name): 
			root.destroy()
			Pages.MyNotes(Name) 
		def MyAccountFunc(Name): 
			root.destroy()
			Pages.MyAccount(Name) 

		Button(frame1, text="My Notes", font=myFont2, command = lambda: MyNotesFunc(Name)).pack() 
		Button(frame3, text="Create Note", font=myFont2, command=lambda: CreateNoteFunc(Name)).pack()
		Button(frame5, text="Settings", font=myFont2, command=lambda: MyAccountFunc(Name)).pack()
		Button(frame7, text="Log Out", font=myFont2, command=LogOut).pack()


		
		root.mainloop()   

	#Account Settings Page	
	def MyAccount(Name): 
		root = Tk() 
		root .title("My Account") 
		root .geometry("1600x1000") 

		myFont = font.Font(family=f"{Data.Font()}" , size = 100)
		myFont2 = font.Font(family=f"{Data.Font()}" , size = 45)
		myFont3 = font.Font(family=f"{Data.Font()}" , size = 20)
		myFont4 = font.Font(family=f"{Data.Font()}" , size = 30)

		Main_Frame = LabelFrame(root, bd=0, pady=130)
		Main_Frame.pack()
		title_label = Label(Main_Frame, text="My Account",  font=myFont, padx=400, pady=0)
		title_label.pack()   
		Frame2 = LabelFrame(Main_Frame, bd=0, pady=30)
		Frame2.pack() 
		def Back():
			root.destroy()
			Pages.Home(Name)
		BackButton = Button(Frame2, text="Back", font=myFont2, command=Back)  
		BackButton.pack()
		SpaceFrame = LabelFrame(Frame2, height=30,bd=0, padx=100)
		SpaceFrame.pack() 
		def ChangePasswordFunc(): 
			root.destroy()
			Pages.ChangePassword(Name)
		ChangePasswordButton = Button(Frame2, text="Change Passcode", font=myFont2, command= ChangePasswordFunc)
		ChangePasswordButton.pack() 
		SpaceFrame2 = LabelFrame(Frame2, height=30,bd=0, padx=100)
		SpaceFrame2.pack() 
		StayLoggedInFrame = LabelFrame(Frame2, bd=0)
		StayLoggedInFrame.pack()
		StayLoggedInLabel = Label(StayLoggedInFrame, text="Stay Logged In?", font=myFont4) 
		StayLoggedInLabel.grid(row=0, column=0) 
		def TurnOn(): 
			with open("StayLoggedIn.txt", "w+") as File: 
				File.write(Name)		
			root.destroy() 
			Pages.MyAccount(Name)

		def TurnOff(): 
			with open("StayLoggedIn.txt", "w+") as File: 
				File.write("Off")		
			root.destroy() 
			Pages.MyAccount(Name)

		with open("StayLoggedIn.txt", "r+") as File: 
			FileVariable = File.readline()
		if FileVariable == "Off": 
			Button(StayLoggedInFrame, text= "Turn On", command=TurnOn, font=myFont3).grid(row=0, column=1)
		else: 
			Button(StayLoggedInFrame, text= "Turn Off", command=TurnOff, font=myFont3).grid(row=0, column=1) 
		SpaceFrame3 = LabelFrame(Frame2, height=30,bd=0, padx=100)
		SpaceFrame3.pack() 
		def DeleteAccount(): 
			Question = messagebox.askyesno("Confirm", "Are you sure you want to delete you account? All your notes will be deleted.")
			if Question == True:  
				Data.RemoveAccount(Name)
				root.destroy()
				Main.Start() 
				with open("StayLoggedIn.txt", "r+") as File: 
					File.write("Off")

		DeleteAccountButton = Button(Frame2, text="Delete Account", font=myFont2, command=DeleteAccount) 
		DeleteAccountButton.pack() 
		root.mainloop()  


	#ChangePasscode Page
	def ChangePassword(Name): 
		root = Tk() 
		root .title("My Account") 
		root .geometry("1600x1000") 
		myFont = font.Font(family=f"{Data.Font()}" , size = 75)
		myFont2 = font.Font(family=f"{Data.Font()}" , size = 17) 
		myFont3 = font.Font(family=f"{Data.Font()}" , size = 17) 

		MainFrame = LabelFrame(root, bd=0, pady=90)
		MainFrame.pack()
		title_label = Label(MainFrame, text="Change Password",  font=myFont, padx=400, pady=45)
		title_label.pack()
		Frame = LabelFrame(MainFrame) 
		Frame.pack()
		Frame.configure(bd=0)

		Old = Entry(Frame, width=30, show="*")
		Old.grid(row=0, column=1, padx=20)
		New = Entry(Frame, width=30, show="*")
		New.grid(row=1, column=1)
		
		Old_Label = Label(Frame, text="Old Password:", font=myFont3) 
		Old_Label.grid(row=0, column=0) 
		New_Label = Label(Frame, text="New Password:", font=myFont3) 
		New_Label.grid(row=1, column=0) 
		def Submit(): 
			UserInfo = []
			for User in Data.GetRecords():
				if User[0] == Name: 
					UserInfo.append(User[1])
			DBPassword = UserInfo[0]
			if Old.get() == DBPassword: 
				Data.EditPassword(Name, New.get())
			else:  
				messagebox.showerror("Password Error", "Old Password is Incorrect")

		SubmitButton = Button(Frame, text="Submit", font=myFont3, command=Submit)
		SubmitButton.grid(row=2, column=0, columnspan=2)
		def Back():
			root.destroy()
			Pages.MyAccount(Name)
		CancleButton = Button(Frame, text="Cancel", font=myFont3, command=Back)
		CancleButton.grid(row=2, column=1)


		root.mainloop() 

	# Create Note Page
	def CreateNote(Name): 
		root = Tk() 
		root .title("Create Note") 
		root .geometry("1600x1000") 

		myFont = font.Font(family=f"{Data.Font()}" , size = 75) 
		myFont2 = font.Font(family=f"{Data.Font()}" , size = 15) 
		MainFrame = LabelFrame(root, bd=0, pady=90)
		MainFrame.pack()
		Title_label = Label(MainFrame, text="Create Note",  font=myFont, padx=400, pady=45)
		Title_label.pack()
		frame = LabelFrame(root, bd=0) 
		frame.pack() 

		EntryFrame = LabelFrame(MainFrame, bd=0)
		EntryFrame.pack()
		AskTitle = Entry(EntryFrame, width=30)
		AskTitle.grid(row=0, column=1, padx=20)
		AskTitle_label = Label(EntryFrame, text="Title:", font=myFont2) 
		AskTitle_label.grid(row=0, column=0) 
		
		def AddNoteFunc(Name, Title): 
			root.destroy()
			Data.AddNote(Name, Title) 
			Pages.MyNotes(Name)
		def Cancel(Name): 
			root.destroy()
			Pages.Home(Name) 

		ButtonFrame = LabelFrame(MainFrame, bd=0)
		ButtonFrame.pack()
		CancleButton = Button(ButtonFrame, text="Cancel", command= lambda: Cancel(Name))
		CancleButton.grid(row=3, column=0)
		MakeNoteButton = Button(ButtonFrame, text="Create", command=lambda: AddNoteFunc(Name, AskTitle.get())) 
		MakeNoteButton.grid(row=3, column=2)

		mainloop() 


	# My Notes Page
	def MyNotes(Name): 
		root = Tk() 
		root .title("Home") 
		root .geometry("1600x1000") 
		myFont = font.Font(family=f"{Data.Font()}" , size = 75)
		myFont2 = font.Font(family=f"{Data.Font()}" , size = 45) 
		myFont3 = font.Font(family=f"{Data.Font()}", size= 25)
		myFont4 = font.Font(family=f"{Data.Font()}", size= 15)
		BackFrame = LabelFrame(root).pack(pady=5)
		def Back(Name): 
			root.destroy() 
			Pages.Home(Name)
		BackButton = Button(BackFrame, text="back", font=myFont4, command= lambda: Back(Name))
		BackButton.pack()
		title_label = Label(root, text=f"{Name}'s Notes",  font=myFont, padx=400, pady=45)
		title_label.pack()
		
		UserNoteList = []
		NoteList = Data.NoteList()
		for Note in NoteList: 
			if Note[0] == Name: 
				UserNoteList.append(Note) 

		def ViewNoteFunc(Name, Title):
			root.destroy()
			Data.ViewNote(Name, Title)

		for Note in UserNoteList: 
			NoteTitle = Note[1]
			CommandWithArgs = partial(ViewNoteFunc, Name, NoteTitle)
			Button(root,text=f"{NoteTitle}", font=myFont2, command=CommandWithArgs).pack()
		root.mainloop() 



class Main():  

	def Start(): 
		root1 = Tk() 
		root1.title("Simple Note Taker") 
		root1.geometry("1600x1000") 

		myFont = font.Font(family=f"{Data.Font()}" , size = 75)
		myFont2 = font.Font(family=f"{Data.Font()}" , size = 20)
		title_label = Label(root1, text="Simple Note Taker",  font=myFont, padx=400, pady=130)
		title_label.pack()
		frame = LabelFrame(root1) 
		frame.pack()
		frame.configure(bd=0) 
		

		def signUpFunc(): 
			root1.destroy() 
			Pages.signUp()
		signUpButton = Button(frame, text="Sign Up", width=15, height=3, font=myFont2, command=signUpFunc) 
		signUpButton.grid(row=0, column = 0) 
		spaceLabel = Label(frame, width= 15, height=3)
		spaceLabel.grid(row=0, column=1) 
		def LogInFunc(): 
			root1.destroy()
			Pages.LogIn()
		LoginButton = Button(frame, text="Login" , width=15, height=3, font=myFont2,command=LogInFunc)
		LoginButton.grid(row=0, column = 2, ) 

		root1.mainloop() 


with open("StayLoggedIn.txt",  "r+") as File: 
	FileVariable = File.readline()

if FileVariable == "Off": 
	Main.Start() 
else: 
	Pages.Home(FileVariable)


