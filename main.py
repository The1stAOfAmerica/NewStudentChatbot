from tkinter import *

# GUI
root = Tk()
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("New Student Chatbot")
halfwidth = root.winfo_screenwidth()/2
root.configure(bg='#E5E5E5')


BG_YELLOW = "#FCA311"
BG_COLOR = "#E5E5E5"
TEXT_COLOR = "#14213D"

FONT = "Arial"
FONT_BOLD = "Helvetica 13 bold"


# Send function
def send():
    send = "You:  " + e.get()
    txt.insert(END, "\n \n" + send)

    user = e.get().lower()
    
    if user == "1":
        txt.insert(END, "\n \n" + "Bot: Amador Valley High School is a comprehensive public high school in Pleasanton, California. It is one of three high schools in the Pleasanton Unified School District, along with Foothill High School and Village High School. Founded as Amador Valley Joint Union High School (AVJUHS), it graduated its first class in 1923. Major construction and renovations were undertaken after district voters approved bonds in 1922, 1965, 1997, and 2016. The school is a four-time California Distinguished School and a three-time National Blue Ribbon School. In national competitions such as We the People: The Citizen and the Constitution, the Amador Valley team has won the 1995 and 2022 national titles. The Amador Valley Wind Ensembles have performed at national venues and conferences, including Carnegie Hall and the Midwest Clinic. Several Amador Valley athletic teams have won multiple California Interscholastic Federation North Coast Section Division I titles since 2010, including the softball team which MaxPreps named 2014 mythical national champion following a perfect season.")

    elif user == "2" or "bathroom" in user or "map" in user:
        txt.insert(END, "\n \n" + "Bot: Amador has 5 bathrooms around campus. There are two located in the Q building, one located in the nurse’s office, and two located near the center of campus.\n Here is a link to the maps: https://amador.pleasantonusd.net/about-us/campus-map")

    elif user == "3" or ("student" in user and "resources" in user):
        txt.insert(END, "\n \n" + "Bot: Check Clever!")

    elif ("teacher" in user):
        txt.insert(END, "\n \n" + "Bot: Amador has 110 teachers that educate students on a variety of topics. These include math, science, history, language arts (foreign included), creative arts, and technology.")

    elif ("admin" in user or "administration" in user):
        txt.insert(END, "\n \n" + "Bot: There are 6 administrators at amador. Mr. Fey is our principal, Ms. Harris, Mr. Jaramillo, Mr. Nelson, and Mr. Raman are all vice principals, and Mr. Pratt is our coordinator of operations. ")

    elif (user == "hi"):
        txt.insert(END, "\n\n" + "Bot: Hello!")
    elif (user == "clear"):
        txt.delete("1.0","end")
        
    else: 
        txt.insert(END, "\n \n" + "Bot: I'm sorry, I don't understand. Please check your spelling and retry")

    e.delete(0, END)

root.bind('<Return>', send)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=125, height=5).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#E5E5E5", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_YELLOW, command=send).grid(row=2, column=1)

txt.insert(END, "\n" + "Bot: Hello New Student! What would you like to know about?")
txt.insert(END, "\n" + "Here are some suggested Questions:\n"
            "1. Tell me more about Amador\n"
            "2. Map of Amador (Where are the classrooms and bathrooms)\n"
            "3. Student Resources\n"
            "Or feel free to write whatever: ")

root.mainloop()



