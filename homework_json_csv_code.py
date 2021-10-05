import json
import csv
import urllib.request
 
with urllib.request.urlopen('https://data.nasa.gov/resource/gh4g-9sfh.json') as url:
    json_data = json.load(url)
 
data_file = open('meteorite_landings.csv', 'w') #newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in json_data:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
 
data_file.close()