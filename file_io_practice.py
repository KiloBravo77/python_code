import csv
import sys

filename = "input_files\subscription_emails_1922.csv"

print 'Opening file ...'

try:
	infile = open(filename)
	print "Reading file ..."
except:
	print "Something went kaboom. Screw you, I'm outta here"
	exit()

PreviousLine = infile.readline()
PreviousLine = infile.readline()	#Read another line to skip the header row
PreviousLine = PreviousLine[:-1]
fields = PreviousLine.split('|')
PreviousPK = fields[0]
OutLine = fields[0] + "|" + fields[1] + "|" + fields[4]

for line in csv.reader(infile, delimiter = "|"):
	CurrentPK = line[0]
	
	if PreviousPK == CurrentPK:
		OutLine = OutLine + ";" + line[4]
	else:
		print OutLine
		with open('out.txt', 'a') as out:
			out.write(OutLine + '\n')
		OutLine = line[0] + "|" + line[1] + "|" + line[4]

	fields = line
	PreviousPK = CurrentPK