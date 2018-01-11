import os
import json


ArgDefaults = {}


ArgDefaults["--mp"] = {'type':'str', 'dest':'modpath','default':'hi','help':'Explicit path to model data'}

# Write json

if os.path.exists('../Defaults/DefArgsCIA.json'):
    print 'File existing, purging: DefArgsCIA.json'
    os.remove('../Defaults/DefArgsCIA.json')
fH = open('../Defaults/DefArgsCIA.json','w')

json.dump(ArgDefaults,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
fH.close()

