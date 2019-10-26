# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:11:07 2016

@author: 510a
"""

class Create:
    
    def __init__(self, xmax, ymax):
        
        self.xmax = xmax
        self.ymax = ymax

    def trigonal(self):

        mmax = self.xmax
        nmax = self.ymax
        
        coord1 = ([[m+0.5 , (n+0.5)*(3**0.5) , 0.0] for m in range(-mmax,mmax,1) 
                                                    for n in range(-nmax,nmax,1)])
        coord2 = ([[m , n*(3**0.5) , 0.0] for m in range(-mmax,mmax+1,1) 
                                          for n in range(-nmax+1,nmax+1,1)])

        coord = (coord1+coord2)

        return coord
        
    def square(self):

        mmax = self.xmax
        nmax = self.ymax
        
        return ([(n , m) for n in range(-int(mmax),int(mmax),1) 
                         for m in range(-int(nmax), int(nmax),1)])

if __name__ == '__main__':
    
#-------------- initialization ----------------#
    xmax = 2
    ymax = 3

    create = Create(xmax,ymax)

#-------------- check boundary ----------------#
    print("Check of Boundary: \n")
    print("xmax = "+str(create.xmax))
    print("ymax = "+str(create.ymax)+"\n")
    
    test_lattice = create.trigonal()
    
    #print("lattice coord = "+str(test_lattice))
    
#-------------- check symmetry ----------------#
    x_list = [row[0] for row in test_lattice]
    y_list = [row[1] for row in test_lattice]
            
    x_shift = (max(x_list)+min(x_list))/2
    y_shift = (max(y_list)+min(y_list))/2

    print("Check of Symmetry: \n")
    print("x shift = "+str(x_shift))
    print("y shift = "+str(y_shift)+"\n")
    
