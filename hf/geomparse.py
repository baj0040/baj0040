import os
import numpy

xyz_file= os.path.join('./', 'water.xyz')
coords_mat= numpy.genfromtxt(fname=xyz_file, skip_header=2, dtype=('U2',float,float,float))
print(coords_mat)
