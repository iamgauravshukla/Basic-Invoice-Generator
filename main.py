import datetime
import random
import os


#Global Variables
print("             SG Mall             ")
product_list = []
price_list = []
quantity_list = []
final_price = []
total = 0

serial = random.randint(100, 10000)
date = datetime.date.today()
customer_name = input("Customer name : ")
customer_mobile = input("Mobile Number : ")


def purchase():
    while True:
        product_name = input("Enter Product name : ")
        product_price = int(input("Enter price : "))
        quantity = int(input("Quantity : "))
        if product_name == 'no' and product_price == quantity == 0:
            break
        product_list.append(product_name)
        price_list.append(product_price)
        quantity_list.append(quantity)

def Finalprice():
    for i in range(len(price_list)):
        final_price.append(price_list[i]*quantity_list[i])


def Invoice():
    print("           ****  Invoice  ****            ")
    print("SN :", serial, "    Date : ", date)
    print("Name : ", customer_name)
    print("Phone : ", customer_mobile)
    for i in range(len(product_list)):
        print("Item : ",product_list[i],"|","Quantity : ",quantity_list[i],"|","Price :",quantity_list[i],"*",price_list[i], " = ",final_price[i])
    return print("Total amount : ",sum(final_price))


purchase()
Finalprice()
os.system('cls')
Invoice()
print("           **** Thank You! ****            ")
