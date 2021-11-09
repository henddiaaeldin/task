
#from urllib.request import urlopen
import json
import csv

#url = "https://raw.githubusercontent.com/russ666/all-countries-and-cities-json/master/countries.json"
#response = urlopen(url)
#data = json.loads(response.read())

f = open('countries.json' )

data = json.load(f)
filename = "country.csv"
csv_file = open(filename, "w")


writer = csv.writer(csv_file)


writer.writerow(["Country Name", "Number of cities", "City with max length"])
city=''
count=0
max1=0
tallestname=''
for i in data:
    max=0
    for j in data[i]:
        count+=1
        if len(j)>max:
            max = len(j)
            city=j
        if len(j)>max1:
            max1 = len(j)
            tallestname=j

    writer.writerow([i, len(data[i]), city])

print(count)
print(tallestname)
f.close()
csv_file.close()


