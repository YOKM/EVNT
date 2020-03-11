import os
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import calendar


# re
##def GetThe_EventDate(EventDate_fromLog):
  #Date and Time:  2019-03-19 17:22:24.761162
 # YYYYmmDD = EventDate_fromLog.split(" ")[0]
 # EventDate = datetime.datetime.strftime(YYYYmmDD, "%Y-%m-%d")





def main():
    
    print ("CONVERSION PROCESS STARTED")

   
#1) Open a specified “analyse_log_” file (created as an output of analyse.py).
#1)
#2) Read each line of a specified “analyse_log_” file and identify the occurrence of
#the string “MATCHED Event ID:” Once identified, sanitise the line so that only
#the Event ID remains (i.e. an integer)
#3) Compare the sanitised Event ID, to your nested dictionary of Event IDs and
#iterate the appropriate dictionary count value, by 1.
#4) Once the process of assigning count values to the Event ID dictionary is
#complete, write each dictionary Event ID value and its associated count, to a
#log file.





Event_Date =[] # to hold the date of the event # will be useed to get the range for the Graph as heading

EventID_Dict = {
  1102 : 0,4611: 0,
  4985 : 0,
  4624 : 0,4634: 0,
  4648 : 0,4661: 0,
  4662 : 0,4663: 0,
  4672 : 0,4673: 0,
  4688 : 0,4698: 0,
  4699 : 0,4702: 0,
  4703 : 0,4719: 0,
  4732 : 0,4738: 0,
  4742 : 0,4776: 0,
  4798 : 0,4799: 0,
  4985 : 0,5136: 0,
  5140 : 0,5142: 0,
  5156 : 0,5158:0
}

DirName = "C:/temp/C15235_Logs/"



if __name__ == "__main__":
    main()




root = tk.Tk()
root.withdraw()
#1) Open a specified “analyse_log_” file (created as an output of analyse.py).
# OPEN THE ANALYSE LOG FROM OPEN DIALOG BOX
logPath_Analyse = filedialog.askopenfilename(initialdir = DirName,title = "OPEN ANALYSE LOG FILE")

print(logPath_Analyse)
with open (logPath_Analyse, "r") as fileHandler:
  for line in fileHandler:
      
      #Date and Time:  2019-03-19 17:22:24.761162
    if "Date and Time:" in line:
      #evt_Date = line.split(":  ")[1].split(' ')[0]
      Event_Date.append(line.split(":  ")[1].split(' ')[0]) # get event date from 
      #print(line.split(":  ")[1].split(' ')[0])
    if "MATCHED Event ID:" in line:
      #Event_Date.append(evt_Date) # if there match will then store the date the date is on the line prior to file source
      #print(line)
      IDNumber = line.split(':')[1].rstrip()
     # IdNum =("'" + IDNumber.replace(" ", "") + "'")
      IDNum = IDNumber.replace(" ", "")
     # print(IDNum)
      if int(IDNum) in EventID_Dict:
       # print("Event ID: " + str(EventID_Dict[int(IDNum)]))
      
        val = EventID_Dict[int(IDNum)]
        val +=1
        EventID_Dict[int(IDNum)] =  val
      #  print("Event Count: " +  str(EventID_Dict[int(IDNum)]))
      

          #break
      #3) Compare the sanitised Event ID, to your nested dictionary of Event IDs and
      #iterate the appropriate dictionary count value, by 1.
      #get value from the dictionary

#Event ID:1102
#Event Count:15
#Event ID:4611
#Event Count:2
#Event ID:4624
#Event Count:46


#4) Once the process of assigning count values to the Event ID dictionary is
#complete, write each dictionary Event ID value and its associated count, to a
#log file.
#5) Once the log file has been saved, open it and read each line.
#6) For each occurrence of an Event ID, append it to an Event ID list variable.
#7) For each occurrence of an Event IDs count value, append the count to an
#appropriately named list variable (e.g. EventIDCount)
#8) Use Matplotlib to create and display a horizontal bar graph, based on the list
#variables created in the last two steps.

# To write in log file.
#Event ID:1102
#Event Count:15
#Event ID:4611
#Event Count:2
#Event ID:4624
#Event Count:46

#1102 15
#4611 2

#• A log file of the scripts analysis activity should be created and saved in a folder
#called /home/user/ CI5235_KUNumber_FirstName/CI5235_logs/

# list of event
#sort date ASC
Event_Date.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
#print(Event_Date)
#res = [ Event_Date[0], Event_Date[-1] ]  #first item & last in the sort list 
#datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print("First Date : " + Event_Date[0])
#print("Month is : "+ str(datetime.strptime(Event_Date[0],"%Y-%m-%d")))
year_Start_num =  Event_Date[0].split("-")[0]
month_Start_num = Event_Date[0].split("-")[1]
MonthStart_name = calendar.month_name[int(month_Start_num)]
print(MonthStart_name)
#print (calendar.month_name[int(month)])

print("Last Date: " + Event_Date[-1])
#print (calendar.month_name[int(month)])
month_End_num = Event_Date[-1].split("-")[1]
year_End_num =  Event_Date[-1].split("-")[0]
MonthEnd_name = calendar.month_name[int(month_End_num)]
print(MonthEnd_name)
#print("Month is : "+ datetime.strptime(Event_Date[-1],"%Y-%m-%d").strftime("%B"))


print("Updated list with EventId and Count : ")
ts = time.time()
st = datetime.fromtimestamp(ts).strftime('%Y_%b_%a %H_%M_%S')
logfile_Name = "visdata_log_" + str(st)
for x, y in EventID_Dict.items():
 #print(x, y)

  print("Event ID:" + str(x))
  print("Event Count:" + str(y))
  #create the log
  #• The name of the log file should be “visdata_log_” concatenated with a timestamp.
  
  file_log = open(DirName + logfile_Name ,"a+") 
  file_log.write("Event ID:" + str(x) + "\n")
  file_log.write("Event Count:" + str(y) + "\n")
file_log.close()

#5) Once the log file has been saved, open it and read each line.
#6) For each occurrence of an Event ID, append it to an Event ID list variable.
#7) For each occurrence of an Event IDs count value, append the count to an
#appropriately named list variable (e.g. EventIDCount)

# create two list
#Event ID list
#EventIDCount
Event_ID_list = []
Event_IDCount_List = []
with open (DirName + logfile_Name, "r") as fileHandler:
  # Read each line in loop
  for line in fileHandler:
    # As each line (except last one) will contain new line character, so strip that
    if "Event ID" in line:
      #Event ID:4611 -> in Event_ID_list
      print("Get Event ID from line : " + line.split(":")[1])
      Event_ID_list.append(line.split(":")[1].rstrip()) 
    else:
      #Event Count:2 -> in Event_IDCount_List
      print("Get Count from line : " + line.split(":")[1])
      Event_IDCount_List.append(int(line.split(":")[1].rstrip()) )  
#rstrip() method strips all kinds of trailing whitespace by default,
#print the list which will be x and y axis
print('Event_ID_list list: ', Event_ID_list)
print('Event_ID_list list: ', Event_IDCount_List)

#now plot the graph

#8) Use Matplotlib to create and display a horizontal bar graph, based on the list
#variables created in the last two steps. 

# Initialize the plot
fig = plt.figure()
ax = fig.add_subplot()

ax.set_title('Event ID Counts ' + "(" + MonthStart_name +" "+ year_Start_num +" - " + MonthEnd_name +" "+ year_End_num+ ")")
#ax.set_yticklabels('Event ID Codes')
#ax.invert_yaxis()
ax.set_xlabel('Event Counts: ' )


ax.barh(Event_ID_list,Event_IDCount_List) # need to sort the list
#start, end = ax.get_xlim()
#ax.xaxis.set_ticks(np.arange(start, end, 20))
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%2d')) #%0.1f
#ax.tick_params(axis ='both', which ='both', length = 0) 
#ax.set_xticks([0,20,40,60,80,100])
plt.show()



#ax.barh(y_pos, performance, xerr=error, align='center')
#
#
#  # labels read top-to-bottom
#

      
#continue
      