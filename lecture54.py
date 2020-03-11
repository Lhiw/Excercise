def login():
    user = input("Username :")
    pas = input("Password  :")
    if user == "admin" and pas == "1234":
        showmenu()
    else:
        print("Error","Please try again later")
def showmenu():
    print("--------shop--------")
    print("1.vat cal")
    print("2.p cal")
    menuSelect()
def menuSelect():
    select = int(input("number : "))
    if select == 1:
        print(priceC())
    if select == 2:
        print(priceC())
def vatC(totalP):
    result = totalP + (totalP * 7 / 100)
    return result
def priceC():
    price1 = int(input("frist product price :"))
    price2 = int(input("second product price :"))
    return vatC(price1 + price2)

login()