#intro
print ("\n      This is the Temperatue conventor. ")
print ("      Developed by Min Sitt Paing Mhuu")
print ("\n      Facebook ::https://www.facebook.com/minsitt.mspm ")
print ("      Email :: #")

#ask

def fun():
    ask = input("\n1 : from Celsius(C*) to Fehrentheit(F*)\n2 : from Fehrentheit(F)* to Celsius(C*)\n3 : from Celsius(C*) to Kelvin(K)\n4 : from Fehrentheit(F)* to Kelvin(K)\n5 : from Kelvin(K) to Celsius(C*)\n6 : from Kelvin(K) to Fehrentheit(F)*\n7 : exit the program\n\n( Choose any options 1 from 7! ) : ")
    if ask == "1":
        #C* to F*
        ctemp = int(input("Input temperature in Celsius (You Don't Need to type unit expression!) : "))
        ftemp = int((ctemp * 9/5) + 32)
        print ("The themperature of ",ctemp,"*C in Fehrentheit is equals to ",ftemp,"*F.")
        print ("\nThanks for using my tool.")
        fun1()


    elif ask == "2":
        #F* to C*
        f_temp = int(input("Input temperature in Fehrentheit (You Don't Need to type unit expression!) : "))
        c_temp = int((f_temp - 32) * 5/9)
        print ("The themperature of ",f_temp,"*F in Celsius is equals to ",c_temp,"*C.")
        print ("\nThanks for using my tool.")
        fun1()

    elif ask == "3":
        #C* tp K
        ctemp1 = int(input("Input temperature in Celsius (You Don't Need to type unit expression!) : "))
        ktemp = (ctemp1 + 273.15)
        print ("The themperature of ",ctemp1,"*C in Kelvin is equals to ",ktemp,"K.")
        print ("\nThanks for using my tool.")
        fun1()

    elif ask == "4":
        #F* to K
        ftemp1 = int(input("Input temperature in Fehrentheit (You Don't Need to type unit expression!) : "))
        ktemp1 = (((ftemp1 - 32) * 5/9) + 273.15)
        print ("The themperature of ",ftemp1,"*F in Kelvin is equals to ",ktemp1,"K.")
        print ("\nThanks for using my tool.")
        fun1()

    elif ask == "5":
        #K to C*
        ktemp2 = float(input("Input temperature in Kelvin (You Don't Need to type unit expression!) : "))
        ctemp2 = int(ktemp2 - 273.15)
        print ("The themperature of ",ktemp2,"K in Celsius is equals to ",ctemp2,"*C.")
        print ("\nThanks for using my tool.")
        fun1()

    elif ask == "6":
        #K to F*
        ktemp3 = float(input("Input temperature in Kelvin (You Don't Need to type unit expression!) : "))
        ftemp2 = int(((ktemp3 - 273.15)* 9/5) + 32)
        print ("The themperature of ",ktemp3,"K in Celsius is equals to ",ftemp2,"*F.")
        print ("\nThanks for using my tool.")
        fun1()

    elif ask == "7":
        print ("\nThanks for using my tool.")

    else:
        print("!!--------Invaild Option (",ask,")--------!!")
        fun1()

def fun1():
    ask1 = input("Want to do it one more time ? (Type y/n) : ")
    if ask1 == "y":
        fun()
    else:
        print ("\nThanks for using my tool.")

fun()
