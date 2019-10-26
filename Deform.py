# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:38:57 2016

@author: 510a
"""

import math

class Deform:
    """
    Define every deforming that we want here. The author created a method which can roll the plane lattice
    in order to make a paper roll.
    """
    pass

    def rolling(self, atom_list):
        """
        A rolling method which can roll a plane lattice to a paper roll.
        atom_list is the old list of coordinates (corresponds to plane lattice).
        This method will return the new list of coordinates.
        """
        ymax = max([row[1] for row in atom_list])
        zmax = max([row[2] for row in atom_list])
        
        new_atom_list = []
        for row in atom_list:
            # New y and z coordinates will form the circle at each cross section of paper roll, which
            # means that the axis of paper roll is new x = x.
            ynew = ((ymax+zmax)/math.pi)*math.sin(math.pi*row[1]/ymax)
            znew = ((-ymax-zmax)/math.pi)*math.cos(math.pi*row[1]/ymax)
            new_atom_list.append([row[0], ynew, znew])    

        """
        After checking symmetry, remove shift here

        z_list = [row[2] for row in new_atom_list]
        z_shift = (max(z_list)+min(z_list))/2
        for row in new_atom_list:
            row[2] -= z_shift
        """
        
        return new_atom_list

if __name__ == '__main__':
    
    #-------------- initialization ----------------#
    import Create
    xmax = 2
    ymax = 3

    create = Create.Create(xmax, ymax) # create plane lattice.
    deform = Deform()
    
    #-------------- print lattices ----------------#
    atom_list = create.trigonal()
    new_atom_list = deform.rolling(atom_list)
    print("lattice coord = {}\n".format(new_atom_list))
    
    #-------------- check symmetry ----------------#    
    y_list = [row[1] for row in new_atom_list]
    z_list = [row[2] for row in new_atom_list]

    y_shift = (max(y_list) + min(y_list))/2
    z_shift = (max(z_list) + min(z_list))/2

    print("Check the center of cross section: \n")
    print("y shift = "+str(y_shift))
    print("z shift = "+str(z_shift)+"\n")
