'''
@author: P.Saravanan
Date:18-09-2024
'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk, StringVar

f=Tk()
f.geometry("250x50")
f.title("Select Class")
f.config(bg="pink")

import mysql.connector
mydb=mysql.connector.connect(host="Localhost",user="root",#passwd="root",
                         passwd="root",database='marklist')
mycursor=mydb.cursor()

lo=ttk.Label(f,text="Select Student's Class")
lo.grid(row=0,column=0)

def get_10():
    f.destroy()
    s=Tk()
    s.geometry("295x70")
    s.title("Details")
    s.config(bg="pink")

    

    roll=Label(s,text="Exam Roll Number \t:",bg="pink",fg="black")
    roll.grid(row=1,column=0)
    eroll=Entry(s)
    eroll.grid(row=1,column=1)
    
    def get_next():

        sr=int(eroll.get())
        mycursor.execute("select *from 10th where Stu_Roll_Number=%d"%(sr))
        myres=mycursor.fetchone()
        
        r=Tk()
        r.geometry("650x400")
        r.title("Result")
        r.config(bg="pink")

        title=Label(r,text="SENIOR SCHOOL CERTIFICATE EXAMINATION",bg="red",fg="black")
        title.grid(row=0,column=1)

        name=Label(r,text="Student Name",bg="pink",fg="black")
        name.grid(row=1,column=0)
        e1name=Entry(r)
        e1name.grid(row=1,column=1)
        e1name.insert(0,myres[0])

        roll=Label(r,text="Roll No.",bg="pink",fg="black")
        roll.grid(row=2,column=0)
        e1roll=Entry(r)
        e1roll.grid(row=2,column=1)
        e1roll.insert(0,eroll.get())

        s.destroy()

        mother=Label(r,text="Mother's Name",bg="pink",fg="black")
        mother.grid(row=3,column=0)
        emother=Entry(r)
        emother.grid(row=3,column=1)
        emother.insert(0,myres[2])

        father=Label(r,text="Father's/Guardian's Name",bg="pink",fg="black")
        father.grid(row=4,column=0)
        efather=Entry(r)
        efather.grid(row=4,column=1)
        efather.insert(0,myres[3])

        school=Label(r,text="School Name",bg="pink",fg="black")
        school.grid(row=5,column=0)
        eschool=Entry(r)
        eschool.grid(row=5,column=1)
        eschool.insert(0,myres[4])

        code=Label(r,text="School Code",bg="pink",fg="black")
        code.grid(row=6,column=0)
        ecode=Entry(r)
        ecode.grid(row=6,column=1)
        ecode.insert(0,myres[5])

        s1=Label(r,text=" ",bg="pink",fg="black")
        s1.grid(row=7,column=0)
        s2=Label(r,text=" ",bg="pink",fg="black")
        s2.grid(row=7,column=1)

        sub=Label(r,text="SUBJECT NAME",bg="red",fg="black")
        sub.grid(row=8,column=0)
        e11=Label(r,text="ENGLISH",bg="pink",fg="black")
        e11.grid(row=9,column=0)
        e12=Label(r,text="MATHS",bg="pink",fg="black")
        e12.grid(row=10,column=0)
        e13=Label(r,text="TAMIL/HINDI",bg="pink",fg="black")
        e13.grid(row=11,column=0)
        e14=Label(r,text="SCIENCE",bg="pink",fg="black")
        e14.grid(row=12,column=0)
        e15=Label(r,text="SOCIAl SCIENCE",bg="pink",fg="black")
        e15.grid(row=13,column=0)

        mark=Label(r,text="THEORY MARK",bg="red",fg="black")
        mark.grid(row=8,column=1)
        e21=Entry(r)
        e21.grid(row=9,column=1)
        e21.insert(0,myres[6])
        e22=Entry(r)
        e22.grid(row=10,column=1)
        e22.insert(0,myres[7])
        e23=Entry(r)
        e23.grid(row=11,column=1)
        e23.insert(0,myres[8])
        e24=Entry(r)
        e24.grid(row=12,column=1)
        e24.insert(0,myres[9])
        e25=Entry(r)
        e25.grid(row=13,column=1)
        e25.insert(0,myres[10])

        namew=Label(r,text="PRACTICAL MARK",bg="red",fg="black")
        namew.grid(row=8,column=2)
        e31=Label(r,text="20",bg="pink",fg="black")
        e31.grid(row=9,column=2)
        e32=Label(r,text="20",bg="pink",fg="black")
        e32.grid(row=10,column=2)
        e33=Label(r,text="20",bg="pink",fg="black")
        e33.grid(row=11,column=2)
        e34=Label(r,text="20",bg="pink",fg="black")
        e34.grid(row=12,column=2)
        e35=Label(r,text="20",bg="pink",fg="black")
        e35.grid(row=13,column=2)

        total=Label(r,text="MARK",bg="red",fg="black")
        total.grid(row=8,column=3)
        e41=Entry(r)
        e41.grid(row=9,column=3)
        e41.insert(0,myres[11])
        e42=Entry(r)
        e42.grid(row=10,column=3)
        e42.insert(0,myres[12])
        e43=Entry(r)
        e43.grid(row=11,column=3)
        e43.insert(0,myres[13])
        e44=Entry(r)
        e44.grid(row=12,column=3)
        e44.insert(0,myres[14])
        e45=Entry(r)
        e45.grid(row=13,column=3)
        e45.insert(0,myres[15])

        s3=Label(r,text=" ",bg="pink",fg="black")
        s3.grid(row=14,column=0)
        s4=Label(r,text=" ",bg="pink",fg="black")
        s4.grid(row=14,column=1)

        tmark=Label(r,text="TOTAL MARK",bg="red",fg="black")
        tmark.grid(row=15,column=0)
        etmark=Entry(r)
        etmark.grid(row=15,column=1)
        etmark.insert(0,myres[16])

        result=Label(r,text="RESULT",bg="red",fg="black")
        result.grid(row=15,column=2)
        eresult=Entry(r)
        eresult.grid(row=15,column=3)
        eresult.insert(0,myres[17])

        s5=Label(r,text=" ",bg="pink",fg="black")
        s5.grid(row=16,column=0)
        s6=Label(r,text=" ",bg="pink",fg="black")
        s6.grid(row=16,column=1)

        def get_exit():
            r.destroy()
            
        be=Button(r,text="EXIT",command=get_exit)
        be.grid(row=17,column=1)

        r.mainloop()

    b11=Button(s,text="SEARCH",command=get_next)
    b11.grid(row=2,column=0)

    s.mainloop()


def get_12():
    f.destroy()
    main=Tk()
    main.geometry("350x50")
    main.title("Select Subject")
    main.config(bg="pink")

    l1=ttk.Label(main,text="\tSelect Student's Group\t")
    l1.grid(row=0,column=1)


    def get_bio():
        main.destroy()
        s=Tk()
        s.geometry("295x70")
        s.title("Details")
        s.config(bg="pink")
        '''
        import mysql.connector
        mydb=mysql.connector.connect(host="Localhost",user="root",passwd="root",database='marklist')
        mycursor=mydb.cursor()
        '''
        roll=Label(s,text="Exam Roll Number \t:",bg="pink",fg="black")
        roll.grid(row=1,column=0)
        eroll=Entry(s)
        eroll.grid(row=1,column=1)
        
        def get_next():

            sr=int(eroll.get())
            mycursor.execute("select *from bio where Stu_Roll_Number=%d"%(sr))
            myres=mycursor.fetchone()
            
            r=Tk()
            r.geometry("650x400")
            r.title("Result")
            r.config(bg="pink")

            title=Label(r,text="SENIOR SCHOOL CERTIFICATE EXAMINATION",bg="red",fg="black")
            title.grid(row=0,column=1)

            name=Label(r,text="Student Name",bg="pink",fg="black")
            name.grid(row=1,column=0)
            e1name=Entry(r)
            e1name.grid(row=1,column=1)
            e1name.insert(0,myres[0])

            roll=Label(r,text="Roll No.",bg="pink",fg="black")
            roll.grid(row=2,column=0)
            e1roll=Entry(r)
            e1roll.grid(row=2,column=1)
            e1roll.insert(0,eroll.get())

            s.destroy()

            mother=Label(r,text="Mother's Name",bg="pink",fg="black")
            mother.grid(row=3,column=0)
            emother=Entry(r)
            emother.grid(row=3,column=1)
            emother.insert(0,myres[2])

            father=Label(r,text="Father's/Guardian's Name",bg="pink",fg="black")
            father.grid(row=4,column=0)
            efather=Entry(r)
            efather.grid(row=4,column=1)
            efather.insert(0,myres[3])

            school=Label(r,text="School Name",bg="pink",fg="black")
            school.grid(row=5,column=0)
            eschool=Entry(r)
            eschool.grid(row=5,column=1)
            eschool.insert(0,myres[4])

            code=Label(r,text="School Code",bg="pink",fg="black")
            code.grid(row=6,column=0)
            ecode=Entry(r)
            ecode.grid(row=6,column=1)
            ecode.insert(0,myres[5])

            s1=Label(r,text=" ",bg="pink",fg="black")
            s1.grid(row=7,column=0)
            s2=Label(r,text=" ",bg="pink",fg="black")
            s2.grid(row=7,column=1)

            sub=Label(r,text="SUBJECT NAME",bg="red",fg="black")
            sub.grid(row=8,column=0)
            e11=Label(r,text="ENGLISH",bg="pink",fg="black")
            e11.grid(row=9,column=0)
            e12=Label(r,text="MATHS",bg="pink",fg="black")
            e12.grid(row=10,column=0)
            e13=Label(r,text="BIOLOGY",bg="pink",fg="black")
            e13.grid(row=11,column=0)
            e14=Label(r,text="PHYSICS",bg="pink",fg="black")
            e14.grid(row=12,column=0)
            e15=Label(r,text="CHEMISTRY",bg="pink",fg="black")
            e15.grid(row=13,column=0)

            mark=Label(r,text="THEORY MARK",bg="red",fg="black")
            mark.grid(row=8,column=1)
            e21=Entry(r)
            e21.grid(row=9,column=1)
            e21.insert(0,myres[6])
            e22=Entry(r)
            e22.grid(row=10,column=1)
            e22.insert(0,myres[7])
            e23=Entry(r)
            e23.grid(row=11,column=1)
            e23.insert(0,myres[8])
            e24=Entry(r)
            e24.grid(row=12,column=1)
            e24.insert(0,myres[9])
            e25=Entry(r)
            e25.grid(row=13,column=1)
            e25.insert(0,myres[10])

            namew=Label(r,text="PRACTICAL MARK",bg="red",fg="black")
            namew.grid(row=8,column=2)
            e31=Label(r,text="20",bg="pink",fg="black")
            e31.grid(row=9,column=2)
            e32=Label(r,text="20",bg="pink",fg="black")
            e32.grid(row=10,column=2)
            e33=Label(r,text="30",bg="pink",fg="black")
            e33.grid(row=11,column=2)
            e34=Label(r,text="30",bg="pink",fg="black")
            e34.grid(row=12,column=2)
            e35=Label(r,text="30",bg="pink",fg="black")
            e35.grid(row=13,column=2)

            total=Label(r,text="MARK",bg="red",fg="black")
            total.grid(row=8,column=3)
            e41=Entry(r)
            e41.grid(row=9,column=3)
            e41.insert(0,myres[11])
            e42=Entry(r)
            e42.grid(row=10,column=3)
            e42.insert(0,myres[12])
            e43=Entry(r)
            e43.grid(row=11,column=3)
            e43.insert(0,myres[13])
            e44=Entry(r)
            e44.grid(row=12,column=3)
            e44.insert(0,myres[14])
            e45=Entry(r)
            e45.grid(row=13,column=3)
            e45.insert(0,myres[15])

            s3=Label(r,text=" ",bg="pink",fg="black")
            s3.grid(row=14,column=0)
            s4=Label(r,text=" ",bg="pink",fg="black")
            s4.grid(row=14,column=1)

            tmark=Label(r,text="TOTAL MARK",bg="red",fg="black")
            tmark.grid(row=15,column=0)
            etmark=Entry(r)
            etmark.grid(row=15,column=1)
            etmark.insert(0,myres[16])

            result=Label(r,text="RESULT",bg="red",fg="black")
            result.grid(row=15,column=2)
            eresult=Entry(r)
            eresult.grid(row=15,column=3)
            eresult.insert(0,myres[17])

            s5=Label(r,text=" ",bg="pink",fg="black")
            s5.grid(row=16,column=0)
            s6=Label(r,text=" ",bg="pink",fg="black")
            s6.grid(row=16,column=1)

            def get_exit():
                r.destroy()
                
            be=Button(r,text="EXIT",command=get_exit)
            be.grid(row=17,column=1)

            r.mainloop()

        b11=Button(s,text="SEARCH",command=get_next)
        b11.grid(row=2,column=0)

        s.mainloop()

    b1=ttk.Button(main,text="BIO MATHS",command=get_bio)
    b1.grid(row=1,column=0)

    def get_comp():
        main.destroy()
        s=Tk()
        s.geometry("295x70")
        s.title("Details")
        s.config(bg="pink")
        '''
        import mysql.connector
        mydb=mysql.connector.connect(host="Localhost",user="root",passwd="root",database='marklist')
        mycursor=mydb.cursor()
        '''

        roll=Label(s,text="Exam Roll Number \t:",bg="pink",fg="black")
        roll.grid(row=1,column=0)
        eroll=Entry(s)
        eroll.grid(row=1,column=1)
        def get_next():
            sr=int(eroll.get())
            mycursor.execute("select *from comp where Stu_Roll_Number=%d"%(sr))
            myres=mycursor.fetchone()
            
            r=Tk()
            r.geometry("650x400")
            r.title("Result")
            r.config(bg="pink")

            title=Label(r,text="SENIOR SCHOOL CERTIFICATE EXAMINATION",bg="red",fg="black")
            title.grid(row=0,column=1)

            name=Label(r,text="Student Name",bg="pink",fg="black")
            name.grid(row=1,column=0)
            nentry=Entry(r)
            nentry.grid(row=1,column=1)
            nentry.insert(0,myres[0])

            roll=Label(r,text="Roll No.",bg="pink",fg="black")
            roll.grid(row=2,column=0)
            nroll=Entry(r)
            nroll.grid(row=2,column=1)
            nroll.insert(0,eroll.get())

            s.destroy()

            mother=Label(r,text="Mother's Name",bg="pink",fg="black")
            mother.grid(row=3,column=0)
            emother=Entry(r)
            emother.grid(row=3,column=1)
            emother.insert(0,myres[2])

            father=Label(r,text="Father's/Guardian's Name",bg="pink",fg="black")
            father.grid(row=4,column=0)
            efather=Entry(r)
            efather.grid(row=4,column=1)
            efather.insert(0,myres[3])

            school=Label(r,text="School Name",bg="pink",fg="black")
            school.grid(row=5,column=0)
            eschool=Entry(r)
            eschool.grid(row=5,column=1)
            eschool.insert(0,myres[4])

            code=Label(r,text="School Code",bg="pink",fg="black")
            code.grid(row=6,column=0)
            ecode=Entry(r)
            ecode.grid(row=6,column=1)
            ecode.insert(0,myres[5])

            s1=Label(r,text=" ",bg="pink",fg="black")
            s1.grid(row=7,column=0)
            s2=Label(r,text=" ",bg="pink",fg="black")
            s2.grid(row=7,column=1)

            sub=Label(r,text="SUBJECT NAME",bg="red",fg="black")
            sub.grid(row=8,column=0)
            e11=Label(r,text="ENGLISH",bg="pink",fg="black")
            e11.grid(row=9,column=0)
            e12=Label(r,text="MATHS",bg="pink",fg="black")
            e12.grid(row=10,column=0)
            e13=Label(r,text="COMPUTER",bg="pink",fg="black")
            e13.grid(row=11,column=0)
            e14=Label(r,text="PHYSICS",bg="pink",fg="black")
            e14.grid(row=12,column=0)
            e15=Label(r,text="CHEMISTRY",bg="pink",fg="black")
            e15.grid(row=13,column=0)

            mark=Label(r,text="THEORY MARK",bg="red",fg="black")
            mark.grid(row=8,column=1)
            e21=Entry(r)
            e21.grid(row=9,column=1)
            e21.insert(0,myres[6])
            e22=Entry(r)
            e22.grid(row=10,column=1)
            e22.insert(0,myres[7])
            e23=Entry(r)
            e23.grid(row=11,column=1)
            e23.insert(0,myres[8])
            e24=Entry(r)
            e24.grid(row=12,column=1)
            e24.insert(0,myres[9])
            e25=Entry(r)
            e25.grid(row=13,column=1)
            e25.insert(0,myres[10])

            namew=Label(r,text="PRACTICAL MARK",bg="red",fg="black")
            namew.grid(row=8,column=2)
            e31=Label(r,text="20",bg="pink",fg="black")
            e31.grid(row=9,column=2)
            e32=Label(r,text="20",bg="pink",fg="black")
            e32.grid(row=10,column=2)
            e33=Label(r,text="30",bg="pink",fg="black")
            e33.grid(row=11,column=2)
            e34=Label(r,text="30",bg="pink",fg="black")
            e34.grid(row=12,column=2)
            e35=Label(r,text="30",bg="pink",fg="black")
            e35.grid(row=13,column=2)

            total=Label(r,text="MARK",bg="red",fg="black")
            total.grid(row=8,column=3)
            e41=Entry(r)
            e41.grid(row=9,column=3)
            e41.insert(0,myres[11])
            e42=Entry(r)
            e42.grid(row=10,column=3)
            e42.insert(0,myres[12])
            e43=Entry(r)
            e43.grid(row=11,column=3)
            e43.insert(0,myres[13])
            e44=Entry(r)
            e44.grid(row=12,column=3)
            e44.insert(0,myres[14])
            e45=Entry(r)
            e45.grid(row=13,column=3)
            e45.insert(0,myres[15])

            s3=Label(r,text=" ",bg="pink",fg="black")
            s3.grid(row=14,column=0)
            s4=Label(r,text=" ",bg="pink",fg="black")
            s4.grid(row=14,column=1)

            tmark=Label(r,text="TOTAL MARK",bg="red",fg="black")
            tmark.grid(row=15,column=0)
            etmark=Entry(r)
            etmark.grid(row=15,column=1)
            etmark.insert(0,myres[16])

            result=Label(r,text="RESULT",bg="red",fg="black")
            result.grid(row=15,column=2)
            eresult=Entry(r)
            eresult.grid(row=15,column=3)
            eresult.insert(0,myres[17])

            s5=Label(r,text=" ",bg="pink",fg="black")
            s5.grid(row=16,column=0)
            s6=Label(r,text=" ",bg="pink",fg="black")
            s6.grid(row=16,column=1)

            def get_exit():
                r.destroy()

            be=Button(r,text="EXIT",command=get_exit)
            be.grid(row=17,column=1)


            r.mainloop()

        b11=Button(s,text="SEARCH",command=get_next)
        b11.grid(row=2,column=0)

        s.mainloop()

    b2=ttk.Button(main,text="COMPUTER SCIENCE",command=get_comp)
    b2.grid(row=1,column=1)

    def get_coms():
        main.destroy()
        s=Tk()
        s.geometry("295x70")
        s.title("Details")
        s.config(bg="pink")
        '''
        import mysql.connector
        mydb=mysql.connector.connect(host="Localhost",user="root",passwd="root",database='marklist')
        mycursor=mydb.cursor()
        '''
        roll=Label(s,text="Exam Roll Number \t:",bg="pink",fg="black")
        roll.grid(row=1,column=0)
        eroll=Entry(s)
        eroll.grid(row=1,column=1)
        def get_next():
            sr=int(eroll.get())
            mycursor.execute("select *from coms where Stu_Roll_Number=%d"%(sr))
            myres=mycursor.fetchone()
            
            r=Tk()
            r.geometry("650x400")
            r.title("Result")
            r.config(bg="pink")

            title=Label(r,text="SENIOR SCHOOL CERTIFICATE EXAMINATION",bg="red",fg="black")
            title.grid(row=0,column=1)

            name=Label(r,text="Student Name",bg="pink",fg="black")
            name.grid(row=1,column=0)
            nentry=Entry(r)
            nentry.grid(row=1,column=1)
            nentry.insert(0,myres[0])
            
            roll=Label(r,text="Roll No.",bg="pink",fg="black")
            roll.grid(row=2,column=0)
            nroll=Entry(r)
            nroll.grid(row=2,column=1)
            nroll.insert(0,eroll.get())

            s.destroy()

            mother=Label(r,text="Mother's Name",bg="pink",fg="black")
            mother.grid(row=3,column=0)
            emother=Entry(r)
            emother.grid(row=3,column=1)
            emother.insert(0,myres[2])

            father=Label(r,text="Father's/Guardian's Name",bg="pink",fg="black")
            father.grid(row=4,column=0)
            efather=Entry(r)
            efather.grid(row=4,column=1)
            efather.insert(0,myres[3])

            school=Label(r,text="School Name",bg="pink",fg="black")
            school.grid(row=5,column=0)
            eschool=Entry(r)
            eschool.grid(row=5,column=1)
            eschool.insert(0,myres[4])

            code=Label(r,text="School Code",bg="pink",fg="black")
            code.grid(row=6,column=0)
            ecode=Entry(r)
            ecode.grid(row=6,column=1)
            ecode.insert(0,myres[5])

            s1=Label(r,text=" ",bg="pink",fg="black")
            s1.grid(row=7,column=0)
            s2=Label(r,text=" ",bg="pink",fg="black")
            s2.grid(row=7,column=1)

            sub=Label(r,text="SUBJECT NAME",bg="red",fg="black")
            sub.grid(row=8,column=0)
            e11=Label(r,text="ENGLISH",bg="pink",fg="black")
            e11.grid(row=9,column=0)
            e12=Label(r,text="MATHS",bg="pink",fg="black")
            e12.grid(row=10,column=0)
            e13=Label(r,text="COMMERCE",bg="pink",fg="black")
            e13.grid(row=11,column=0)
            e14=Label(r,text="BUSINESS",bg="pink",fg="black")
            e14.grid(row=12,column=0)
            e15=Label(r,text="ECONOMICS",bg="pink",fg="black")
            e15.grid(row=13,column=0)

            mark=Label(r,text="THEORY MARK",bg="red",fg="black")
            mark.grid(row=8,column=1)
            e21=Entry(r)
            e21.grid(row=9,column=1)
            e21.insert(0,myres[6])
            e22=Entry(r)
            e22.grid(row=10,column=1)
            e22.insert(0,myres[7])
            e23=Entry(r)
            e23.grid(row=11,column=1)
            e23.insert(0,myres[8])
            e24=Entry(r)
            e24.grid(row=12,column=1)
            e24.insert(0,myres[9])
            e25=Entry(r)
            e25.grid(row=13,column=1)
            e25.insert(0,myres[10])

            namew=Label(r,text="PRACTICAL MARK",bg="red",fg="black")
            namew.grid(row=8,column=2)
            e31=Label(r,text="20",bg="pink",fg="black")
            e31.grid(row=9,column=2)
            e32=Label(r,text="20",bg="pink",fg="black")
            e32.grid(row=10,column=2)
            e33=Label(r,text="20",bg="pink",fg="black")
            e33.grid(row=11,column=2)
            e34=Label(r,text="20",bg="pink",fg="black")
            e34.grid(row=12,column=2)
            e35=Label(r,text="20",bg="pink",fg="black")
            e35.grid(row=13,column=2)

            total=Label(r,text="MARK",bg="red",fg="black")
            total.grid(row=8,column=3)
            e41=Entry(r)
            e41.grid(row=9,column=3)
            e41.insert(0,myres[11])
            e42=Entry(r)
            e42.grid(row=10,column=3)
            e42.insert(0,myres[12])
            e43=Entry(r)
            e43.grid(row=11,column=3)
            e43.insert(0,myres[13])
            e44=Entry(r)
            e44.grid(row=12,column=3)
            e44.insert(0,myres[14])
            e45=Entry(r)
            e45.grid(row=13,column=3)
            e45.insert(0,myres[15])

            s3=Label(r,text=" ",bg="pink",fg="black")
            s3.grid(row=14,column=0)
            s4=Label(r,text=" ",bg="pink",fg="black")
            s4.grid(row=14,column=1)

            tmark=Label(r,text="TOTAL MARK",bg="red",fg="black")
            tmark.grid(row=15,column=0)
            etmark=Entry(r)
            etmark.grid(row=15,column=1)
            etmark.insert(0,myres[16])

            result=Label(r,text="RESULT",bg="red",fg="black")
            result.grid(row=15,column=2)
            eresult=Entry(r)
            eresult.grid(row=15,column=3)
            eresult.insert(0,myres[17])

            s5=Label(r,text=" ",bg="pink",fg="black")
            s5.grid(row=16,column=0)
            s6=Label(r,text=" ",bg="pink",fg="black")
            s6.grid(row=16,column=1)

            def get_exit():
                r.destroy()

            be=Button(r,text="EXIT",command=get_exit)
            be.grid(row=17,column=1)

            r.mainloop()

        b11=Button(s,text="SEARCH",command=get_next)
        b11.grid(row=2,column=0)

        s.mainloop()

    b3=ttk.Button(main,text="COMMERCE",command=get_coms)
    b3.grid(row=1,column=2)

    main.mainloop()
    
b10=ttk.Button(f,text="Class 10th",command=get_10)
b10.grid(row=1,column=0)
b12=ttk.Button(f,text="Class 12th",command=get_12)
b12.grid(row=1,column=1)

f.mainloop()
