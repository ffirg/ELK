import easygui
import os

esprog="C:\Python27\esupdate.py"

options = easygui.buttonbox(msg='Select File', title='HLR Migration Logger', choices=('File', 'Quit'), image=None)

while True:
  if options == 'File':
    datafile = easygui.fileopenbox(msg="Select file", title="File Selection", default=None)
    break
  else:
	print "Bye."
	exit()
	
action = easygui.buttonbox(msg='Press Add or Delete', title='HLR Migration Logger', choices=('add', 'delete', 'Quit'), image=None)
if action == 'add':
  cmd = esprog + " --action=" + action +" -f " + datafile
  print cmd 
  os.system(cmd)
elif action == 'delete':
  cmd = esprog + " -f " + datafile
  print cmd
  os.system(cmd)
else:
  print "Bye."
  exit()