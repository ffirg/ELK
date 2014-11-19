import random
import sys
import time

# The range for MSISDNs
startn=447900000000
endn=447999999999
count = 0

# Where we store our test output
file = 'c:\\temp\\hlr_migration.log'

# Need a couple of args
if len(sys.argv) == 1:
  print sys.argv[0] + " [number] [dd.mm.yyyy]"
  exit()

if len(sys.argv) == 3:
  number = int(sys.argv[1].strip())
  datestamp = str(sys.argv[2].strip())
else:
  print "Not enough args!"
  exit()

# Ask if we want to overwrite or append to existing output
mode = raw_input ("Overwrite (w) or Append (a)? ")

print "Let's do this!"

outfile = open(file, mode)
sys.stdout = outfile

# Do the biz!
while (count < number):
  if datestamp:
    print "%d,%s" % (random.randrange(startn, endn, +1) , datestamp)
  else:
    print "%d,%s" % (random.randrange(startn, endn, +1) , (time.strftime("%d.%m.%Y")))
  count = count + 1

outfile.close()