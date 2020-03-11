x = int(input("Enter price :"))
def vatC(total):
    result = total+(total*7/100)
    return result
print(vatC(x))