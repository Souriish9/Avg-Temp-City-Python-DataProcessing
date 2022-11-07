#Open the file
dataset=open("citytemp.csv","r")

#Read the first variable and split into variables
set1=dataset.readline()
city,temperature,unit=set1.split(',')
prev_city=city

#Point to the first record
dataset.seek(0)

#Initialise the variables
tempSum=0.0
count=0
averageTemp=0.0

for records in dataset:
    records=records.rstrip('\n')
    city,temperature,unit=records.split(',')

    if unit== "C":
        temperature=(float(temperature)*9/5)+32

    if city!=prev_city:
        averageTemp=tempSum/count
        print(prev_city+" "+str(round(averageTemp,2)))
        prev_city=city
        tempSum=0.0
        count=0
        averageTemp=0.0
    tempSum=tempSum+float(temperature)
    count+=1
else:
    averageTemp=tempSum/count
    print(prev_city+" "+str(round(averageTemp,2)))
