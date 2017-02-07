#XDP sort statistics extractor
Copyright (c) 2017 Genome Research Ltd.
Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk
http://www.sanger.ac.uk/science/groups/cytometry-core-facility

The BD Influx has a very useful feature that automatically saves sort statistics for every run.  The XDP does not and if a user forgets, loses a print out or we accidently clear the stats (especially the total events) all the sort data is lost.  However the XDP does save this information on the server!  This script will extract this data and present it as a text file containing the sort statistics for each run on a given day.

This script opens a log file on the XDP server, extracts the sort statisitics and creats a new sort statisitic text file

##CAUTION
The XDP server runs an unpatched, ancient version of Windows XP embedded.  Do not map or access the machine from a PC that is comprimised by a virus or trojan etc.  Use an up to date version of Windows and a virus scanner to secure your workstaion.

##INSTRUCTIONS
Map the 'Logs' folder on the server to the workstation.

In 'Windows Explore' click 'Tools' and 'Map Network Drive...'

Type in '\\192.168.0.1\Thor\Logs\'

username=.\XDP_console, password=password

Run the script from anywhere on the workstation and enter the date you want to recover using 2 digit names.  i.e. 01

The script will create a file that contains the sort stats for that day.

##TROUBLESHOOTING
The sort stats only includ the information of the sort decisions.  So if you do a single well plate then the stats will not show the whole plate, just one event.

The sort time is the time that the sorting ended.

During morning drop delay set up we use 10x100 beads on a slide.  I have included a loop in the script to remove these sorts.  If you do something different then please adjust this loop. You could also copy this loop to remove plate alignments or single cell sorts if you wish.

If the script cannot find the correct file you can look at the network share, copy the 'RunStats...' file to the same folder as the script the add # to the start of lines 27-29 and remove the # from line 31 and replace the RunStats... name in this line with the actual one from the server.

There is a good chance that the time and date on the server is wrong.  Use Remote desktop connection, or the mouse and keyboard on the server to correct this.

If you run the script and the network drive isn't mapped then it will hang.  It will give up and close eventually.

