# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:38:57 2016

@author: 510a
"""

import math

class Deform:
    
    pass

    def rolling(self, atom_list):
        
        ymax = max([row[1] for row in atom_list])
        zmax = max([row[2] for row in atom_list])
        
        new_atom_list = []
        for row in atom_list:
            
            ynew = ((ymax+zmax)/math.pi)*math.sin(math.pi*row[1]/ymax)
            znew = ((-ymax-zmax)/math.pi)*math.cos(math.pi*row[1]/ymax)
            new_atom_list.append([row[0],ynew,znew])    

        """After checking symmetry, remove shift here

        z_list = [row[2] for row in new_atom_list]
        z_shift = (max(z_list)+min(z_list))/2
        for row in new_atom_list:
            row[2] -= z_shift
        """
        
        return new_atom_list

if __name__ == '__main__':

    import Create

    create = Create.Create(2,3)
    deform = Deform()
    
    atom_list = create.trigonal()
    new_atom_list = deform.rolling(atom_list)
    
    y_list = [row[1] for row in new_atom_list]
    z_list = [row[2] for row in new_atom_list]

    y_shift = (max(y_list)+min(y_list))/2
    z_shift = (max(z_list)+min(z_list))/2

    print("Check of Symmetry: \n")
    print("y shift = "+str(y_shift))
    print("z shift = "+str(z_shift)+"\n")
