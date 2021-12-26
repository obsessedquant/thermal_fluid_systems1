#!/usr/bin/env python
# coding: utf-8

# # Custom Thermo
# 
# I wrote this script to be used in conjunction with other libraries hosting the accurate saturation tables data.

# In[ ]:


class custom_thermo:
    '''
    This class was created to capture calculations that are not present in any other module or library.
    
    How to use this class:
    
    from custom_thermo import custom_thermo as ct
    
    # Find the quality based on pressure and entropy inputs
    x = ct.find_quality(P=p, s=s)
    print(x)
    '''

    def find_quality(P,s):
        '''
        Requires pressure (P) in MPa and entropy (s) in kJ/kg*Celsius input values.

        Example
        Inputs:
        print(find_quality(P=0.01, s=6.727))

        Output:
        0.81047
        '''
        # !pip install pyXSteam
        from pyXSteam.XSteam import XSteam
        steamTable = XSteam(XSteam.UNIT_SYSTEM_BARE)
        # print(steamTable.hL_p(5))

        sL = steamTable.sL_p(P)
        sV = steamTable.sV_p(P)

        x = (s - sL) / (sV - sL)
        return x

