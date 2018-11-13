import pyFMSPage 

class RMUPage(pyFMSPage.FMSPage):

  def __init__(self,canvas,rt,leftline,rightline):
    self.canvas = canvas
    self.rt = rt
    self.leftline=leftline
    self.rightline=rightline
 
  def drawLines(self):
    self.set_left_line(0,'white',self.rt.get_com1())
    self.set_left_line(1,'green',self.rt.get_com1_())
    self.set_right_line(0,'green',self.rt.get_com2())


class RadioTracker(object):
  def __init__(self):
    self.com1 = 122.8
    self.com1_ = 118.0
    self.com2 = 118.0
    self.com2_ = 120.0
    
    self.transponder = 2200
    self.transpondermode = 'OFF'
    
  def transfer_com1(self):
    x = self.com1
    self.com1 = self.com1_
    self.com1_ = x
    
  def transfer_com2(self):
    x = self.com2
    self.com2 = self.com1_
    self.com2_ = x
    
  def set_com1_(self,f):
    self.com1_ = f
    
  def set_com2_(self,f):
    self.com2_ = f
   
  def get_com1(self):
    return self.com1
    
  def get_com1_(self):
    return self.com1_
    
  def get_com2(self):
    return self.com2
    
  def get_com2_(self):
    return self.com2_
 
  def set_transponder(self,code):
    self.transponder = code
  def get_transponder(self):
    return self.transponder
    
    