# Python script to add/delete ES documents for HLR Migration Logs

# args:
# index [optional, otherwise default=hlr] -i | --index
# action [optional, default=Delete ] -a | --action
# doc_type [optional, default=migration-log] -t | --type
# file [mandatory] -f | --file

# import modules
from elasticsearch import Elasticsearch
from datetime import datetime
import sys
import getopt

# Help/usage information
def call4help() :
  print ""
  print sys.argv[0] + " [ -i | --index=<index>] [ -t | --type=<document_type> [ -a | --action=<add|delete> ] -f | --file <file_to_load>]"
  print "Default action is to DELETE, filename is MANDATORY."
  sys.exit(0)

# ES create function
def ESAdd(ESindex, ESdoctype, msisdn, doc):
  es.index(index=ESindex, doc_type=ESdoctype, id=msisdn, body=doc)
  
# ES delete function
def ESDelete( ESindex, ESdoctype, msisdn):
  es.delete(index=ESindex, doc_type=ESdoctype, id=msisdn, ignore=[400, 404])

# Set some defaults like index, document and action types
ESindex='hlr'
ESdoctype='migration-log'
action='delete'
hlrdata=''

# If no args then barf...
if len(sys.argv) == 1:
  call4help()
 
# Parse cmd line args using getopts
options, remainder = getopt.getopt(sys.argv[1:], 'i:t:f:a:h', ['index=','doc_type=','file=','action=','help'])

for opt, arg in options:
  if opt in ('-i', '--index'):
    ESindex = arg
  elif opt in ('-t', '--type'):
    ESdoctype = arg
  elif opt in ('-f', '--file'):
    hlrdata = arg
  elif opt in ('-a', '--action'):
    action = arg
  elif opt in ('-h', '--help'):
    call4help()

# create connection to ES on localhost
es = Elasticsearch([
  {'host': 'localhost'},
])

# Parse log file and update/delete as appropriate
# Throw exception if problems
try:
	for line in open(hlrdata,'r').readlines():
		# need to ignore blank lines, else script will barf...
		if not line.strip():
		  continue
		else:
		  msisdn = line.strip().split(",")[0]
		  date = line.strip().split(",")[1]
		  # use REST API to add/delete doc entries
		  if action == 'add':
			doc = {
				'id': msisdn,
				'msisdn': msisdn,
				'migration_date': date
			}
			ESAdd(ESindex, ESdoctype, msisdn, doc)
		  else:
			ESDelete(ESindex, ESdoctype, msisdn)
except IOError:
	print "Could not open file %s" % hlrdata
	sys.exit(1)
