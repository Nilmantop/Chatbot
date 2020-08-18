import os
#chatbot by Nilmadhab Ghosh
print("say your name :")
name = input()
print(name + ' welcome to Nilmadhab Chatbot')
while True:
 print('hey please say me what you need :' , end = '' )
 i = input() 
 if (("run" in i) or ('open' in i) or ('start' in i)) and (("chrome" in i) or ("browser" in i)):
  os.system('chrome')
 elif (("connect"in i) or ("go" in i)) and ("web" in i):
  os.system('chrome')   
 elif (("start" in i) or ("open" in i)) and (("notepad" in i) or ("editor" in i)):
  os.system('notepad')
 elif (("start" in i) or ("open" in i)) and (("media" in i) or ("video" in i)):
  os.system('wmplayer')
 elif ("time" in i) or ("clock" in i):
    print('press enter to exit the clock,or you can set time')
    print(" do you understand: y/n ?")  
    ti = input()
    if str(ti) == 'y' :
       os.system('time')
    else:
       print("ok try next time") 
 elif((("open" in i) or ("go to" in i)) and ("control pannel" or "settings" in i)):
    os.system("control panel")
 elif("shutdown" in i):
    print("choose carefully shutdown = s,dont shutdown = type anything")
    sd = input()
    if str(sd) == 's':
       os.system('shutdown /s')
    else : 
       print('thank you')      
 elif ('exit' in i) or ('quit' in i):
  print('thanks from Nilmadhab Ghosh')
  break
 else:
  print('I did not get it')
  