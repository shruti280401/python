import re
import mysql.connector
from mysql.connector import Error

connection=mysql.connector.connect(host='localhost',database='atm',user='root',password='root')

print("welcome to atm")
n=int(input("press 1 for login & 0 for register:"))
password =""
myname=""
depo=""
id=""



if n==0:
        name = input("enter name:")
        accn = int(input("enter account no:"))
        t = int(input("enter starting amount u want to deppositr"))
        pw=int(input("set ur password:"))

        myname = name
        password =pw
        depo=t
        id=accn

        val = (myname,password,depo,id)

        sql = "INSERT INTO data(my_name, pass_word,de_po,i_d ) VALUES (%s, %s, %s, %s)"
        mycursor = connection.cursor()

        mycursor.execute(sql,val)
        connection.commit()


if n==1:
    info=int(input("enter ur id:"))
    passw=int(input("enter password:"))
    #print(passw)
    mycursor = connection.cursor()
    mycursor.execute("""SELECT * FROM atm.data where i_d='%s'"""% (info))
    row=mycursor.fetchone()
    #(mycursor.rowcount)
    if mycursor.rowcount==1:

        mycursor.execute("""SELECT * FROM atm.data where pass_word='%s'""" % (passw))
        row = mycursor.fetchone()
        if mycursor.rowcount==1:
            print("ur looged in")
            d = int(input("enter 1 for withdrawl or 0 for deposit & 3 for exit:"))
            if d==1:
                a = int(input("how much u want to withdrawl:"))
                mycursor.execute("""SELECT de_po FROM atm.data where pass_word='%s'""" % (passw))
                col=mycursor.fetchone()
                x=list(col)
                for i in x:
                    z=(int(i))
                    c=z-a
                mycursor.execute("UPDATE data SET de_po='%s' where pass_word='%s'"%(c,passw))

            if d == 0:
                a = int(input("how much u want to deposite:"))
                mycursor.execute("""SELECT de_po FROM atm.data where pass_word='%s'""" % (passw))
                col = mycursor.fetchone()
                x = list(col)
                for i in x:
                    z = (int(i))
                    c = z + a
                mycursor.execute("UPDATE data SET de_po='%s' where pass_word='%s'" % (c, passw))

            if d == 3:
                 exit(0)


        else:
            print("invalid password")

    else:
        print("not")
    connection.commit()









