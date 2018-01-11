import os
import json


ArgDefaults = {}


ArgDefaults["--mp"] = {'type':'str', 'dest':'modpath','default':'hi','help':'Explicit path to model data'}

# Write json

if os.path.exists('../Tables/DefArgs.json'):
    print 'File existing, purging: DefArgs.json'
    os.remove('../Tables/DefArgs.json')
fH = open('../Tables/DefArgs.json','w')

json.dump(ArgDefaults,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
fH.close()

