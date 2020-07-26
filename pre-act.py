
import sys
import os
import time

filename = 'interface.log'
name1 = 'interface_r.txt'
filename1 = 'port.txt'
name2 = 'port_r.txt'
name3 = 'port_fix.txt'
name4 = 'port_des.txt'
name5 = 'port_detail.txt'
import re
expression_to_use = r'172\d+$'
s = '-------------------------------------------------------------------------------'
e = '-------------------------------------------------------------------------------'
s1 = '-------------------------------------------------------------------------------'
e1 = 'Ports on Slot A'
wris = []
wris2 = []
fout = open(name1, "w")
fout1 = open(name2,"w")
fout2 = open(name3,"w")
router=[]
data=[]
pagar = "#" #IDLE STRING ON ROUTER
idleses= '~]$' #IDLE STRING ON SESSION
stop_port = ["show port","#"]
filename = 'router.txt' 
ceklist = 'ceklist.txt'
cm_ceklist = 'cm_ceklist.txt'
objTab = crt.GetScriptTab()
objTab.Screen.Synchronous = True


with open(filename, 'r') as input:
        for line in input:
        	router.append(line)
def send_com(x):
	crt.Screen.Send(x + "\r")
	crt.Screen.WaitForString(pagar)
	return
def start():

	crt.Dialog.MessageBox("SCRIPT BEFORE AFTER WITH MONITOR PORT & PING INTF"+"\n"+"Created By Ridho")
	username= crt.Dialog.Prompt("Input Username :")
	passwords= crt.Dialog.Prompt("Input Passwords :")
	for idx,i in enumerate(router):
		objTab.Screen.Clear()
		#Create File Name
		za = str(i)
		z0 = za.rstrip()+"_ceklist.log"
		z1 = za.rstrip()+".log"
		z2 = za.rstrip()+"_port.log"
		z3 = za.rstrip()+"_port_mentah.log"
		z5 = za.rstrip()+"_show_port.log"
		z4 = za.rstrip()+"_FULL.log"
		z6 = za.rstrip()+"_port_detail.log"
		z7 = za.rstrip()+"_interface.log"
		z8 = za.rstrip()+"_interface_r.log"
		z9 = za.rstrip()+"_interface_Fix.log"
		objTab.Screen.Send("\r")
		objTab.Screen.WaitForString(idleses)
		crt.Dialog.MessageBox(i)
		if idx == 0:
			objTab.Screen.Send("telnet "+ i)
		else:
			objTab.Screen.Send("telnet "+ i+"\n")
		objTab.Screen.WaitForString("ogin:")
		objTab.Screen.Send(username+"\r")
		objTab.Screen.WaitForString("assword:")
		objTab.Screen.Send(passwords+"\r")
		objTab.Screen.WaitForString(pagar)
		#prompt = prompt.strip()
		objTab.Session.LogFileName= z1
		send_com("environment no more")
		objTab.Session.Log(True)
		#szResult = objTab.Screen.ReadString(pagar)
		send_com("show port")
		time.sleep(5)
		objTab.Session.Log(False)
		objTab.Screen.Send("\r")
		objTab.Screen.WaitForString(pagar)
		objTab.Screen.Send("\r")
		objTab.Screen.WaitForString(pagar)
		objTab.Session.LogFileName= z7
		objTab.Session.Log(True)
		send_com("show router interface exclude-services")
		objTab.Session.Log(False)
		port(z1,z2)
		masukan_port(z2,z3,z5,z6)
		interface(z7,z8,z9)
		#objTab.Session.LogFileName= z4
		#objTab.Session.Log(True,False,True)
		objTab.Session.LogFileName= z0
		objTab.Session.Log(True)
		for line in open(z3,"r"):
			objTab.Screen.Send(line)
			objTab.Screen.WaitForString("\r")
			#time.sleep(2)
			#data.append(objTab.Screen.ReadString("#"))
		for line2 in open(z5,"r"):
			objTab.Screen.Send(line2)
			objTab.Screen.WaitForString("\r")
			#data.append(objTab.Screen.ReadString("\r"))
		for lin3 in open(cm_ceklist,"r"):
			objTab.Screen.Send(lin3)
			objTab.Screen.WaitForString("\r")
			#data.append(objTab.Screen.ReadString("\r"))
		#data.append("End Of Ceklist")
		objTab.Screen.Send("#--end\r")
		objTab.Screen.WaitForString("#--end")
		#port1 = open(z0,"w")
		#for line1 in data:
		#	if line1.isspace():
		#		break
		#	else:
		#		port1.writelines(line1)
		#	#objTab.Screen.WaitForString(pagar)
		#objTab.Screen.WaitForString("#")
		objTab.Screen.Send("#--end\r")
		objTab.Screen.WaitForString("#--end")
		objTab.Session.Log(False)
		objTab.Session.LogFileName= z4
		objTab.Session.Log(True)
		#port1.close() 
		objTab.Screen.Clear()
		for interface1 in open(z9,"r"):
			objTab.Screen.Send(interface1)
		for port_d in open(z6,"r"):
			send_com(port_d)
		#objTab.Session.LogFileName= z4
		#objTab.Session.Log(True,False,True)
		#objTab.Session.Log(True,True,True)
		objTab.Screen.Send("\r")
		objTab.Screen.WaitForString(pagar)
		objTab.Screen.Clear()
		
		send_com("show router interface exclude-services")
		send_com("show bof")
		send_com("show system information")
		send_com("show version")
		send_com("show chassis")
		send_com("show card state")
		send_com("show card detail")
		send_com("show mda detail")
		#time.sleep(10)
		#objTab.Session.Log(False,False,False)
		#objTab.Session.Log(True,False,True)
		objTab.Screen.Send("\r")
		objTab.Screen.WaitForString(pagar)
		#time.sleep(3)
		send_com("show port detail")
		send_com("show router interface")
		send_com("show router route-table summary")
		send_com("show router ospf neighbor")
		send_com("show router ospf interface")
		send_com("show router mpls status")
		send_com("show router mpls interface")
		send_com("show router mpls path")
		send_com("show router ldp status")
		objTab.Screen.Send("\r")
		objTab.Screen.WaitForString(pagar)
		#time.sleep(3)
		send_com("show router ldp interface")
		send_com("show router ldp session")
		send_com("show router rsvp interface")
		send_com("show router pim status")
		send_com("show router pim interface")
		send_com("show router pim group")
		send_com("show router igmp status")
		send_com("show router igmp interface")
		send_com("show router igmp group")
		send_com("show service service-using")
		objTab.Screen.Send("\r")
		objTab.Screen.WaitForString(pagar)
		#time.sleep(3)
		send_com("show log log-id 99")
		send_com("show log log-id 99 application chassis")
		send_com("show log log-id 99 application snmp")
		send_com("show log log-id 100")
		send_com("show log log-id 100 application chassis")
		send_com("show log log-id 100 application snmp")
		send_com("show service fdb-mac")
		send_com("show service service-using")
		send_com("show service service-using | match Down")
		send_com("show service service-using | match Down | count")
		send_com("show service sdp")
		send_com("show service sdp | match Down")
		send_com("show service sdp | match Down | count")
		send_com("show service sdp-using")
		send_com("show service sdp-using | match Down")
		send_com("show service sdp-using | match Down | count")
		send_com("show service sap-using")
		send_com("show service sap-using | match \"Up   Up\"")
		send_com("show service sap-using | match \"Up   Up\" | count")
		send_com("show service sap-using | match Down")
		send_com("show service sap-using | match Down | count")
		send_com("show service fdb-mac | match sap ")
		send_com("show service fdb-mac | match sap | count")
		send_com("/show service service-using | match Down")
		send_com("/show service sdp-using | match Down")

		objTab.Screen.Send("\r")
		objTab.Screen.WaitForString(pagar)
		#time.sleep(3)
		#objTab.Screen.Send("\r")
		#time.sleep(5)
		#szResult = objTab.Screen.ReadString("#")
		#crt.Dialog.MessageBox(szResult)
		#colIndex = objTab.Screen.CurrentColumn
		#crt.Dialog.MessageBox(prompt)
		#time.sleep(4)
		send_com("admin display-config")
		objTab.Screen.WaitForString("# Finished") 
		objTab.Screen.Send("logout")
		objTab.Session.Log(False)
		objTab.Screen.Send("\r")
		objTab.Screen.WaitForString('~]$')
		objTab.Screen.Send("\r")
		#objTab.Screen.Synchronous = False
		os.remove(z2)
		os.remove(z3)
		os.remove(z1)
		os.remove(z6)
		os.remove(z7)
		os.remove(z8)
		os.remove(z9)
		os.remove(z5)
#-----------------------------------------------------------------
#-----------------------------------------------------------------		
def CaptureOutputOfCommand(command, prompt):
	if not crt.Session.Connected:
		return "[ERROR: Not Connected.]"
	objTab.Screen.Send(command + '\r')
	objTab.Screen.WaitForString('\r')
	return objTab.Screen.ReadString(prompt)
def myfunc():
	with open(filename, 'r') as input:
   		for line in input:
   			if s in line:
   				line1 = s.splitlines()
   				for line1 in input:
					if e in line1:
						return
					else:
						return #fout.writelines(" ".join(line1.split()) + "\n")
def interface(output,output2,output3):
	wris=[]
	wris2=[]
	wris3=[]
	fout2 = open(output2,"w")
	with open(output, 'r') as input:
   		for line in input:
   			if s in line:
   				line1 = s.splitlines()
   				for line1 in input:
					if e in line1:
						break
					else:
						#print("HMMMM")
						fout2.writelines(" ".join(line1.split()) + "\n")
	wris = [w.replace('#--------------------------------------------------', '') for w in wris]
	#fout.writelines('/configure\n')
	#fout.writelines(wris)
	fout2.close()
	#fout1.close()
	with open(output2, "r") as input:
		for line in input:
			wris.append(line)
	result = [i for i in wris if i.startswith('172')]
	#print(result)

	with open(output2, "r") as input:
		fout3 = open(output3,"w")
		for line2 in input:
			#match=re.search(r"([0-9]\W+[0-9])", line2)
			#print(match)
			#match2 = re.findall(r"\d\d\d\W\d\d\W\d\S\S\S", line2)
			match1 = re.findall(r"\d\d\d\W\d\d\W\d\S\S\S\S*", line2)
			#print(match1)
			#print(match2)
			for intf in match1:
				if intf.isspace():
					break
				else:
					wris3.append("ping ")
					for idx,intf_i in enumerate(intf):
						if (intf[idx]) != "/":
							if intf[idx+1] == "/":
								if (int(intf_i) % 2) == 0:
									if int(intf_i) == 0:
										intf_i = "9"
									else:
										intf_i = int(intf_i) - 1 
									#print(intf_i)
								elif(int(intf_i)) + 1 ==10:
									intf_i = "0"
								elif int(intf_i) == 0:
									intf_i = "9"	
								else:
									intf_i = int(intf_i) + 1 
									#print(intf_i)
							if intf[idx+3] == "/":
								if ((intf[idx]).isdigit()) and (intf[idx+1].isdigit()) and (intf[idx+2].isdigit()):
									if (int(intf[idx+1]) + 1 == 10) and (int(intf[idx]) + 1 == 10) :
										intf_i = int(intf[idx])+1

							if intf[idx+2] == "/":
								if (intf[idx]).isdigit() and (intf[idx+1].isdigit()):
									if ((int(intf[idx]) + 1 == 10)) and (int(intf[idx+1]) + 1 == 10):
										intf_i = "0"
									elif (int(intf[idx])+1 != 10) and (int(intf[idx+1]) + 1 == 10) :
										intf_i = int(intf_i)+1
									elif (int(intf[idx])+1 == 0):
										intf_i = int(intf_i)-1
									elif (int(intf[idx+1]) == 0):
										intf_i = int(intf_i)-1
										#intf[idx+1]= '0'

							wris3.append(str(intf_i))
							
							#print(len(intf))
							#print(idx)
						else:
							wris3.append(" rapid count 1000 do-not-fragment\n")
							break

						#if intf_i.isdigit():
						#	if (int(intf_i) % 2) == 0:
						#		print("HEHE")
						#	else:
						#		print("HOHO")
	#print(wris3)	
	fout3.writelines("".join(wris3)+"\n")				#print(fout3)
	fout3.close()
	fout2.close()
def port(nama_log,output):
	fout1 = open(output,"w")
	with open(nama_log, 'r') as input:
   		for line in input:
   			if s1 in line:
   				line1 = s1.splitlines()
   				for line1 in input:
					if e1 in line1:
						return
					else:
						fout1.writelines(" ".join(line1.split()) + "\n")
	fout1.close()
def masukan_port(output,output2,output3,output4):
	with open(output, "r") as input:
		fout2 = open(output2,"w")
		fout3 = open(output3,"w")
		fout4 = open(output4,"w")
		for line2 in input:
			match=re.search(r"([0-9]\W+[0-9])", line2)
			#print(match)
			match1 = re.findall(r"\d\W\S\W[0-9]\S*", line2)
			match10 = re.findall(r"\d\d\W\d\W\d\W*", line2)
			for port_masuk in match1:
				if port_masuk.isspace() or port_masuk.startswith("0"):
					break
				else:
					fout2.writelines("monitor port "+"".join(port_masuk)+" rate interval 3 repeat 1 | match %\n")
			for port_des in match1:
				if port_des.isspace() or port_masuk.startswith("0"):
					break
				else:
					fout3.writelines("show port "+"".join(port_masuk)+" detail | match Description\n")
			for port_full in match1:
				if port_full.isspace() or port_masuk.startswith("0"):
					break
				else:
					fout4.writelines("show port "+"".join(port_full)+" detail\n")
			for port_masuk in match10:
				if port_masuk.isspace():
					break
				else:
					fout2.writelines("monitor port "+"".join(port_masuk)+" rate interval 3 repeat 1 | match %\n")
			for port_des in match10:
				if port_des.isspace():
					break
				else:
					fout3.writelines("show port "+"".join(port_masuk)+" detail | match Description\n")
			for port_full in match10:
				if port_full.isspace():
					break
				else:
					fout4.writelines("show port "+"".join(port_full)+" detail\n")
	fout2.close()
	fout3.close()
	fout4.close()

start()
