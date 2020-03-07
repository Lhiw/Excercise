Username = input("Username :")
Password = input("Password :")
a = 15
b = 20
if Username == "You" and Password == "1234":
    print("Welcome!")
    print("-------- Shop --------")
    print("1.น้ำโค้ก     15 THB/1")
    print("2.น้ำโซดา    20 THB/1")
    print("3.น้ำส้ม      15 THB/1")
    select = int(input("select here>>"))
    x = int(input("Number :"))
    y = x
    if select == 1:
        print("น้ำโค้ก", y,"ขวด ราคา:",a*x, "THB")
    elif select == 2:
        print("น้ำโซดา", y,"ขวด ราคา:",b*x, "THB")
    elif select == 3:
        print("น้ำส้ม", y,"ขวด ราคา:",a*x, "THB")
else:
    print("Eror Please try again!")
print("Thank You!!")