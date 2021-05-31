import csv 
with open("SOCR-HeightWeight.csv",newline='') as f:
    file_read=csv.reader(f)
    file_data=list(file_read)
file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newdata.append(float(num))
total=0
for x in newdata:
    total=total + x
mean = total/len(newdata)
print(mean)