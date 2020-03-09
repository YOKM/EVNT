import os
import sys

import time
import pathlib
import glob



from os import path
from datetime import datetime
from time import process_time
from fnmatch import fnmatch



dirName = 'c:/temp/C15235_Logs/'
count_evtxfile = 0
count_folder = 0


print("A log file for this xml conversion session will be saved to a folder called 'CI5235_Logs'.")

#date time for file name for log
ts = time.time()
st = datetime.fromtimestamp(ts).strftime('%Y_%b_%a %H_%M_%S')
file = open(dirName + 'convert_log_'+ str(st), 'w+')

print(str(st))


#A log file of the script conversion activity should be created and saved in a folder called /home/user/ CI5235_KUNumber_FirstName/CI5235_logs
#• The name of the log file should be “convert_log_” concatenated with a time stamp.

def my_function(filepath):
  if os.path.exists(filepath):
    print(str(datetime.now()) + " file xml exist , please delete")
    yesno = input()
    if yesno == 'yes':
        os.remove(filepath)
        print(xmltoCheck + "File Removed!")
 
    
 


def main():
    
    print ("CONVERSION PROCESS STARTED")

   


if __name__ == "__main__":
    main()


start = time.time()#process_time()

    
if not os.path.exists(dirName):
     os.makedirs(folder_create)
 
#delte all xml 
for dirpath, dirnames, filenames in os.walk(dirName):
    for file in filenames:
        if fnmatch(file, '*.xml'):
            os.remove(os.path.join(dirpath, file))

for (dirpath, dirnames, filenames) in os.walk(dirName):
    
    for dir in dirnames:
        count_folder +=1
        print("")
        print(str(count_folder) +": Working in the " + dir)
        subfolder = os.path.join(dirName, dir)
        for (dirpath, dirnames, filenames) in os.walk(subfolder):
            for file in filenames:
                count_evtxfile +=1
                xmltoCheck = subfolder +'/' + file.replace("evtx", "xml")
                #my_function(xmltoCheck)  --delete XML not working
                #Convert tunna_iis_rdp_smb_tunneling_sysmon_3.evtx from evtx to xml format, started...
                print("Convert " + os.path.basename(file) +" from evtx to xml format, started...")
                arg = "python ./evtx_dump.py " + (subfolder + '\\'+file).replace('\\', '/') + " > " + (xmltoCheck).replace('\\', '/')
                print(arg)
                os.system(arg)
                print("Converted successfully!")
            
               
end = time.time() #process_time()               
                
               
                


print("")
print("")
print("SUMMARY OF CONVERSION PROCESS!")
print("Folder Count: " + str(count_folder))
print("File Count: " + str(count_evtxfile))

hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("The time to complete this conversion was: " + "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds) + " seconds")




#start = time.time()
#end = time.time()
#hours, rem = divmod(end-start, 3600)
#minutes, seconds = divmod(rem, 60)
#print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))


#SUMMARY OF CONVERSION PROCESS!
#Folder Count: 10
#File Count: 166

#The time to complete this conversion was: 0:00:40
    

 
        

         



