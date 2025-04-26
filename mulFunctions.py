class mulFunctions():
    def Subfields():
        a=('Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing')
        print ("Subfields in AI are:")
        for i in a:
            print (i)

    def oddeven():
        a=int(input("Enter a Number:"))
        if (a%2==0):
          print(a,"is Even Number")
        else:
            print(a, "is Odd Number")

    def Eligible():
        a=input("Your Gender:")
        b=int(input("Your Age:"))
        if (a=="Male" or "male"):
            if b>=21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(a=="Female" or "female"):
                        if b>=18:
                            print("ELIGIBLE")
                        else:
                            print("NOT ELIGIBLE")

    def percentage():
        s1=int(input("Subject1:"))
        s2=int(input("Subject2:"))
        s3=int(input("Subject3:"))
        s4=int(input("Subject4:"))
        s5=int(input("Subject5:"))
        T=s1+s2+s3+s4+s5
        P=T/5
        print("Total :",T)
        print("Percentage :",P)

    def Triangle():
        H=int(input("Height :"))
        B=int(input("Breadth :"))
        print("Area Formula: (Height*Breadth)/2")
        print("Area of Triangle :",(H*B)/2)
        H1=int(input("Height1 :"))
        H2=int(input("Height2 :"))
        B=int(input("Breadth :"))
        P=H1+H2+B
        print("Perimeter Formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",P)