# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:07:23 2016

@author: Lina492375qW1188
"""

class Construct:
    
    pass

    def output1(self, atom_list):
        f = open('.\data.unknown','w')
        
        f.write('LAMMPS data file, version 2016-ICMS, timestep = unkown\n\n')
        
        f.write(str(len(atom_list))+" atoms\n\n")
        
        f.write('1 atom types\n\n')
        
        x_list = [row[0] for row in atom_list]
        y_list = [row[1] for row in atom_list]
        z_list = [row[2] for row in atom_list]
        
        f.write(str(min(x_list)-5)+" "+str(max(x_list)+5)+" xlo xhi\n")
        f.write(str(min(y_list)-5)+" "+str(max(y_list)+5)+" ylo yhi\n")
        f.write(str(min(z_list)-5)+" "+str(max(z_list)+5)+" zlo zhi\n\n")
        
        f.write('Masses\n\n1 10.0\n')
        
        f.write("\nAtoms\n\n")
        i = 0
        for item in atom_list:
            i += 1            
            f.write(str(i)+" 0 1 "+str(item[0])+" "+str(item[1])+" "+str(item[2])+"\n")
        
        f.close()
       
    def output2(self, atom_list, bond_list):
        f = open('.\data.unknown','w')
        
        f.write('LAMMPS data file, version 2016-ICMS, timestep = unkown\n\n')
        
        f.write(str(len(atom_list))+" atoms\n")
        f.write(str(len(bond_list))+" bonds\n\n")
        
        f.write('1 atom types\n')
        f.write('1 bond types\n\n')
        
        x_list = [row[0] for row in atom_list]
        y_list = [row[1] for row in atom_list]
        z_list = [row[2] for row in atom_list]
        
        f.write(str(min(x_list)-5)+" "+str(max(x_list)+5)+" xlo xhi\n")
        f.write(str(min(y_list)-5)+" "+str(max(y_list)+5)+" ylo yhi\n")
        f.write(str(min(z_list)-5)+" "+str(max(z_list)+5)+" zlo zhi\n\n")
        
        f.write('Masses\n\n1 10.0\n')
        
        f.write("\nAtoms\n\n")
        i = 0
        for item in atom_list:
            i += 1            
            f.write(str(i)+" 0 1 "+str(item[0])+" "+str(item[1])+" "+str(item[2])+"\n")
        
        f.write("\nBonds\n\n")
        j = 0
        for item in bond_list:
            j += 1
            f.write(str(j)+" 1 "+str(item[0]+1)+" "+str(item[1]+1)+"\n")
            
        f.close()

    def output3(self, atom_list, bond_list, angle_list):
        f = open('.\data.unknown','w')
        
        f.write('LAMMPS data file, version 2016-ICMS, timestep = unkown\n\n')
        
        f.write(str(len(atom_list))+" atoms\n")
        f.write(str(len(bond_list))+" bonds\n")
        f.write(str(len(angle_list))+" angles\n\n")
        
        f.write('1 atom types\n')
        f.write('1 bond types\n')
        f.write('1 angle types\n\n')
        
        x_list = [row[0] for row in atom_list]
        y_list = [row[1] for row in atom_list]
        z_list = [row[2] for row in atom_list]
        
        f.write(str(min(x_list)-5)+" "+str(max(x_list)+5)+" xlo xhi\n")
        f.write(str(min(y_list)-5)+" "+str(max(y_list)+5)+" ylo yhi\n")
        f.write(str(min(z_list)-5)+" "+str(max(z_list)+5)+" zlo zhi\n\n")
        
        f.write('Masses\n\n1 10.0\n')
        
        f.write("\nAtoms\n\n")
        i = 0
        for item in atom_list:
            i += 1            
            f.write(str(i)+" 0 1 "+str(item[0])+" "+str(item[1])+" "+str(item[2])+"\n")
        
        f.write("\nBonds\n\n")
        j = 0
        for item in bond_list:
            j += 1
            f.write(str(j)+" 1 "+str(item[0]+1)+" "+str(item[1]+1)+"\n")
        
        f.write("\nAngles\n\n")
        k = 0
        for item in angle_list:
            k += 1
            f.write(str(k)+" 1 "+str(item[0]+1)+" "+str(item[1]+1)+" "+str(item[2]+1)+"\n")
            
        f.close()
