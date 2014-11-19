# Python script to delete ES documents for HLR Migration Logs

# import modules
from elasticsearch import Elasticsearch
from datetime import datetime
import sys
import json
import os 
from io import StringIO

file = 'c:\\temp\\output.txt'
#dfile = open('c:\\temp\\pydebug.txt','a') 
lines = sys.stdin.readline().splitlines() 


myjson = [json.loads(line)["msisdn"] for line in lines]
	
outfile = open(file, 'a')
sys.stdout.flush()
sys.stdout = outfile
print myjson
outfile.close()

