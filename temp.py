# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:31:27 2022

@author: Lenovo
"""
import pandas as pd
import random
from datetime import date, timedelta

arrData=[]
def _ToCSV(data):  
  print("***Array***\n", data)
  arrData.append(data)
  output = pd.DataFrame (arrData)
  print(output)
  output.to_csv("data3.csv",mode='a', index=False, header=False)
  arrData.clear()
dates="16-05-2022, 17-05-2022, 18-05-2022, 19-05-2022, 20-05-2022, 21-05-2022, 22-05-2022, 23-05-2022, 24-05-2022, 25-05-2022, 26-05-2022, 27-05-2022, 28-05-2022, 29-05-2022, 30-05-2022, 31-05-2022, 01-06-2022, 02-06-2022, 03-06-2022"
#tags = "creator, name, hours, contact, course, fees, location, hostel, event, document, campus, syllabus, library, infrastructure, canteen, iqac, placement, cshod, principal, sem, admission, facilities, college intake, uniform, committee, random, swear, vacation, salutaion, task, ragging, hod, transport, metro, scholarships, faq"
#tags = "transport, metro, scholarships, faq"
#print (random.choice(tags.split(",")).strip())
#for i in range (0,2500):
 #  var = random.choice(tags.split(",")).strip()
  #  print(var)
   # _ToCSV(var)

start_date = date(2022, 5, 16)
end_date = date(2022, 6, 3)
delta = timedelta(days=1)
count=0
while start_date <= end_date:
    var = random.choice(range (135,170))
    for j in range(1,var):
        #print
        _ToCSV(start_date.strftime("%d-%m-%Y"))
        count+=1
    start_date += delta

print(count)