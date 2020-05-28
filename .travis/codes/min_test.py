#import mdi

import os
import subprocess

working_dir = "../../user/engine_tests/test1"

os.system("cp -r " + str(working_dir) + " _work")
os.chdir("./_work")

engine_name = "/Users/tbarnes/Documents/mdi/lammps/src/lmp_mac"

#driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
#                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#engine_proc = subprocess.Popen([engine_name, "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"])
#engine_proc = subprocess.Popen([engine_name, "-in", "lammps.in",">","lammps.out"])
engine_proc = subprocess.Popen([engine_name, "-in", "lammps.in"])
#driver_tup = driver_proc.communicate()
engine_proc.communicate()

print("Hello World!")
