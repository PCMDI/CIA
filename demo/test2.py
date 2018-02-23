import os, sys
from cdp.cdp_parser import CDPParser

P = CDPParser(None, [os.path.join(sys.prefix,"share","cia","DefArgsCIA.json"), "mydefs.json"])

P.use("p")
P.use("diags")
P.use("mp")
P.use("mp2")

P.add_argument("--crap",help = 'bla bla',default = 'bad')

P.add_argument("--modpath","--mp",dest = "modpath", default = 'shitze')


params = P.get_parameter()

print params.modpath
print params.modpath2
print params.crap
 
