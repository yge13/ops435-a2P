#OPS435 Assignment 2P - Fall 2019
#Program: a2_yge13.py 
#Author: "Yun Ge"
#The python code in this file (a2_yge13.py) is original work written by "Yun Ge".  No code in this file is copied from any other source except those provided by the course instructor, including any person, textbook, or on-line resource. I have not shared this python script with anyone or anything except for submission for grading. 
#I understand that the Academic Honesty Policy will be enforced and violators will be reported and appropriate action will be taken.

class Date:
   def __init__(self,year=0,month=0,day=0):
       self.year = year
       self.month = month
       self.day = day
   
   def __str__(self):
      return '%.2d-%.2d-%.2d' % (self.year, self.month, self.day)

   def __add__(self, t2):
       return self.sum_date(t2)

   def __sub__(self, t3):
       return self.desc_date(t3)

   def __repr__(self):
      return '%.2d-%.2d-%.2d' % (self.year, self.month, self.day)


   import sys  
   
   def tomorrow(self):
       str_year, str_month, str_day = self.year, self.month, self.day
       year = int(str_year) 
       month = int(str_month)
       day = int(str_day)

       lyear = year % 4
       if lyear == 0:
          feb_max = 29
       else:
          feb_max = 28

       lyear = year % 100
       if lyear == 0:
          feb_max = 28

       lyear = year % 400
       if lyear == 0:
          feb_max = 29

       tmp_day = day + 1

       mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
       tmp_day = day + 1
       if tmp_day > mon_max[month]:
          to_day = tmp_day % mon_max[month]
          tmp_month = month + 1
       else:
          to_day = tmp_day
          tmp_month = month + 0

       if tmp_month > 12:
           to_month = 1
           year = year + 1
       else:
           to_month = tmp_month + 0

       next_date = str(year)+"-"+str(to_month).zfill(2)+"-"+str(to_day).zfill(2)
       return next_date

   def yesterday(self):
       str_year, str_month, str_day = self.year, self.month, self.day
       year = int(str_year) 
       month = int(str_month)
       day = int(str_day)

       lyear = year % 4
       if lyear == 0:
          feb_max = 29
       else:
          feb_max = 28

       lyear = year % 100
       if lyear == 0:
          feb_max = 28

       lyear = year % 400
       if lyear == 0:
          feb_max = 29

       tmp_day = day - 1 
       mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
       tmp_day = day - 1
       if tmp_day <= 0:
          to_month = month - 1
          if to_month == 0:
            year = year -1
            to_month = 12
            to_day = mon_max[to_month]
          else:
            to_day = mon_max[to_month]
       else:
          to_month = month
          to_day = tmp_day

       before_date = str(year)+"-"+str(to_month).zfill(2)+"-"+str(to_day).zfill(2)
       return before_date

   def sum_date(self, t2):
       str_year, str_month, str_day = self.year, self.month, self.day
       year = int(str_year) 
       month = int(str_month)
       day = int(str_day)
       t2 = int(t2)
	   
       lyear = year % 4
       if lyear == 0:
          feb_max = 29
       else:
          feb_max = 28

       lyear = year % 100
       if lyear == 0:
          feb_max = 28

       lyear = year % 400
       if lyear == 0:
          feb_max = 29


       mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
       tmp_day = day + t2
       if tmp_day > mon_max[month]:
          to_day = tmp_day % mon_max[month]
          tmp_month = month + 1
       else:
          to_day = tmp_day
          tmp_month = month + 0

       if tmp_month > 12:
           to_month = 1
           year = year + 1
       else:
           to_month = tmp_month + 0

       next_date = str(year)+"-"+str(to_month).zfill(2)+"-"+str(to_day).zfill(2)
       return next_date

   def desc_date(self, t3):
       str_year, str_month, str_day = self.year, self.month, self.day
       year = int(str_year) 
       month = int(str_month)
       day = int(str_day)
       t3 = int(t3)

       lyear = year % 4
       if lyear == 0:
          feb_max = 29
       else:
          feb_max = 28

       lyear = year % 100
       if lyear == 0:
          feb_max = 28

       lyear = year % 400
       if lyear == 0:
          feb_max = 29

       tmp_day = day - t3 
       mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
       tmp_day = day - t3 
       if tmp_day <= 0:
          to_month = month - 1
          if to_month == 0:
            year = year - 1
            to_month = 12
            to_day = mon_max[to_month]-(abs(t3)-1)
          else:
            to_day = mon_max[to_month]
       else:
          to_month = month
          to_day = tmp_day

       before_date = str(year)+"-"+str(to_month).zfill(2)+"-"+str(to_day).zfill(2)
       return before_date

def date_of_week(self):
    if month < 3:
        z = year-1
    else:
        z = year
    dayofweek = ( 23*month//9 + day + 4 + year + z//4 - z//100 + z//400 )
    if month >= 3:
        dayofweek -= 2
    dayofweek = dayofweek%7
    return dayofweek
