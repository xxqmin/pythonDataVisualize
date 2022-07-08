import csv

f = open('weather.csv',encoding = 'euc-kr')
data = csv.reader(f)
header = next(data)
data = list(data)

import matplotlib.pyplot as plt

data

header

for row in data:
  if row[2] == '':
    row[2] = -999

for row in data:
  if row[3] == '':
    row[3] = -999

high = []
high2 = []
low = []
low2 = []

for row in data:
  if row[0].split('-')[1] == "08" and row[0].split('-')[2] == "15":
    high.append(row[2])

for row in data:
  if row[0].split('-')[1] == "08" and row[0].split('-')[2] == "15":
    low.append(row[3])

for i in high:
  if i == -999:
    continue
  high2.append(float(i))

for i in low:
  if i == -999:
    continue
  low2.append(float(i))

plt.figure(figsize=(15,2))
plt.plot(high2, c = 'red')
plt.plot(low2,c  = 'blue')

plt.show()

avg = []
year_avg = []
year_avg_sum = 0


for row in data:
  if float(row[0].split('-')[0]) >= 1960 and float(row[0].split('-')[0]) <= 2020:
    year_avg.append(float(row[1]))
    if row[0].split('-')[1] == "12" and row[0].split('-')[2] == "31":
      for i in year_avg:
        year_avg_sum += i
      avg.append(year_avg_sum/len(year_avg))
      year_avg_sum = 0

plt.plot(avg)
plt.show()

