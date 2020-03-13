menulist = []
pricelist = []
def showBill():
    total = 0
    print("-------Your food-------")
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number],"THB")
        total += int(pricelist[number])
    print("Total Price :", total)
while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price :")
        menulist.append(menuName)
        pricelist.append(menuPrice)
showBill()