# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 08:52:49 2016

@author: Lina492375qW1188
"""

from scipy import spatial
import math

class Interaction:
    """
    This class defines the methods which we used to creat the connection between atoms and atoms.
    As an example, the author created two methods for LAMMPS bonds and angles.
    The methods that the author made connect every two points in the lattice of "paper roll" with a 
    single bond, and specify an angle with three atoms along a line.
    """
    def __init__(self, ymax):
        """
        Here we can define any initial parameters that we might need when building the connection.
        """
        self.ymax = ymax

    def bond(self, atom_list):
        """
        This function search nearest neighbor atoms within distance = 1 and connect them with bonds
        using KDTree method in scipy.
        """
        return list(spatial.cKDTree(atom_list).query_pairs(1.1))

    def angle(self, atom_list):
        """
        This method make a list of LAMMPS angles with three atoms which have their coordinates line 
        up. The way we do it is:
        (1) Use scipy tree.query_ball to find the list of atoms in the ball distance.
        (2) Connect only the atoms in the list which are arranged along a line.
        (3) We check whether they are along a line by calculating the law of cosine.
        """
        num_y = 4*self.ymax # num of atoms in y-dir.
        
        angle = []
        
        def law_of_cosine(vec1 , vec2):
            """
            A function used to calculate the law of cosine.
            """
            len_vec1 = (sum([p*p for p in vec1]))**0.5
            len_vec2 = (sum([q*q for q in vec2]))**0.5
            dot = sum([p*q for (p,q) in zip(vec1,vec2)])
            return dot/(len_vec1*len_vec2)
        
        tree = spatial.cKDTree(atom_list)    
        for i in range(len(atom_list)):
            
            a = tree.query_ball_point(atom_list[i],1.1);    a.remove(i)            
            for j in range(len(a)):
                for k in range(j+1, len(a)):
                    
                    v1 = [p - q for (p,q) in zip(atom_list[a[j]], atom_list[i])]
                    v2 = [p - q for (p,q) in zip(atom_list[i], atom_list[a[k]])]

                    arc = math.cos(2*math.pi/num_y)

                    if law_of_cosine(v1, v2) > arc:
                        
                        angle.append( [a[j] , i , a[k]])
                        
        return angle

if __name__ == '__main__':
    
    interaction = Interaction(3)
    
    # In this example, we did not really make connection on the lattice of the paper roll.
    # We generate an example square latticce to show intuitively how to use this interaction object.
    atom_list = [(i, j, k) for i in range(3) for j in range(3) for k in range(2)]
    bond_list = interaction.bond(atom_list)
    angle_list = interaction.angle(atom_list)
    
    print("bond_list\n{}".format(bond_list))
    print("angle_list\n{}".format(angle_list))
