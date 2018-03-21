from fdfgen import forge_fdf
import csv
import random
import os

# Read in first and last names
with open('CSV_Database_of_First_Names.csv', 'rU') as f:
    reader = csv.reader(f)
    fnlist = list(reader)

with open('CSV_Database_of_Last_Names.csv', 'rU') as f:
    reader = csv.reader(f)
    lnlist = list(reader)

with open('crimelist.csv', 'rb') as f:
    reader = csv.reader(f)
    crimelist = list(reader)

for i in range(0, 100):
    crime = crimelist[0][random.randint(0, len(crimelist))]
    day = random.randint(1, 29)
    month = random.randint(1, 13)
    year = random.randint(2000, 2018)
    hour = random.randint(0, 24)
    minute = random.randint(10, 60)
    fname = fnlist[random.randint(0, len(fnlist))][0]
    lname = lnlist[random.randint(0, len(lnlist))][0]

    date = str(month) + '-' + str(day) + '-' + str(year)
    time = str(hour) + ':' + str(minute)
    name = lname + ', ' + fname
    filename = 'gen/report' + str(i) + '.pdf'

    fields = [('OffenseType', crime),('Date', date),('Time', time),('InvolvedName1', name)]
    fdf = forge_fdf("",fields,[],[],[])
    fdf_file = open("data.fdf", "w")
    fdf_file.write(fdf)
    fdf_file.close()

    cmdstring = "pdftk report_template.pdf fill_form data.fdf output " + filename + " flatten"

    os.system(cmdstring)
    
'''
fields = [('OffenseType', 'Agressive Tickling'),('Date', '05-21-2015'),('Time', '8:45AM')]
fdf = forge_fdf("",fields,[],[],[])
fdf_file = open("pdfs/data.fdf","w")
fdf_file.write(fdf)
fdf_file.close()
'''

