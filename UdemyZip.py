import csv
import os


file ="web_starter.csv"
title=[]
price=[]
subCount=[]
NumReviews=[]
CourseLength=[]

with open(file,  encoding="utf8", newline='') as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        title.append(row[1])
        price.append(row[4])
        subCount.append(row[5])
        NumReviews.append(row[7])
        CourseLength.append(row[10])

    
# Read the header row first (skip this step if there is now header)


# Read each row of data after the header
    
# Three Lists


Header = ["Title", "Price", "Subscriber Count", "Number of Reviews","Course Length"]

# Zip all three lists together into tuples
roster = zip(title,price,subCount,NumReviews,CourseLength)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Title", "Price", "Subscriber Count", "Number of Reviews","Course Length"])

    writer.writerows(roster)


# # to print out to terminal:
# #comment out above code and run the code below
# for employee in roster:
#     print(employee)
