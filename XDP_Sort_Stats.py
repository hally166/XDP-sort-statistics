#XDP sort statisitics extractor
#v1.4 Nov 2017
#Python 2.7 (2016)
#Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk
#License : GPLv3 https://www.gnu.org/licenses/gpl-3.0.html

#This script opens a log file on the XDP server, extracts the sort statisitics and creats a new sort statisitic text file

#import dependancies
from os import path
import subprocess
import glob

#maps the XDP console server to the computer using Z as the drive letter
subprocess.call(r'net use Z: /del', shell=True)
subprocess.call(r'net use Z: \\192.168.0.1\Thor\Logs /user:XDP_Console password', shell=True)
server= '\\\\192.168.0.1\\Thor\\Logs\\'

#today or another date?
print ("Do you want today's sort statistics?")
today=raw_input().lower()

if today.startswith('y'):
    filename = max(glob.iglob('\\\\192.168.0.1\\Thor\\Logs\\*.txt'), key=path.getctime)
    datename = filename.split(' ')
    date = str(datename[1])
    day = str(date.split('_')[1])
    month = str(date.split('_')[0])
    year = str(date.split('_')[2])
    year = str(year.split('.')[0])

else:
    #choose your date
    print ("This script will produce a file named 'sortstats' in this directory\nwhich will give you the sort statistics for a particular day\n\nWhich day of the month do you want to look at\ni.e 01, 10, 31.")
    day=raw_input()
    print ("Which month do you want to look at\ni.e 01 = jan, 09 = sept, 12 = dec.")
    month=raw_input()
    print ("Which year do you want to look at\ni.e 17 = 2017.")
    year=raw_input()
    filename="RunStats "+month+"_"+day+"_"+year+".txt"

#creates the filename and the path to the logfiles on the XDP
xdp_console_log = open(path.join (server,filename),'r')

#process the file
x=xdp_console_log.read()
y=str(x)
z=y.split('Run Statistics')
runs_count= y.count('Run Statistics')

#This removes all the pieces of the statistic file that are not related to sorting
sortlist=[]
for item in z:
   if 'Run Counts and Rates' in item:
        sortlist.append(item)

#This removes our drop delay calibration.  i.e. 100 drops per drop, change this to your specific scheme
editedlist=[]
for item in sortlist:
   if 'Sorted events: stream 2 events: 100' not in item:
        editedlist.append(item)

#Creats a new sort_statistics file in the directory that this script is contained in
sortfile = open('raw_statistics.txt', 'w')
for item in editedlist:
  sortfile.write("%s\n" % item)
sortfile.close()

#Displays the sort information in the python window
print('\n\n')
date=month+"/"+day+"/"+year
with open('raw_statistics.txt') as f:
	for line in f:
		if date in line:
			print (line,)
		if 'Total events processed' in line:
			print (line,)
		if 'Sorted events:' in line:
			print (line,)

#Disconnects the XDP server
subprocess.call(r'net use Z: /del /y', shell=True)

#Generates the csv file
date=month+"/"+day+"/"+year
stat_in=open('raw_statistics.txt','r')
file=open('sort_statistics.csv','w')
file.write('Date,End Time,Total Events,Sort Time (Mins),Sort mode: stream -2,Sort mode: stream -1,Sort mode: stream 1,Sort mode: stream 2,Sorted events: stream -2,Sorted events: stream -1,Sorted events: stream 1,Sorted events: stream 2,Soft aborts: stream -2,Soft aborts: stream -1,Soft aborts: stream 1,Soft aborts: stream 2\n' )
print('\n\n')
for line in stat_in:
    if date in line:
        tot=line.split()
        file.write(tot[0]+",") 
        file.write(tot[1]+",")
    if 'Total events processed' in line:
        tot=line.split()
        file.write(tot[3]+",")
    if 'Total time elapsed' in line:
        timel=line.split()
        tim=float(timel[3])/60000000
        tim=str(tim)
        file.write(tim +",")
    if 'Sort modes: stream -2' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[4]+",")
    if 'Sort modes: stream -1' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[4]+",")
    if 'Sort modes: stream 1' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[4]+",")
    if 'Sort modes: stream 2' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[4]+",")
    if 'Sorted events: stream -2' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[5]+",")
    if 'Sorted events: stream -1' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[5]+",")
    if 'Sorted events: stream 1' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[5]+",")
    if 'Sorted events: stream 2' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[5]+",")
    if 'Soft aborts: stream -2' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[4]+",")
    if 'Soft aborts: stream -1' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[4]+",")
    if 'Soft aborts: stream 1' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[4]+",")
    if 'Soft aborts: stream 2' in line:
        timel=line.split()
        tot=line.split()
        file.write(tot[4]+",\n")
file.close()
stat_in.close()

print ('\n\nA raw_statistics.txt file and a sort_statistics.csv file has been created\n\nPress enter to close' )
raw_input()
