import socket

import logging

class fmckeypad:

  def __init__(self):
    UDP_IP = "192.168.0.77"
    UDP_PORT = 49011
    
    self.addr = (UDP_IP,UDP_PORT)
    self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
                     
  def key_entry(self,msg):
  
    self.sock.sendto(msg, self.addr)
    logging.debug(msg)
    
  def key_close(self):
  
    self.sock.close()
