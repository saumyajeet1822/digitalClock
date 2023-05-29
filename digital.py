from tkinter import *
import datetime


def date_time():
    # for time
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    # for day month and year 
    day = time.strftime('%d')
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    

    # to add values in the 00
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)

    # to add values in the 00 in date month,year
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)


    # to change evrytime the value in miliseconds
    lab_hr.after(200,date_time)



clock = Tk()

# Title of the program
clock.title('   **** Digital Clock by Saumyajeet Das****')

# size of the program
clock.geometry('1000x500')


# change the background color
clock.config(bg = 'pink')

# making label
lab_hr = Label(clock, text="00", font=('Time new Roman',60,'bold'), bg='red',fg="white")
lab_hr.place(x=120,y=50,height=110,width=100)
# text position
lab_hr_txt = Label(clock, text="Hour", font=('Time new Roman',20,'bold'), bg='red',fg="white")
lab_hr_txt.place(x=120,y=190,height=40,width=100)


# minute block 
lab_min = Label(clock, text="00", font=('Time new Roman',60,'bold'), bg='red',fg="white")
lab_min.place(x=340,y=50,height=110,width=100)
# text position
lab_min_txt = Label(clock, text="Min.", font=('Time new Roman',20,'bold'), bg='red',fg="white")
lab_min_txt.place(x=340,y=190,height=40,width=100)



# seconds block  calculate 560+100=660+120=780
lab_sec = Label(clock, text="00", font=('Time new Roman',60,'bold'), bg='red',fg="white")
lab_sec.place(x=560,y=50,height=110,width=100)
# text position
lab_sec_txt = Label(clock, text="Sec.", font=('Time new Roman',20,'bold'), bg='red',fg="white")
lab_sec_txt.place(x=560,y=190,height=40,width=100)




# AM block
lab_am = Label(clock, text="00", font=('Time new Roman',50,'bold'), bg='red',fg="white")
lab_am.place(x=780,y=50,height=110,width=100)
# text position
lab_am_txt = Label(clock, text="AM/PM", font=('Time new Roman',20,'bold'), bg='red',fg="white")
lab_am_txt.place(x=780,y=190,height=40,width=100)

# 110*2=220+30*30=60+280-500=-220/5=45


# ********date*****
# making label 
lab_date = Label(clock, text="00", font=('Time new Roman',60,"bold"), bg='red',fg="white")
lab_date.place(x=120,y=270,height=110,width=100)
# text position
lab_date_txt = Label(clock, text="Date", font=('Time new Roman',20,'bold'), bg='red',fg="white")
lab_date_txt.place(x=120,y=410,height=40,width=100)
# 190+40=230+40=270



# month block 
lab_mo = Label(clock, text="00", font=('Time new Roman',60,'bold'), bg='red',fg="white")
lab_mo.place(x=340,y=270,height=110,width=100)
# text position
lab_mo_txt = Label(clock, text="Month", font=('Time new Roman',20,'bold'), bg='red',fg="white")
lab_mo_txt.place(x=340,y=410,height=40,width=100)




# year block
lab_year = Label(clock, text="00", font=('Time new Roman',60,'bold'), bg='red',fg="white")
lab_year.place(x=560,y=270,height=110,width=100)
# text position
lab_year_txt = Label(clock, text="Year", font=('Time new Roman',20,'bold'), bg='red',fg="white")
lab_year_txt.place(x=560,y=410,height=40,width=100)



# Day block
lab_day = Label(clock, text="00", font=('Time new Roman',35,'bold'), bg='red',fg="white")
lab_day.place(x=780,y=270,height=110,width=100)
# text position
lab_day_txt = Label(clock, text="Day", font=('Time new Roman',20,'bold'), bg='red',fg="white")
lab_day_txt.place(x=780,y=410,height=40,width=100)






date_time()

# it will run the graphics
clock.mainloop()


