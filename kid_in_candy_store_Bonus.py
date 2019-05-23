# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

for i in range(len(candyList)):
        print("[" + str(i) + "] " + candyList[i])

# The amount of candy the user will be allowed to choose
allowance = int(input("How many candies you want? "))
run = "y"

# The list used to store all of the candies selected inside of
candyCart = []
while run=="y":
    for i in range(allowance):
        candy= int(input("Input the candies you like"))
        candyCart.append(candyList[candy])
    print("Your Candy Cart has below candies")    
        
        # Print out options1

    for i in candyCart:
        print (i)
    run=input("Do you want more candies? Enter y or n ")
    if run == "y":
        allowance = int(input("How many candies you want? "))
    else:
        print("\n Your Final Candy Cart has below candies")    
        
        # Print out options1

        for i in candyCart:
            print (i)
        print("Enjoy your Candies")