# -*- coding: utf-8 -*-
"""project.python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11aY-jWmJbCMPPyRspuyd9lPxLTCC-FgX
"""

s_year = int(input("enter the start year "))
e_year =int(input("enter the end year "))
for year in range(s_year, e_year+1):
  if ((year%4==0 and year%100!=0) or ((year % 400 == 0) and (year % 100 == 0))):
      print((year,"is a Leap Year"),sep="\n")
  else:
      print(year,"is a Non-Leap Year")