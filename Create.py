# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:11:07 2016

@author: 510a
"""

class Create:
    """
    Create initial lattice structure here. The author made two method for creating the plane lattice. 
    There are two options can be called: triagonal and square-based lattice.
    """
    def __init__(self, xmax, ymax):
        """
        The plane lattice is centered at origin. xmax and ymax are the maximum x and y "indices" can have
        from the center of the lattice plane.
        """
        self.xmax = xmax
        self.ymax = ymax

    def trigonal(self):
        """
        Create plane triagonal lattice with lattice constant = 1.
        """
        mmax = self.xmax
        nmax = self.ymax
        
        coord1 = ([[m+0.5 , (n+0.5)*(3**0.5) , 0.0] for m in range(-mmax, mmax, 1) 
                                                    for n in range(-nmax, nmax, 1)])
        coord2 = ([[m , n*(3**0.5) , 0.0] for m in range(-mmax, mmax+1, 1) 
                                          for n in range(-nmax+1, nmax+1, 1)])

        coord = (coord1+coord2)

        return coord
        
    def square(self):
        """
        Create plane square lattice with lattice constant = 1.
        """
        mmax = self.xmax
        nmax = self.ymax
        
        return ([(n , m) for n in range(-int(mmax), int(mmax), 1) 
                         for m in range(-int(nmax), int(nmax), 1)])

if __name__ == '__main__':
    
    #-------------- initialization ----------------#
    xmax = 2
    ymax = 3

    create = Create(xmax, ymax)

    #-------------- print lattices ----------------#
    test_lattice = create.trigonal()
    
    print("lattice coord = {}\n".format(test_lattice))
    
    #-------------- check symmetry ----------------#
    x_list = [row[0] for row in test_lattice]
    y_list = [row[1] for row in test_lattice]
            
    x_shift = (max(x_list)+min(x_list))/2
    y_shift = (max(y_list)+min(y_list))/2

    print("Check the center of lattice: \n")
    print("x shift = {}".format(x_shift))
    print("y shift = {}\n".format(y_shift))
