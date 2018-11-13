import logging

class FMSPage(object):
  def __init__(self,canvas):
    self.canvas = canvas
    self.leftline=[]
    self.rightline=[]
    
    
    self.line1 = []
    self.line2 = []
    self.line3 = []
    self.line4 = []
    self.line5 = []
    self.line6 = []
    self.line7 = []
    self.line8 = []
    self.line9 = []
    self.line10 = []
    self.line11 = []
    self.line12 = []
    
    self.upper = []
    self.scratch = []
    self.status = []
    
    self.lines=[]
    
    self.y = [50,65,80,95,
              110,125,140,155,
              170,185,200,210,
              20,230,4]
              
    self.y = map(lambda x:x+5,self.y)
    
    self.createLines()
    
  def createLines(self):
    print 'create fmc lines'
    
    #make five line parts each line
    for i in range(1):
      self.line1.append( self.canvas.create_text(50,self.y[0],fill='green',anchor='w',text='') )
      self.line2.append( self.canvas.create_text(50,self.y[1],fill='green',anchor='w',text='') )
      self.line3.append( self.canvas.create_text(50,self.y[2],fill='green',anchor='w',text='') )
      self.line4.append( self.canvas.create_text(50,self.y[3],fill='green',anchor='w',text='') )
      self.line5.append( self.canvas.create_text(50,self.y[4],fill='green',anchor='w',text='') )
      self.line6.append( self.canvas.create_text(50,self.y[5],fill='green',anchor='w',text='') )
      self.line7.append( self.canvas.create_text(50,self.y[6],fill='green',anchor='w',text='') )
      self.line8.append( self.canvas.create_text(50,self.y[7],fill='green',anchor='w',text='') )
      self.line9.append( self.canvas.create_text(50,self.y[8],fill='green',anchor='w',text='') )
      self.line10.append( self.canvas.create_text(50,self.y[9],fill='green',anchor='w',text='') )
      self.line11.append( self.canvas.create_text(50,self.y[10],fill='green',anchor='w',text='') )
      self.line12.append( self.canvas.create_text(50,self.y[11],fill='green',anchor='w',text='') )
    
    
    self.lines = [  
                    self.line1, self.line2, self.line3, self.line4, 
                    self.line5, self.line6, self.line7, self.line8, 
                    self.line9, self.line10, self.line11, self.line12,self.upper,self.scratch,self.status]
    
  def drawLines(self):
    '''
    self.leftline.append( self.canvas.create_text(50,self.y[0],fill='green',anchor='w',text='line0') )
    self.leftline.append( self.canvas.create_text(50,self.y[1],fill='green',anchor='w',text='line1') )
    self.leftline.append( self.canvas.create_text(50,self.y[2],fill='green',anchor='w',text='line2') )
    self.leftline.append( self.canvas.create_text(50,self.y[3],fill='green',anchor='w',text='line3') )
    self.leftline.append( self.canvas.create_text(50,self.y[4],fill='green',anchor='w',text='line4') )
    self.leftline.append( self.canvas.create_text(50,self.y[5],fill='green',anchor='w',text='line5') )
    self.leftline.append( self.canvas.create_text(50,self.y[6],fill='green',anchor='w',text='line6') )
    self.leftline.append( self.canvas.create_text(50,self.y[7],fill='green',anchor='w',text='line7') )
    self.leftline.append( self.canvas.create_text(50,self.y[8],fill='green',anchor='w',text='line8') )
    self.leftline.append( self.canvas.create_text(50,self.y[9],fill='green',anchor='w',text='line9') )
    self.leftline.append( self.canvas.create_text(50,self.y[10],fill='green',anchor='w',text='line10') )
    self.leftline.append( self.canvas.create_text(50,self.y[11],fill='green',anchor='w',text='line11') )
 
    self.rightline.append( self.canvas.create_text(300,70,fill='blue',anchor='e',text='line0') )
    self.rightline.append( self.canvas.create_text(300,80,fill='blue',anchor='e',text='line1') )
    self.rightline.append( self.canvas.create_text(300,95,fill='blue',anchor='e',text='line2') )
    self.rightline.append( self.canvas.create_text(300,105,fill='blue',anchor='e',text='line3') )
    self.rightline.append( self.canvas.create_text(300,123,fill='blue',anchor='e',text='line4') )
    self.rightline.append( self.canvas.create_text(300,133,fill='blue',anchor='e',text='line5') )
    self.rightline.append( self.canvas.create_text(300,152,fill='blue',anchor='e',text='line6') )
    self.rightline.append( self.canvas.create_text(300,162,fill='blue',anchor='e',text='line7') )
    self.rightline.append( self.canvas.create_text(300,182,fill='blue',anchor='e',text='line8') )
    self.rightline.append( self.canvas.create_text(300,192,fill='blue',anchor='e',text='line9') )
    self.rightline.append( self.canvas.create_text(300,210,fill='blue',anchor='e',text='line10') )
    self.rightline.append( self.canvas.create_text(300,220,fill='blue',anchor='e',text='line11') )
    '''
  def blank(self,line_number):
    #delete all canvas items in a line list
    for item in self.lines[line_number-1]:
      self.canvas.delete(item)
      
    #delete the list
    self.lines[line_number-1] = []
    
  def set_line(self,line_number,line_part,color,text,text_small=False,x=0):

    x=x*132
    x=x/100
    
    if text_small:
      f=("Helvetica", 9, "bold")
    else:
      f=("Helvetica", 12, "bold") 
   
    line = self.lines[line_number-1]
    
    try:
      self.lines[line_number-1].append(self.canvas.create_text(40+x,self.y[line_number-1],fill=color,anchor='w',text=text,font = f))
    except ValueError as err:
      logging.warning('ValueError in set_line: tried text: %s' % text)
      pass

  def handlebuttons(self,button):
    self.drawPage()
    return
    
  def scratchpad_available(self):
    return True
    
  def drawPage(self):
    #self.canvas.itemconfig(self.leftline[0],fill='blue',text='leftline0')
    return
    
  def set_left_line(self,line_number,color,text,text_small=False):
    if text_small:
      f=("Helvetica", 9, "bold")
    else:
      f=("Helvetica", 12, "bold") 
      
    self.canvas.itemconfig(self.leftline[line_number],fill=color,font=f,text=text)
    
  def set_right_line(self,line_number,color,text):
    self.canvas.itemconfig(self.rightline[line_number],fill=color,text=text)
    
  def get_leftline(self):
    return self.leftline
    
  def get_rightline(self):
    return self.rightline
    