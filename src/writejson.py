import os
import json

#PJG 1/11/18 - CIA launched 

#Populate default arguments
ArgDefaults = {}
ArgDefaults["--mp"] = {'aliases':['--modpath'],'type':'str', 'dest':'modpath','default':'hi','help':'Explicit path to model data'}
ArgDefaults["--mns"] = {'aliases':['--modnames'],'type':'ast.literal_eval', 'dest':'modnames','default':'None','help':'A list of names that can be used to loop through modpath'}

# Write arguments json

if os.path.exists('../Defaults/DefArgsCIA.json'):
    print 'File existing, purging: DefArgsCIA.json'
    os.remove('../Defaults/DefArgsCIA.json')
fH = open('../Defaults/DefArgsCIA.json','w')

json.dump(ArgDefaults,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
fH.close()

