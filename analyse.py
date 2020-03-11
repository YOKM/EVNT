import os
import time
from datetime import datetime
def main():
    
    print ("CONVERSION PROCESS STARTED")

   


if __name__ == "__main__":
    main()

#An Event ID: 1, was found in file /home/user/CI5235_Coursework/evtx_logs/Persistence/persistence_sysmon_11_13_1_shime_appfix.xml
#No Match in Event ID List
#This event was created on: 2019-03-19 17:22:24.761162

#1) Search for xml files in the evtx_logs folder.
#2) For each xml file found, read each file line by line and search for a means to
#isolate an “Event ID”.
#3) Sanitise the Event ID line so that only the Event ID remains (i.e. an integer)
#4) Compare the sanitised Event ID found in each file, to values in the Event ID
#table below:

    #<EventID Qualifiers="16384">1003</EventID>
    #<TimeCreated SystemTime="2019-12-30 09:45:13.775417"></TimeCreated>


#log file

#A log file of the scripts analysis activity should be created and saved in a folder
#called /home/user/ CI5235_KUNumber_FirstName/CI5235_logs/
#• The name of the log file should be “analyse_log_” concatenated with a time
#stamp.

#    LOG DATE and TIME: 05_Jan_2020_13:20:45
#File Source: /home/user/CI5235_Coursework/evtx_logs/Persistence/persistence_sysmon_11_13_1_shime_appfix.xml
#NO MATCH For Event ID: 1
#Date and Time:  2019-03-19 17:22:24.761162

    
# create the log file

ts = time.time()
st = datetime.fromtimestamp(ts).strftime('%Y_%b_%a %H_%M_%S')

log_file = open("C:/temp/C15235_Logs/analyse_log_" + str(st),"w")
log_file.write("LOG DATE and TIME: " + str(st)+"\n")


EventID_Table = ["1102","4611","4624","4634","4648","4661","4662","4663","4672","4673","4688","4698","4699","4702","4703","4719","4732","4738","4742","4776","4798","4799","4985","5136","5140","5142","5156","5158"]
xml_Counter = 0
EventId_Counter = 0
MatchEventID_Counter = 0

directory = 'c:/temp/C15235_Logs/evtx_logs'

for filename in os.listdir(directory):
    fullfilename = directory+"/" + filename
    if fullfilename.endswith(".xml"):
        log_file.write("File Source: " + fullfilename +"\n")
        xml_Counter +=1
        # Open file 
        with open (fullfilename, "r") as fileHandler:
            # Read each line in loop
            for line in fileHandler:
                # As each line (except last one) will contain new line character, so strip that
                if "EventID" in line:
                    EventId_Counter +=1
                    EventId_line = line
                    IDNumber = EventId_line.split('>')[1].lstrip().split('<')[0]
                    print ("An Event ID: "+IDNumber+", was found in file "+fullfilename)
                    if IDNumber in EventID_Table :
                        MatchEventID_Counter +=1
                        #Matched in Event ID List
                        print ("Matched in Event ID List")
                        log_file.write("MATCHED Event ID: " + str(IDNumber)+"\n")
                    else:
                        print("No Match in Event ID List")
                        log_file.write("NO MATCH For Event ID: " + str(IDNumber)+"\n")
                if "TimeCreated" in line:
                    TimeCreated_line = line
                    Time = TimeCreated_line.split('"')[1].lstrip().split('"')[0]
                    print ("This event was created on: "+ str(Time))
                    log_file.write("#Date and Time:  " + str(Time)+"\n")
                   # print(line.strip())
 
        
        continue
    else:
        continue
            
                             
     #   MATCHED Event ID: 4662
#Date and Time:  2019-05-08 03:00:37.541178
     
      

print("ANALYSIS SUMMARY")
print(str(xml_Counter) +" log files analysed.")
print(str(EventId_Counter)+ " Event IDs found.")
print(str(MatchEventID_Counter) +" Event IDs matched in Event ID List.")

log_file.close()

# log file


#ANALYSIS SUMMARY
#166 log files analysed.
#4735 Event IDs found.
#480 Event IDs matched in Event ID List.
#This data has been logged in a file called: analysis_log_05_Jan_2020_13:20:45.txt



