# created an env using:

# RUN EXAMPLE
# conda create -n pmp_01_08_2018 pcmdi_metrics -c conda-forge -c pcmdi -c uvcdat -c uvcdat/label/v210
# > python using_Param_With_CDP_Without_CIAjson.py -p test_paramfile.py

# PJG & ZS 1/17/18

from pcmdi_metrics.pcmdi.pmp_parser import PMPParser

P = PMPParser()

params = P.get_parameter()

print params.mods
print params.modpath
 
