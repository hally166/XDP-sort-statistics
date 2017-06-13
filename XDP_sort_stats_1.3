#Copyright (c) 2017 Genome Research Ltd.

#XDP sort statisitics extractor
#v1.3 Jun 2017
#Python 3.6 (2016)
#Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk

#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.


#This script opens a log file on the XDP server, extracts the sort statisitics and creats a new sort statisitic text file

#import dependancies
from os import path
import subprocess

#maps the XDP console server to the computer using Z as the drive letter
subprocess.call(r'net use Z: /del', shell=True)
subprocess.call(r'net use Z: \\192.168.0.1\Thor\Logs /user:XDP_Console password', shell=True)

#choose your date
print ("This script will produce a file named 'sortstats' in this directory\nwhich will give you the sort statistics for a particular day\n\nWhich day of the month do you want to look at\ni.e 01, 10, 31.")
day=input()
print ("Which month do you want to look at\ni.e 01 = jan, 09 = sept, 12 = dec.")
month=input()
print ("Which year do you want to look at\ni.e 17 = 2017.")
year=input()

#creates the filename and the path to the logfiles on the XDP
filename="RunStats "+month+"_"+day+"_"+year+".txt"
server= '\\\\192.168.0.1\\Thor\\Logs\\'
xdp_console_log = open(path.join (server,filename),'r')

#xdp_console_log=open(filename,'r')

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

#Disconnects the XDP server
subprocess.call(r'net use Z: /del', shell=True)

print ('\n\nA raw_statistics.txt file and a sort_statistics.csv file has been created\n\nPress enter to close' )
input()
