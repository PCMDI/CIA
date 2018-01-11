# CIA

No, not that CIA.  This repository is used to maintain the Common Input Arguments (CIA) that are used for independently developed analysis used to evaluate General Circulation Models (GCMs) or Earth System Models (ESMs). 

Purpose:  Many modeling centers are interested in using multiple externally developed analysis packages.  They and other potential users will experience substantial benefit if these packages can be operated at least somewhat similiarly.  The common input options provided by the CIA offer a default or starting point which can easily be modified or appended as needed by specific capabilities.  

Maintainance: The CIA is maintained by a small team motivated to help advance the interoperability of different GCM/ESM analysis capabilities. When changes are agreed upon, they will be added to the python script (src) which will be run to update the defaults stored in a json file.  Version control will enable users to control how they adopt to modifications.  Anyone interested in contributing to the support of the CIA or wanting to register to recieve routine status updates should contact BLAH BLAH BLAH   

Targeted use:  We recommend users use the python argparse module to control how they drive their analysis systems.  The CIA is designed with the python argparse in mind, but it can readily be used with different utilites - the common syntax is the real reason for the CIA.

Capabilities currently collaborating with the CIA:

  PCMDI Metrics Package
  E3SM diagnostics package: https://acme-climate.github.io/acme_diags/docs/html/index.html
  ARM diagnostics package: https://github.com/ARM-DOE/arm-gcm-diagnostics
  Coming soon(?)...
  Regional Climate Model Evaluation System (RCMES): https://rcmes.jpl.nasa.gov/
  The Toolkit for Extreme Climate Analysis (TECA): https://github.com/LBL-EESA/TECA
  
  Collaborating modeling groups:
  
  
