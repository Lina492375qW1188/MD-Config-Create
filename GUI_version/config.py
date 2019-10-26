# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 10:41:10 2016

@author: Lina492375qW1188
"""

import wx
import Create, Deform, Interaction, Construct

if __name__ =='__main__':

    app = wx.PySimpleApp()

#-------------- Entering Information ----------------#
    #border in x-direction:
    x_border = wx.TextEntryDialog(None, 'xmax:', 'Enter xmax here.')
    if x_border.ShowModal() == wx.ID_OK:
        xmax = int(x_border.GetValue()) #num of atoms in x-dir = (2*xmax+1, 2*xmax)

        #border in y-direction:
        y_border = wx.TextEntryDialog(None, 'ymax:', 'Enter ymax here.')
        if y_border.ShowModal() == wx.ID_OK:
            ymax = int(y_border.GetValue()) #num of atoms in y-dir = ymax*4

            #Choose the action:
            act_value = wx.SingleChoiceDialog(None, '(a)create a plane\n(b)create a paper roll', 'Action', ['(a)','(b)'])
            if act_value.ShowModal() == wx.ID_OK:
                action = act_value.GetStringSelection()

                #Choose the output way:
                out_value = wx.SingleChoiceDialog(None, '(a)Coordinates only\n(b)Coordinates with bonds\n(c)Coordinates with bonds and angles','Output', ['(a)','(b)','(c)'])
                if out_value.ShowModal() == wx.ID_OK:
                    output = out_value.GetStringSelection()



#----------------- Initialization ------------------#
create = Create.Create(xmax,ymax)
deform = Deform.Deform()
interaction = Interaction.Interaction(create.ymax)
construct = Construct.Construct()

#---------- Rolling, Set bond and angle ------------#
#action choices: (a)create plane (b)create paper roll.
#action = '(b)'

if action == '(a)':
    coord1 = create.trigonal()
elif action == '(b)':
    coord1 = deform.rolling(create.trigonal())
    
bond1 = interaction.bond(coord1)

angle1 = interaction.angle(coord1)

#--------------------- Output ----------------------#
#output: (a)coord only (b)+bond (c)+bond and angle.
#output = '(c)'

if output == '(a)':
    construct.output1(coord1)
elif output == '(b)':
    construct.output2(coord1, bond1)
elif output == '(c)':
    construct.output3(coord1, bond1, angle1)

