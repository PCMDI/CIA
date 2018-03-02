from __future__ import print_function
import os, sys
from cdp.cdp_parser import CDPParser

# CREATE THE PARSER OBJECT
P = CDPParser(None, [os.path.join(sys.prefix,"share","cia","DefArgsCIA.json")])

# WHICH PARAMETERS TO USE FROM THE INPUT PARAMETER FILE 
P.use("p")
P.use("diags")
P.use("mp")

#The first two parameters ("p" and "diags") must always be loaded as is.  In this example we also load up "modepath"

P.add_argument("--newarg",help="newarg help",default="newarg default")

# NOW, LOAD THE REQUESTED PARAMETERS
params = P.get_parameter()

print(params.newarg)
#print(params.newarg.help)
 
