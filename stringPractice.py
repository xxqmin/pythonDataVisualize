import csv

from google.colab import files

upload = files.upload()

f = open('weather.csv',encoding='euc-kr')
data = csv.reader(f)
header = next(data)
data = list(data)

header

data[0][0].split('-')[0][2:4]

array = [1,2,3,4,5]

array2 = [[1,2],[3,4],[5,6],[7,8]]

array2[0][0]

dictionary = {'boy':"소년", 'girl':'소녀',"book":"책"}
print(dictionary['boy'])
dictionary.keys()

dictionary.values()

dictionary.items()

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

keylist = dictionary.keys()
for i in keylist:
  print(i)

score = []
for i in range(5):
  score.append(int(input("성적입력:")))
print(score)

sum = 0
for s in score:
  sum += s
print("총점은 {}이고 평균은 {}입니다.".format(sum,sum/len(score)))

song = '''by the rivers of babylon'''

alphabet = dict()
for c in song:
  if c.isalpha() == False:
    continue
  c = c.lower()
  if c not in alphabet:
    alphabet[c] = 1
  else:
    alphabet[c] += 1
print(alphabet)

key = list(alphabet.keys())
key.sort()

for i in key:
  num = alphabet[i]
  print(i, "=>", num)

header

max_date = ''
max_temp = 0


for row in data:
  if row[2] == '':
    row[2] = -999
  row[2] = float(row[2])
  if row[2] > max_temp:
    max_temp = row[2]
    max_date = row[0]

print("가장 더웠던 날은 ",max_date,"이고 기온은 ", max_temp,"였다.",sep='')

max_temp = []
low_temp = []

import matplotlib.pyplot as plt
plt.rc('font',family = 'NanumGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize = (15,5)) #해상도
plt.title("Graph")
plt.xlabel("date")
plt.ylabel("temperature")

for row in data:
  if row[2] != '' and row[3] !='':
    if row[0].split('-')[1] == '08' and row[0].split('-')[2] == '15':
      max_temp.append(float(row[2]))
      low_temp.append(float(row[3]))

plt.plot(max_temp,color = 'red')
plt.plot(low_temp,color = 'blue')
plt.show()