#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 10:51:43 2017

@author: apple
"""

import cx_Oracle
con=cx_Oracle.connect('pythonhol/welcome@101.98.66.65/orcl')
print(con.version)
con.close()
