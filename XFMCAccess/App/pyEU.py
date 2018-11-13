from Tkinter import *
import tkMessageBox
import pyFMSPage
import pyRMUPage
import threading
import time

import logging

import fmcrx
import keypad

UDP_IP = '192.168.0.77'

def on_closing():
  n.signalClosing()
  root.destroy()
  
def callback():
  if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
    root.destroy()
  
def onClickArea(event,tag):
  print 'click'
  print tag
  
def click(event):
  global current_page

  
  global m1
  w.delete(m1)
  txt='{0} {1}'.format(event.x,event.y)  
  m1=w.create_text(50,30,fill='red',anchor='w',text=txt)
  
  tag,meta = findHotSpot(event.x,event.y)
 
  logging.debug(tag,meta)
  
  displayAN(tag,meta)
  

def displayAN(tag,meta={}):
  if True:
    try:
      print meta
      xk = meta['xfmc']
      msg = 'KEY:%d' % xk
      logging.debug(msg)
      k.key_entry(msg)
    except KeyError:
      print '***'
      pass


hotspot = []
def addHotSpot(x1,y1,x2,y2,tag,meta={}):
  hotspot.append([x1,y1, x2, y2,tag,meta]) 

def findHotSpot(x,y):
  for h in hotspot:
    if x>h[0] and x<h[2] and y>h[1] and y<h[3]:
      tag = h[4]
      meta = h[5]
      break
    else:
      tag = ''
      meta = {}
  return tag,meta
  
def EXEC_lamp_yellow():
  w.create_rectangle(286, 310, 311, 317, fill="yellow",outline='lightYellow',tag='EXEC_lamp')
  
def EXEC_lamp_green():
  w.create_rectangle(286, 310, 311, 317, fill="green",outline='lightGreen',tag='EXEC_lamp')
 
def EXEC_lamp_black():
  w.create_rectangle(286, 310, 311, 317, fill="black",outline='black',tag='EXEC_lamp')
 
root=Tk()

root.title("FMC")

w = Canvas(root, width=360, height=557)

img = PhotoImage(file="fmc.gif")

w.create_image((180, 278),image=  img)

'''
oval = w.create_oval(50,50,60,60,fill="white")
w.create_oval(60,50,70,60,fill="red")
w.create_oval(70,50,80,60,fill="blue")
'''

click_area = w.create_rectangle(153,337,172,357,fill='',outline='lightBlue')

m1 = w.create_text(50,125,fill='red',anchor='w',text='')
# m2 = w.create_text(50,210,fill='green',anchor='w',text='')


addHotSpot(153,337,172,357,'A',{'xfmc':27})
addHotSpot(187,337,207,357,'B',{'xfmc':28})
addHotSpot(224,337,244,357,'C',{'xfmc':29})
addHotSpot(260,337,280,357,'D',{'xfmc':30})
addHotSpot(294,337,314,357,'E',{'xfmc':31})

addHotSpot(153,373,172,393,'F',{'xfmc':32})
addHotSpot(187,373,207,393,'G',{'xfmc':33})
addHotSpot(224,373,244,393,'H',{'xfmc':34})
addHotSpot(260,373,280,393,'I',{'xfmc':35})
addHotSpot(294,373,314,393,'J',{'xfmc':36})

addHotSpot(153,407,172,427,'K',{'xfmc':37})
addHotSpot(187,407,207,427,'L',{'xfmc':38})
addHotSpot(224,407,244,427,'M',{'xfmc':39})
addHotSpot(260,407,280,427,'N',{'xfmc':40})
addHotSpot(294,407,314,427,'O',{'xfmc':41})

addHotSpot(153,442,172,462,'P',{'xfmc':42})
addHotSpot(187,442,207,462,'Q',{'xfmc':43})
addHotSpot(224,442,244,462,'R',{'xfmc':44})
addHotSpot(260,442,280,462,'S',{'xfmc':45})
addHotSpot(294,442,314,462,'T',{'xfmc':46})

addHotSpot(153,476,172,496,'U',{'xfmc':47})
addHotSpot(187,476,207,496,'V',{'xfmc':48})
addHotSpot(224,476,244,496,'W',{'xfmc':49})
addHotSpot(260,476,280,496,'X',{'xfmc':50})
addHotSpot(294,476,314,496,'Y',{'xfmc':51})

addHotSpot(153,511,172,531,'Z',{'xfmc':52})

addHotSpot(187,511,207,531,['OP','SP'],{'xfmc':53})
addHotSpot(224,511,244,531,['OP','DEL'],{'xfmc':54})
addHotSpot(260,511,280,531,'/'         ,{'xfmc':55})
addHotSpot(294,511,314,531,['OP','CLR'],{'xfmc':56})

addHotSpot( 45,406,69,429,['NUM','1'],{'xfmc':57})
addHotSpot( 81,406,105,429,['NUM','2'],{'xfmc':58})
addHotSpot(116,406,141,429,['NUM','3'],{'xfmc':59})

addHotSpot( 45,439,69,464,['NUM','4'],{'xfmc':60})
addHotSpot( 81,439,105,464,['NUM','5'],{'xfmc':61})
addHotSpot(116,439,141,464,['NUM','6'],{'xfmc':62})

addHotSpot( 45,476,69,498,['NUM','7'],{'xfmc':63})
addHotSpot( 81,476,105,498,['NUM','8'],{'xfmc':64})
addHotSpot(116,476,141,498,['NUM','9'],{'xfmc':65})

addHotSpot( 45,510,69,533,['NUM','.'],{'xfmc':66})
addHotSpot( 81,510,105,533,['NUM','0'],{'xfmc':67})
addHotSpot(116,510,141,533,['NUM','-'],{'xfmc':68})

addHotSpot(7,63,24,78,  ['OP','LSK1'],{'xfmc':0})
addHotSpot(7,92,24,106, ['OP','LSK2'],{'xfmc':1})
addHotSpot(7,121,24,134,['OP','LSK3'],{'xfmc':2})
addHotSpot(7,149,24,163,['OP','LSK4'],{'xfmc':3})
addHotSpot(7,178,24,193,['OP','LSK5'],{'xfmc':4})
addHotSpot(7,207,24,220,['OP','LSK6'],{'xfmc':5})

addHotSpot(336,63,354,78,  ['OP','RSK1'],{'xfmc':6})
addHotSpot(336,92,354,106, ['OP','RSK2'],{'xfmc':7})
addHotSpot(336,121,354,134,['OP','RSK3'],{'xfmc':8})
addHotSpot(336,149,354,163,['OP','RSK4'],{'xfmc':9})
addHotSpot(336,178,354,193,['OP','RSK5'],{'xfmc':10})
addHotSpot(336,207,354,220,['OP','RSK6'],{'xfmc':11})

addHotSpot(49,265,79,286,  ['OP','INITREF'],{'xfmc':12})
addHotSpot(94,265,125,286, ['OP','RTE'],{'xfmc':13})
addHotSpot(139,265,172,286,['OP','DEPARR'],{'xfmc':14})
addHotSpot(185,265,218,286,['OP','ATC'],{'xfmc':15})
addHotSpot(230,265,264,286,['OP','VNAV'],{'xfmc':16})

addHotSpot(49,298,79,321,  ['OP','FIX'],{'xfmc':17})
addHotSpot(94,298,125,321, ['OP','LEGS'],{'xfmc':18})
addHotSpot(139,298,172,321,['OP','HOLD'],{'xfmc':19})
addHotSpot(185,298,218,321,['OP','FMCCOMM'],{'xfmc':20})
addHotSpot(230,298,264,321,['OP','PROG'],{'xfmc':21})
addHotSpot(282,298,314,321,['OP','EXEC'],{'xfmc':22})

addHotSpot(49,335,79,357,  ['OP','MENU']),{'xfmc':23}
addHotSpot(94,335,125,357, ['OP','NAVRAD'],{'xfmc':24})

addHotSpot(49,371,79,391,  ['OP','PREVPAGE'],{'xfmc':25})
addHotSpot(94,371,125,391, ['OP','NEXTPAGE'],{'xfmc':26})


EXEC_lamp_green();
init_page = pyFMSPage.FMSPage(w)

current_page = init_page
current_page.drawLines()



w.pack()


for i in range(1,12,2):
  current_page.set_line(i,1,'orange','DESCRIPTION',True)
  current_page.set_line(i+1,1,'red','VALUE')


#root.protocol("WM_DELETE_WINDOW", callback)
root.bind("<Button-1>",click)

class netz:
  def __init__(self,r):

    self.rootz = r
    self.xfmc_display = {}
    self.die = threading.Event()
    self.lock = threading.Lock()
    self.netClientThread = False

    self.fmcsock = fmcrx.fmcsocket(UDP_IP)
    
    self.die.clear()
    if not self.netClientThread:
       self.netClientThread = threading.Thread(target=self.netClient)
       self.netClientThread.start()
       
  def update_timer(self):
    #print '&'
    self.fmcdraw()
    #why lock not acq?
    if self.lock.acquire(False):
      self.fmcdraw()
      self.lock.release()
      
    self.rootz.after(100,self.update_timer)
    
  def signalClosing(self):
    self.die.set()
    self.fmcsock.close()
    self.netClientThread.join(5)
    
  ###### in thread #####
  def netClient(self):
    while not self.die.isSet():
      self.network()

  def network(self):
    self.lock.acquire()
    self.xfmc_display = self.fmcsock.get_data()
    self.lock.release()
  ###### thread #####
    
  def fmcdraw(self):
    #shall run in root thread
    #print xfmc_display
    
    keys = ['line2','line1','line4','line3','line6','line5',
          'line8','line7','line10','line9','line12','line11', 'line13','line14','line15']
   
    i = 0
    
    #print 'Go thru keys'
    for k in keys:
      try: 
     
        i=i+1
        current_page.blank(i)
 
        for b in self.xfmc_display[k]:
         
          if len(b)>0:
            
            try:
              color = 'orange'
              #adjust based on line_number  
              if i == 14:
                b['x']=25
                b['smallfont']=False
                color='yellow'
              if i == 15:
                b['x']=25
                b['smallfont']=True
                color = 'red'
              current_page.set_line(i,0,color,b['text'],b['smallfont'], b['x'])  
            except KeyError:
              pass
            


      except KeyError:
        print 'key not found %s' % k

    try:
      b=self.xfmc_display['line16']
      s=b[0] #get first list
      status = s['status']
      if status & 32:
        print 'exec on'
        EXEC_lamp_green()
      else:  
        EXEC_lamp_black()
 
    except KeyError:
      pass

 
logging.basicConfig(filename='debug.log',level=logging.DEBUG)
n = netz(root)
k = keypad.fmckeypad()
n.update_timer()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
