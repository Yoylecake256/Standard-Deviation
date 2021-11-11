import pandas as pd
import plotly.express as px
import csv 
import math

with open('Num.csv', newline='')as f:
    reader= csv.reader(f)
    file_data= list(reader)
    
    print(file_data)
    
#remove the headers from csv
file_data.pop(0)

totalmarks = 0
totalenteries = len (file_data)

for marks in file_data:
    totalmarks += float(marks[1])
    
print(totalmarks)

mean = totalmarks/totalenteries
print("The mean is:", str(mean))