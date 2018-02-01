from __future__ import print_function
import os
import sys
import shutil

dest_dir = os.path.join(sys.prefix,"share","cia")

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

src = os.path.join("Defaults","DefArgsCIA.json")
dest = os.path.join(sys.prefix,"share","cia","DefArgsCIA.json")

print("copying {} to {}".format(src,dest))
shutil.copy(os.path.join("Defaults","DefArgsCIA.json"),os.path.join(sys.prefix,"share","cia","DefArgsCIA.json"))
