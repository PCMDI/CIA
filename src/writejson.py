import os
import json

#PJG 1/11/18 - CIA launched 

#Populate default arguments
ArgDefaults = {}

ArgDefaults["--parameter"] = {'aliases':["-p"]}
ArgDefaults["--modpath"] = {'aliases':['--mp'],'type':'str', 'dest':'modpath','default':'hi','help':'Explicit path to model data'}
ArgDefaults["--modnames"] = {'aliases':['--mns'],'type':'ast.literal_eval', 'dest':'modnames','default':'None','help':'A list of names that can be used to loop through modpath'}

ArgDefaults["--results_dir"] = {'aliases':['--rd'],'type':'ast.literal_eval', 'default':'None','help':'The name of the folder where all runs will be stored.'}
ArgDefaults["--case_id"] = {'aliases':['--cid'],'dest':'modnames','default':'None','help':'The name of the subdirectory (below results_dir where results from a paritcular code execution is stored '}

ArgDefaults['--reference_data_path'] = {'aliases':['--rd'],'help':'The path/filename of reference (obs) data.'}

ArgDefaults['--test_data_path'] = {'aliases':['--tp'],'help':'The path/filename to model output.'}

ArgDefaults['--diags'] = {'aliases':["-d"],'help':"Path to other user-defined parameter file.","help":"Path to other user-defined parameter file.","type":"str","nargs":"+","required":False,"dest":"other_parameters"}

ArgDefaults['--num_workers'] = {'aliases':["-n"],'help':"Number of workers, used when running with multiprocessing or in distributed mode.","type":"int","required":False}

ArgDefaults['--scheduler_addr"'] = {'aliases':["--N/A"],'help':"Address of scheduler in the form of IP_ADDRESS:PORT. Used when running in distributed mode.","type":"str","required":False}


# Write arguments json

if os.path.exists('../Defaults/DefArgsCIA.json'):
    print 'File existing, purging: DefArgsCIA.json'
    os.remove('../Defaults/DefArgsCIA.json')
fH = open('../Defaults/DefArgsCIA.json','w')

json.dump(ArgDefaults,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
fH.close()



"""
        "--diags": {
                "aliases": ["-d"],
                "type": "str",
                "nargs": "+",
                "dest": "other_parameters",
                "default": [],
                "help": "Path to other user-defined parameter file.",
                "required": false
        },
        "--num_workers": {
                "aliases": ["-n"],
                "type": "int",
                "help": "Number of workers, used when running with multiprocessing or in distributed mode.",
                "required": false
        },
        "--scheduler_addr": {
                "type": "str",
                "help": "Address of scheduler in the form of IP_ADDRESS:PORT. Used when running in distributed mode."
        }
"""
