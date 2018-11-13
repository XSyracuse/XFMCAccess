"""
XFMCAccess.py

by MDF

Network link plugin for XFMC on X-Plane 10
Requires X-Plane Python plugin
Place into <X-Plane plugin folder>/PythonScript folder

"""
'''
from XPLMDefs import *
from XPLMMenus import *
from XPLMDataAccess import *
'''
# X-plane includes
from XPLMDefs import *
from XPLMProcessing import *
from XPLMDataAccess import *
from XPLMUtilities import *
from XPLMPlanes import *
from XPLMNavigation import *
from SandyBarbourUtilities import *
from PythonScriptMessaging import *
from XPLMPlugin import *
from XPLMMenus import *
from XPWidgetDefs import *
from XPWidgets import *
from XPStandardWidgets import *

import socket
import string 
import select

from EasyDref2 import *

UDP_IP = "192.168.128.60"
UDP_PORT = 49010
SEND_UDP_IP = "192.168.128.70"

class MCDU_Client:

        def __init__(self):
                self.xfmc_data = Data()
                # Create client socket
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.sock.bind((UDP_IP,UDP_PORT))
                         
                self.server_ip = UDP_IP
                self.server_port = 49011
                
                self.rsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.rsock.bind((self.server_ip,self.server_port))
                self.rsock.setblocking(0)
                
                self.button_q = []
                
        def get(self):
                self.xfmc_data.getData()
       
        def start_MCDU_Client(self):
                print '------------------------'
                print 'MCDU Access Client Start'
                print '------------------------'
 
                self.button_q = []
                self.sendData()
                
        def sendData(self):
                msg = self.xfmc_data.getData()
                self.sock.sendto(msg, (SEND_UDP_IP, UDP_PORT))
                
        def dequeuebutton(self):
                if len(self.button_q) > 0:
                        self.xfmc_data.buttonXFMC(self.button_q.pop(0))
          
        def MCDUrx(self):
       
                ready_to_read,ready_to_write,in_error = select.select([self.rsock],[],[],0)
                for s in ready_to_read:
                        received = s.recv(1024)
                        print received
                        keypath = received.split(':')
                        if len(keypath) > 1 and keypath[0] == 'KEY':
                                try:
                                        buttons = int(keypath[1]) 
                                        self.button_q.append(buttons)
                                except ValueError:
                                        pass
        
        def process(self):
                
                self.sendData()
                self.MCDUrx()
                self.dequeuebutton()
                

            
class BDref:
        def __init__(self,name,type,min,max):
        
                self.DataRef = XPLMFindDataRef(name)
                self.min = min
                self.max = max
                
        def get(self):
                TempArray = []
                count = XPLMGetDatab(self.DataRef, TempArray, self.min, self.max)
                return TempArray
        
class Data:
        def __init__(self):
            self.xfmc_up = False
            
 
        def getDataRef(self):
            self.version = EasyDref("xfmc/Version[0:79]","bit")
            
            if self.version != 0:
                self.xfmc_up = True
                # get datarefs 
                '''
                self.panel1   = EasyDref("xfmc/Panel_1[0:79]","bit")
                self.panel2   = EasyDref("xfmc/Panel_2[0:79]","bit")
                self.panel3   = EasyDref("xfmc/Panel_3[0:79]","bit")
                self.panel4   = EasyDref("xfmc/Panel_4[0:79]","bit")
                self.panel5   = EasyDref("xfmc/Panel_5[0:79]","bit")
                self.panel6   = EasyDref("xfmc/Panel_6[0:79]","bit")
                self.panel7   = EasyDref("xfmc/Panel_7[0:79]","bit")
                self.panel8   = EasyDref("xfmc/Panel_8[0:79]","bit")
                self.panel9   = EasyDref("xfmc/Panel_9[0:79]","bit")
                self.panel10  = EasyDref("xfmc/Panel_10[0:79]","bit")
                self.panel11  = EasyDref("xfmc/Panel_11[0:79]","bit")
                self.panel12  = EasyDref("xfmc/Panel_12[0:79]","bit")
                
                self.upper     = EasyDref("xfmc/Upper[0:79]","bit")
                self.scratch   = EasyDref("xfmc/Scratch[0:79]","bit")
                self.messages  = EasyDref("xfmc/Messages[0:79]","bit")
                '''
                self.panel1   = BDref("xfmc/Panel_1","bit",0,80)
                self.panel2   = BDref("xfmc/Panel_2","bit",0,80)
                self.panel3   = BDref("xfmc/Panel_3","bit",0,80)
                self.panel4   = BDref("xfmc/Panel_4","bit",0,80)
                self.panel5   = BDref("xfmc/Panel_5","bit",0,80)
                self.panel6   = BDref("xfmc/Panel_6","bit",0,80)
                self.panel7   = BDref("xfmc/Panel_7","bit",0,80)
                self.panel8   = BDref("xfmc/Panel_8","bit",0,80)
                self.panel9   = BDref("xfmc/Panel_9","bit",0,80)
                self.panel10  = BDref("xfmc/Panel_10","bit",0,80)
                self.panel11  = BDref("xfmc/Panel_11","bit",0,80)
                self.panel12  = BDref("xfmc/Panel_12","bit",0,80)
                
                self.upper     = BDref("xfmc/Upper","bit",0,80)
                self.scratch   = BDref("xfmc/Scratch","bit",0,80)
                self.messages  = BDref("xfmc/Messages","bit",0,80)
                
                self.status    = EasyDref("xfmc/Status","int")
                self.keypath   = EasyDref("xfmc/Keypath","int",False,True)
                
        def getData(self):
            if self.xfmc_up == False:
                self.getDataRef()
            
            tArray = ['none']
            delimiters = ("PAN1","PAN2","PAN3","PAN4",
                          "PAN5","PAN6","PAN7","PAN8",
                          "PAN9","PAN10","PAN11","PAN12",
                          "UPPER","SCRATCH","MSG","STATUS")
            
            r = 'XFMC'
            
            if self.xfmc_up == True:
            
                tArray = self.panel1.get()
                tArray.append(self.panel2.get()[0])
                tArray.append(self.panel3.get()[0])
                tArray.append(self.panel4.get()[0])
                tArray.append(self.panel5.get()[0])
                tArray.append(self.panel6.get()[0])
                tArray.append(self.panel7.get()[0])
                tArray.append(self.panel8.get()[0])
                tArray.append(self.panel9.get()[0])
                tArray.append(self.panel10.get()[0])
                tArray.append(self.panel11.get()[0])
                tArray.append(self.panel12.get()[0])
                tArray.append(self.upper.get()[0])
                tArray.append(self.scratch.get()[0])
                tArray.append(self.messages.get()[0])
                status = self.status.get()
                tArray.append('{0}'.format(status))
               
                #print tArray
                # make it a delimited packet string   
                for entry in tArray:
                        r = r + chr(29) + entry
                        #print entry
                        
            return r 

        def buttonXFMC(self,buttoncode):
                if self.xfmc_up == True:
                    self.keypath.set(buttoncode)
   
class PythonInterface:

        def XPluginStart(self):
                self.Name = "XFMCAccess"
                self.Sig =  "me/xfmcAccess"
                self.Desc = "XFMC to network"

                mySubMenuItem = XPLMAppendMenuItem(XPLMFindPluginsMenu(), "Python - Sim Data 1", 0, 1)
                self.MyMenuHandlerCB = self.MyMenuHandlerCallback
                self.myMenu = XPLMCreateMenu(self, "XFMC", XPLMFindPluginsMenu(), mySubMenuItem, self.MyMenuHandlerCB,    0)
                XPLMAppendMenuItem(self.myMenu, "Panel_1", -1000, 1)
               
                
                self.TailNumberDR = XPLMFindDataRef("sim/aircraft/view/acf_tailnum")
                
                
                self.mcdu_client = MCDU_Client()
                
                self.FlightLoopCB = self.FlightLoopCallback
                XPLMRegisterFlightLoopCallback(self, self.FlightLoopCB, 1.0, 0)
                
                return self.Name, self.Sig, self.Desc

        def XPluginStop(self):
                XPLMDestroyMenu(self, self.myMenu)
                
                EasyDref.cleanup()
                # Unregister the callback
                XPLMUnregisterFlightLoopCallback(self, self.FlightLoopCB, 0)

                pass

        def XPluginEnable(self):
                return 1

        def XPluginDisable(self):
                pass

        def XPluginReceiveMessage(self, inFromWho, inMessage, inParam):
        
                if inParam == XPLM_PLUGIN_XPLANE and inMessage == XPLM_MSG_AIRPORT_LOADED:
                        self.mcdu_client.start_MCDU_Client()
                        self.newAptLoaded = True
                elif inMessage == (0x8000000 | 8090)  and inParam == 1:
                        # inSimUpdater wants to shutdown
                        self.XPluginStop()

        
        def FlightLoopCallback(self, elapsedMe, elapsedSim, counter, refcon):
                # The actual callback.

                self.mcdu_client.process()

                # Return 0.1 to indicate that we want to be called again in 1/10 second.
                return 0.1

        
        def MyMenuHandlerCallback(self, inMenuRef, inItemRef):
                
                self.mcdu_client.sendData()
                
                        
                pass
