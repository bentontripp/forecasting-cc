﻿import datetime
import pandas as pd

def holiday_lis():
	"""Generates list of holidays where there is not any call volume (other than occasional testing)"""
	holidays = [datetime.datetime(2018,1,1),
            	    datetime.datetime(2018,1,15),
            	    datetime.datetime(2018,2,19),
 	            datetime.datetime(2018,3,30),
 	            datetime.datetime(2018,5,28),
                    datetime.datetime(2018,7,4),
 	            datetime.datetime(2018,9,3),
                    datetime.datetime(2018,10,26),
                    datetime.datetime(2018,11,22),
                    datetime.datetime(2018,11,23),
                    datetime.datetime(2018,12,5),
                    datetime.datetime(2018,12,24),
                    datetime.datetime(2018,12,25),
                    datetime.datetime(2019,1,1),
                    datetime.datetime(2019,1,1),
                    datetime.datetime(2019,1,21),
                    datetime.datetime(2019,2,18),
                    datetime.datetime(2019,3,18),
                    datetime.datetime(2019,4,19),
                    datetime.datetime(2019,5,27),
                    datetime.datetime(2019,7,4),
                    datetime.datetime(2019,9,2),
                    datetime.datetime(2019,11,28),
                    datetime.datetime(2019,11,29),
                    datetime.datetime(2019,12,24),
                    datetime.datetime(2019,12,25),
                    datetime.datetime(2020,1,1),
                    datetime.datetime(2020,1,20),
                    datetime.datetime(2020,2,17),
                    datetime.datetime(2020,4,10),
                    datetime.datetime(2020,5,25),
                    datetime.datetime(2020,6,19),
                    datetime.datetime(2020,7,3),
                    datetime.datetime(2020,9,7),
		    datetime.datetime(2020,11,3),
                    datetime.datetime(2020,11,26),
                    datetime.datetime(2020,11,27),
                    datetime.datetime(2020,12,24),
                    datetime.datetime(2020,12,25),
		    datetime.datetime(2021,1,1),
		    datetime.datetime(2021,1,18),
		    datetime.datetime(2021,2,15),
		    datetime.datetime(2021,4,2),
		    datetime.datetime(2021,6,18),
		    datetime.datetime(2021,7,5),
		    datetime.datetime(2021,8,6),
		    datetime.datetime(2021,11,25),
		    datetime.datetime(2021,11,26),
		    datetime.datetime(2021,12,23),
		    datetime.datetime(2021,12,24)]
	return holidays

def dept_dict():
	"""Generates mapping of main departments to sub-groups"""
	depts = {'dept_1a':'dept_1','dept_1b':'dept_1','dept_1c':'dept_1',
		 'dept_2a':'dept_2','dept_2b':'dept_2','dept_2c':'dept_2','dept_2d':'dept_2',
		 'dept_3a':'dept_3','dept_3b':'dept_3','dept_3c':'dept_3','dept_3d':'dept_3',
		 'dept_4a':'dept_4','dept_4b':'dept_4','dept_4c':'dept_4','dept_4d':'dept_4','dept_4e':'dept_4',
		 'dept_5a':'dept_5',
		 'dept_6a':'dept_6',
		 'dept_7a':'dept_7','dept_7b':'dept_7',
		 'dept_8a':'dept_8',
		 'dept_9a':'dept_9',
        	 'dept_10a':'dept_10',
        	 'dept_11a':'dept_11'}
	return depts

def grp_dict():
	"""Generates mapping of splits to sub-groups"""
	grps = {4:'dept_9a',
		14:'dept_8a',
        	15:'dept_8a',
        	48:'dept_5a',
        	49:'dept_7a',
        	51:'dept_2d',
        	54:'dept_7a',
        	58:'dept_2c',
       		62:'dept_5a',
        	80:'dept_6a',
        	82:'dept_6a',
        	93:'dept_1c',
        	96:'dept_2a',
        	97:'dept_2b',
        	102:'dept_3a',
		106:'dept_11a',
        	114:'dept_8a',
        	123:'dept_6a',
        	131:'dept_8a',
        	150:'dept_7b',
        	161:'dept_3a',
        	165:'dept_3b',
        	166:'dept_3a',
        	168:'dept_3c',
        	170:'dept_1a',
        	173:'dept_2d',
        	176:'dept_1b',
        	177:'dept_1a',
        	178:'dept_3d',
        	182:'dept_1a',
        	183:'dept_8a',
        	187:'dept_1a',
        	902:'dept_10a',
        	903:'dept_4a',
        	904:'dept_10a',
        	907:'dept_4b',
        	909:'dept_10a',
        	925:'dept_4c',
        	926:'dept_4d',
        	934:'dept_4e',
        	942:'dept_4a',
        	1025:'dept_2b',
        	1095:'dept_9a',
        	1208:'dept_2a',
        	1268:'dept_5a'}
	return grps