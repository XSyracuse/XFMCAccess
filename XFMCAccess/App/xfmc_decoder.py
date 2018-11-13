

def dexfmc(x):
  r=x
  if x==30:
    r=159 # degree
  elif x>255:
    r=0  
  elif x==31:
    r=12 # box
  elif x>127:
    r=x-128
    
  return r
  
def decode_block(d):
  blk = {}
  arg = d.split(',')
 
  if len(arg)==1:
    try:
      blk['status'] = int(float(arg[0]))
    except ValueError:
      pass
      
  if len(arg) > 2:
    
    index_font = arg[0].split('/')
    index = index_font[0]
    
    ba = map(ord,arg[2])
    
    # determine small fonts used
    small = all(x>127 for x in ba)
    # convert
    ba = map(dexfmc,ba)
    
    txt = ''.join(map(chr,ba))
    
    #print small
    #print ba
    #print txt
    blk['page index'] = int(float(index))
    blk['x'] = int(float(arg[1]))
    blk['smallfont'] = small
    blk['text'] = txt
    
    #print blk
  return blk    

def decode(data):

  disp = {}
  i=1
  lines = data.split(chr(29))
  #print lines      
  for line in lines[1:]:
    #set up key
    disp_key = 'line{0}'.format(i)
    i=i+1
    disp[disp_key] = []
    
    #print line
    blocks = line.split(';')
    
    for b in blocks:
      dblk = decode_block(b)
      disp[disp_key].append(dblk)
    
  return disp
    
def test_print(fmc_display):
  print 'test 1 results'
  keys = ['line1','line2','line3','line4','line5','line6',
          'line7','line8','line9','line10','line11','line12',
          'line13','line14','line15','line16'
         ]
  
 
  for k in keys:
    try: 
      print k
      for b in fmc_display[k]:
        print b
      print
      
    except KeyError:
      print 'key not found %s' % k
 
if __name__ == '__main__':
  decode_block('65/0,80,Waypoint')

  s = 'MODEL'
  d = map(ord,s)

  print d
  d=map(lambda x:x+128,d)

  print d  
  d.append(31)
  
  t = ''.join(map(chr,d))
  decode_block('16/0,10,'+t)


  print
  print
  print
  print
  print

  z = 'XFMC'+chr(29)+'1/0,1,TYPE;1/0,16,;1/0,32,MODEL;1/0,48,,' + chr(29)+ '1/0,1,departure 41\'57\";1/0,20,;1/0,40,destination;1/0,0,'

  
  fmc_display = decode(z)

  
  test_print(fmc_display)

    
    
    
    
