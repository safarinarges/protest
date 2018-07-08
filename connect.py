#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 10:51:43 2017

@author: apple
"""

import cx_Oracle
con=cx_Oracle.connect('cl')
print(con.version)
con.close()
