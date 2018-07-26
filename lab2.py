# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:50:34 2018

@author: BIT
"""

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return 1.0/(1+np.power(t,2))

t1=np.arange(-10,10,0.001)

plt.plot(t1,f(t1))
plt.show()