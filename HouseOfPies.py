pieList = ["Pecan", "Apple Crisp","Bean","Banoffee",  "Black Bun", "Blueberry", "Buko", "Burek",  "Tamale", "Steak"]
for i in range(len(pieList)):
    print("[" + str(i+1) + "] " + pieList[i])
PiesOrdered=[]
run = 'y'
count=[0,0,0,0,0,0,0,0,0,0]
while run=='y':
    order = int(input("Which pie do you want to Order. Enter Number"))
    order=order-1
    count[int(order)]=count[int(order)]+1
    print (f"We will have that {pieList[order]} right out for you")
    run =input("Do you want to make another Order? Enter y/n ")
    if run =='n':
        print("Your Cart contains below Pies")
        for i in range(len(pieList)):
            print("["+str(count[i])+"]"+pieList[i])