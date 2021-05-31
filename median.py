import csv 
with open("SOCR-HeightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][2]
    newdata.append(num)
n=len(newdata)
newdata.sort()
if n%2==0:
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    Median=(median1 + median2)/2
    print(Median)
else:
    Median = float(newdata[n//2])
    print(Median)
    