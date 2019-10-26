# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 10:41:10 2016

@author: Lina492375qW1188
"""

import Create, Deform, Interaction, Construct
#----------------- Number of atom ------------------#
xmax = 150 # num of atoms in x-dir = (2*xmax+1, 2*xmax)
ymax = 50 # num of atoms in y-dir = ymax*4

#----------------- Initialization ------------------#
create = Create.Create(xmax,ymax)
deform = Deform.Deform()
interaction = Interaction.Interaction(create.ymax)
infile='data.unknown'
construct = Construct.Construct(infile)

#---------- Rolling, Set bond and angle ------------#
# action choices: (a)create plane (b)create paper roll.
action = '(b)'

if action == '(a)':
    coord1 = create.trigonal()
elif action == '(b)':
    coord1 = deform.rolling(create.trigonal())
    
bond1 = interaction.bond(coord1)

angle1 = interaction.angle(coord1)

#--------------------- Output ----------------------#
# output: (a)coord only (b)+bond (c)+bond and angle.
output = '(c)'

if output == '(a)':
    construct.output1(coord1)
elif output == '(b)':
    construct.output2(coord1, bond1)
elif output == '(c)':
    construct.output3(coord1, bond1, angle1)
