# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 08:52:49 2016

@author: Lina492375qW1188
"""

from scipy import spatial
import math

class Interaction:
    
    def __init__(self, ymax):

        self.ymax = ymax

    def bond(self, atom_list):
        return list(spatial.cKDTree(atom_list).query_pairs(1.1))

    def angle(self, atom_list):

        num_y = 4*self.ymax #num of atoms in y-dir.
        
        angle = []
        
        def law_of_cosine(vec1 , vec2):
            len_vec1 = (sum([p*p for p in vec1]))**0.5
            len_vec2 = (sum([q*q for q in vec2]))**0.5
            dot = sum([p*q for (p,q) in zip(vec1,vec2)])
            return dot/(len_vec1*len_vec2)
        
        tree = spatial.cKDTree(atom_list)
        for i in range(len(atom_list)):
            
            a = tree.query_ball_point(atom_list[i],1.1);    a.remove(i)
            
            for j in range(len(a)):
                for k in range(j+1,len(a)):
                    
                    v1 = [p - q for (p,q) in zip(atom_list[a[j]],atom_list[i])]
                    v2 = [p - q for (p,q) in zip(atom_list[i],atom_list[a[k]])]

                    arc = math.cos(2*math.pi/num_y)

                    if law_of_cosine(v1,v2) > arc:
                        
                        angle.append( [i , a[j] , a[k]])
                        
        return angle

if __name__ == '__main__':
    
    interaction = Interaction(3)
    
    atom_list = [(i,j,k) for i in range(3) for j in range(3) for k in range(2)]
    bond_list = interaction.bond(atom_list)
    angle_list = interaction.angle(atom_list)
    
    print("bond_list = "+str(bond_list))
    print("angle_list = "+str(angle_list))
