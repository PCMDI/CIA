import os
import json

#PJG 1/11/18 - CIA launched 

#Populate default arguments
ArgDefaults = {}

ArgDefaults["-p"] = {'aliases':["--parameter"]}
ArgDefaults["--mp"] = {'aliases':['--modpath'],'type':'str', 'dest':'modpath','default':'hi','help':'Explicit path to model data'}
ArgDefaults["--mns"] = {'aliases':['--modnames'],'type':'ast.literal_eval', 'dest':'modnames','default':'None','help':'A list of names that can be used to loop through modpath'}

ArgDefaults["--rd"] = {'aliases':['--results_dir'],'type':'ast.literal_eval', 'default':'None','help':'The name of the folder where all runs will be stored.'}
ArgDefaults["--cid"] = {'aliases':['--case_id'],'dest':'modnames','default':'None','help':'The name of the subdirectory (below results_dir where results from a paritcular code execution is stored '}

ArgDefaults['--rd'] = {'aliases':['--reference_data_path'],'help':'The path/filename of reference (obs) data.'}

ArgDefaults['--tdp'] = {'aliases':['--test_data_path'],'help':'The path/filename to model output.'}



# Write arguments json

if os.path.exists('../Defaults/DefArgsCIA.json'):
    print 'File existing, purging: DefArgsCIA.json'
    os.remove('../Defaults/DefArgsCIA.json')
fH = open('../Defaults/DefArgsCIA.json','w')

json.dump(ArgDefaults,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
fH.close()

