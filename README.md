# CIA

No, not that CIA.  This repository maintains the Common Input Arguments (CIA) that are used for independently developed analysis capabilities used to evaluate General Circulation Models (GCMs) or Earth System Models (ESMs). 

Many modeling centers are interested in using multiple externally developed analysis packages.  They and other potential users can experience substantial benefit if independently developed packages can be operated at least somewhat similiarly.  The common input options provided by the CIA offer a default or starting point which can easily be modified or appended as needed by specific capabilities.  

The CIA is overseen by a small team motivated to help advance the interoperability of different GCM/ESM analysis capabilities. When changes are agreed upon, they will be added to the defaults stored in a [JSON](json.org) file.  Version control will enable users to control how they adopt to modifications.  Anyone interested in contributing to the support of the CIA or wanting to register to recieve routine status updates should contact (*email listserv coming soon*).  The Climate-Forecast conventions (http://cfconventions.org/) are an example of what we aspire to accomplish with the CIA.    

We recommend use of the standard python *argparse* module to control input arguments.  The CIA is designed with the argparse in mind, however, it can readily be adopted to be used with different utilites.   Shared syntax is the objective.  How it gets used is determined by the user.  

For more information including examples and instructions, see https://github.com/PCMDI/CIA. 

Capabilities currently using and contributing to the CIA:

  + PCMDI Metrics Package: https://github.com/PCMDI/pcmdi_metrics
  + E3SM diagnostics package: https://acme-climate.github.io/acme_diags/docs/html/index.html
  + ARM diagnostics package: https://github.com/ARM-DOE/arm-gcm-diagnostics
  

  
