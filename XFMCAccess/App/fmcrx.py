import socket

import logging

import xfmc_decoder



class fmcsocket:
  def __init__(self,addr='0'):
    if addr=='0':
      self.UDP_IP = socket.gethostname()
    else:
      self.UDP_IP = addr
    
    self.UDP_PORT = 49010

    self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
  
    self.sock.bind(('192.168.0.91', self.UDP_PORT))
    self.sock.sendto('go', ('192.168.0.77', self.UDP_PORT))

  def get_data(self):
      xfmc_display = {}
      
      data, addr = self.sock.recvfrom(1024)
      xfmc_display = xfmc_decoder.decode(data)
      #print "received message:", data
      #logging.debug(data)
      
      
    
      return xfmc_display

  def close(self):
      self.sock.shutdown(socket.SHUT_RDWR)
      self.sock.close()
      
    
if __name__ == '__main__':

  fmc = fmcsocket()
  while True:
    xfmc_display = fmc.get_data()
    xfmc_decoder.test_print(xfmc_display)
    
    fmc.close()
