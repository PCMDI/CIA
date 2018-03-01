import argparse
import json
import os
import sys
import ast

p = argparse.ArgumentParser()

fjson = open(os.path.join(sys.prefix,"share","cia","DefArgsCIA.json"))
#fjson = open("../Defaults/DefArgsCIA.json")

json_data = json.load(fjson)

print "keys in dictionary are ", json_data.keys()

for key in json_data:
    if key[0]!='-': continue
    params = json_data[key]
    if "aliases" in params:
        option_strings = params.pop("aliases")
    else:
        option_strings = []
    option_strings.insert(0,key)
    params["type"] = eval(params.pop("type", "str"))
#   print 'key is ', key
    p.add_argument(*option_strings, **params)

args = p.parse_args(sys.argv[1:])

print "after modifications provided by command line arguments:", args


