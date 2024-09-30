#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:37:18 2024
README: Code that backs up files and data
@author: karelgreen
"""
#%%  Modules
import os
import sys
from datetime import datetime

#%% Backup folder
fp = os.getcwd()+'/backup_work_data_example/' #Path to folder you wish to backup

save1 = os.getcwd()+'/backup1' #Path to backup location 1
save2 = os.getcwd()+'/backup2' #Path to backup location 2

#%% Checking locations
def file_path(path):
    """Checks that folder to be saved exists"""
    assert os.path.exists(path), "Folder does not exist!" 

file_path(fp)

def save_path(save):
    """Checks that the save path exists, if it doesn't it gives the option to make it"""
    if os.path.exists(save) is False:
        keep_going = str(input(f'{save} does not exist, do you want to make it? Y/N \n'))
        if keep_going == 'Y':
            os.mkdir(save)
        elif keep_going == 'N':
            sys.exit()

save_path(save1)
save_path(save2)
#%% Backing up work
startTime = datetime.now()
os.system(f'rsync -a --progress {fp} {save1}')
print('\n','\n', f'{fp} \nsaved to \n{save1}', '\n', datetime.now() - startTime, '\n', '\n')

startTime = datetime.now()
os.system(f'rsync -a --progress {fp} {save2}')
print('\n','\n', f'{fp} \nsaved to \n{save2}',  '\n',datetime.now() - startTime, '\n', '\n')

