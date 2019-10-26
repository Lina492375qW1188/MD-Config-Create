# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:07:23 2016

@author: Lina492375qW1188
"""

class Construct:
    """
    This class is only used for constructing LAMMPS configuration file.
    """
    def __init__(self, infile):

        self.infile = infile # must be a string.

    def output1(self, atom_list):
        """
        This method creates only atoms with their coordinates.
        """
        f = open(self.infile, 'w')
        
        f.write('LAMMPS data file, version 2016-ICMS, timestep = unkown\n\n')
        
        f.write("{} atoms\n\n".format(len(atom_list)))
        
        f.write('1 atom types\n\n')
        
        x_list = [row[0] for row in atom_list]
        y_list = [row[1] for row in atom_list]
        z_list = [row[2] for row in atom_list]
        
        f.write("{} {} xlo xhi\n".format(min(x_list)-5, max(x_list)+5))
        f.write("{} {} ylo yhi\n".format(min(y_list)-5, max(y_list)+5))
        f.write("{} {} zlo zhi\n\n".format(min(z_list)-5, max(z_list)+5))
        
        f.write('Masses\n\n1 10.0\n')
        
        f.write("\nAtoms\n\n")
        i = 0
        for item in atom_list:
            i += 1
            f.write("{} 0 1 {} {} {}\n".format(i, item[0], item[1], item[2]))
        
        f.close()
       
    def output2(self, atom_list, bond_list):
        """
        This method creates atoms with their coordinates and bonds with the pair of indices.
        """
        f = open(self.infile, 'w')
        
        f.write('LAMMPS data file, version 2016-ICMS, timestep = unkown\n\n')
        
        f.write("{} atoms\n\n".format(len(atom_list)))
        f.write("{} bonds\n\n".format(len(bond_list)))
        
        f.write('1 atom types\n')
        f.write('1 bond types\n\n')
        
        x_list = [row[0] for row in atom_list]
        y_list = [row[1] for row in atom_list]
        z_list = [row[2] for row in atom_list]
        
        f.write("{} {} xlo xhi\n".format(min(x_list)-5, max(x_list)+5))
        f.write("{} {} ylo yhi\n".format(min(y_list)-5, max(y_list)+5))
        f.write("{} {} zlo zhi\n\n".format(min(z_list)-5, max(z_list)+5))
        
        f.write('Masses\n\n1 10.0\n')
        
        f.write("\nAtoms\n\n")
        i = 0
        for item in atom_list:
            i += 1
            f.write("{} 0 1 {} {} {}\n".format(i, item[0], item[1], item[2]))
        
        f.write("\nBonds\n\n")
        j = 0
        for item in bond_list:
            j += 1
            f.write("{} 1 {} {}\n".format(j, item[0]+1, item[1]+1))
            
        f.close()

    def output3(self, atom_list, bond_list, angle_list):
        """
        This method creates a complete configuration file with atomic positions, bonds and angles.
        """
        f = open(self.infile, 'w')
        
        f.write('LAMMPS data file, version 2016-ICMS, timestep = unkown\n\n')
        
        f.write("{} atoms\n\n".format(len(atom_list)))
        f.write("{} bonds\n\n".format(len(bond_list)))
        f.write("{} angles\n\n".format(len(angle_list)))
        
        f.write('1 atom types\n')
        f.write('1 bond types\n')
        f.write('1 angle types\n\n')
        
        x_list = [row[0] for row in atom_list]
        y_list = [row[1] for row in atom_list]
        z_list = [row[2] for row in atom_list]
        
        f.write("{} {} xlo xhi\n".format(min(x_list)-5, max(x_list)+5))
        f.write("{} {} ylo yhi\n".format(min(y_list)-5, max(y_list)+5))
        f.write("{} {} zlo zhi\n\n".format(min(z_list)-5, max(z_list)+5))
        
        f.write('Masses\n\n1 10.0\n')
        
        f.write("\nAtoms\n\n")
        i = 0
        for item in atom_list:
            i += 1
            f.write("{} 0 1 {} {} {}\n".format(i, item[0], item[1], item[2]))
        
        f.write("\nBonds\n\n")
        j = 0
        for item in bond_list:
            j += 1
            f.write("{} 1 {} {}\n".format(j, item[0]+1, item[1]+1))
        
        f.write("\nAngles\n\n")
        k = 0
        for item in angle_list:
            k += 1
            f.write("{} 1 {} {} {}\n".format(k, item[0]+1, item[1]+1, item[2]+1))
            
        f.close()


