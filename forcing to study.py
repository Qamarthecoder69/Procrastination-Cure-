import time,os
start_time_file=open(f"C:\\Users\\{os.getlogin()}\\Documents\\starttime.txt","rt")
end_time_file=open(f"C:\\Users\\{os.getlogin()}\\Documents\\endtime.txt","rt")

# INPUT THE START TIME
User_Start_Time=start_time_file.read()
# #     int(input("Enter The Start of Study Session(Time)\n"))
# # User_Start_Time_FORMAT=int(input("Enter The Start of Study Session(AM OR PM)\n"))
#
# # INPUT THE END TIME
User_End_Time=end_time_file.read()
# # int(input("Enter The END of Study Session(Time)\n"))
# # User_End_Time_FORMAT=int(input("Enter The Start of Study Session(AM OR PM)\n"))
while True:
    current_time = time.strftime("%I:%M %p")
    while str(current_time) >= User_Start_Time and str(current_time) <= User_End_Time:
        os.system("shutdown /s /t 0")

