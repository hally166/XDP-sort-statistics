# XDP sort statistics extractor

Copyright (c) 2017 Genome Research Ltd.

Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk

http://www.sanger.ac.uk/science/groups/cytometry-core-facility

The BD Influx has a very useful feature that automatically saves sort statistics for every run.  The XDP does not so if a user forgets to ask, loses their print out or we accidentally don't record the total events before the next sort, all the sort data is lost.  However the XDP does save this information on the server!  

This script will extract this data and present it as a text file containing the sort statistics for each run on a given day.

## CAUTION
The XDP server runs an unpatched, ancient version of Windows XP embedded.  Do not map or access the machine from a PC that is comprimised by a virus or trojan etc.  Use an up to date version of Windows and a virus scanner to secure your workstaion.

This script will automatically disconnect any drive mapped to the letter Z.  If you use this drive letter then change the drive letter used in the script before running it.  Change the mapping and unmapping lines.

## INSTRUCTIONS

https://youtu.be/NJc3PsUD434

Run the script from anywhere on the workstation and enter the date you want to recover using 2 digit desciptors.  i.e. 01

View the stats in the python window then close the window and you will see two files that contains the sort stats for that day in same folder as the script.

## TROUBLESHOOTING

There is a good chance that the time and date on the server is wrong.  Use Remote desktop connection, or the mouse and keyboard on the server to correct this.

The server saves the final sort results for each sort.  If you 'clear' the sort results, either from the console or in the software, before the sort finishes then only the results after the clearance will be shown. 

Plate sorts will show the final number of events ito the well.  The total events is the total events for the whole sort run.

The sort time is the time that the sort ended.

During morning drop delay set up we use 10x100 beads on a slide.  I have included a loop in the script to remove these "sorts".  If you do something different then please adjust this loop. You could also copy this loop to remove plate alignments or single cell sorts if you wish.

If the 'today's sort' feature is slow then you probably have a large number of sort log files.  Try going into the log folder and archiving the old ones.

The XDP server only has one spare USB slot. This means that one of your keyboard or mouse will need to be via an old connection using PS/2 (the purple/green round port). This is not a plug and play so you need your mouse or keyboard plugged in before you start the server.
