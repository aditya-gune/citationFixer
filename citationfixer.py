import os, re

def fixCitations(a,path):
   
   newpath = path + '\\text.txt'
   print("Writing to ",newpath)
   tf = open(newpath, 'w+')
   
   '''pattern for single level tiling'''
   citpattern = '\.\\cite\{([a-zA-Z0-9,\s]*)\}'
   
   ctr = 0;
   regex = re.compile(r'\.\\cite\{([a-zA-Z0-9,\s]*)\}')
   finalstr = a
   for m in regex.finditer(a):
       
      found = m.group(0)
      cit = m.group(1)
      print(found)

      newstr = found.replace('.', '')
      newstr = newstr + '.'
      
      
      finalstr = finalstr.replace(found, newstr)
      ctr += 1
      print(ctr)
      print("\n-----\n")

   tf.write(finalstr)
   tf.close()
   
file = raw_input("Location of txt file?")
path = raw_input("Path to save to?")

with open(file, 'r') as f:
    content = f.read()
    fixCitations(content, path)
    
