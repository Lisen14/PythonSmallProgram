#Monitor file change and whether it has the specil content.

import os,time,logging
from ConfigParser import ConfigParser

def getTargetFileNameArray(config):
    fileListConfig = config.get("config","target_file")
    fileList = fileListConfig.split(",")
    return fileList

def readTargetFolderConfigFile(config):
    folderName = config.get("config","target_folder")
    return folderName

def getFileListfromFolder():
    return os.listdir(TARGET_FOLDER)
    
def checkfileContent(file_name):
    f = open(file_name,"r")
    while True:
        line = f.readline()
        if not line: break
        if line.find("exception")!=-1 or line.find("Exception")!=-1:
           return True 
    return False
    
def sendAlertEmail(file_name):
    pass

CONFIG_FILE="/Users/workProgram/pythonPractice/MonitorFile/config.ini"

TARGET_FOLDER=os.curdir

logging.basicConfig(level=logging.INFO,filename='monitor.log')

config=ConfigParser()
config.read(CONFIG_FILE)
    
TARGET_FILE_NAME_LIST = getTargetFileNameArray(config)
TARGET_FOLDER = readTargetFolderConfigFile(config)

logging.info("began scaning file")

fileListInSystem = getFileListfromFolder()
nowtime = time.time()

for file in TARGET_FILE_NAME_LIST:
    if file in fileListInSystem:
        #get modify time
        modify_time = os.stat(os.stat(file).st_ctime)
        if((modify_time - nowtime)<= 10 * 60):
            #the file modified resently
            if(checkfileContent):
                sendAlertEmail(file)

logging.info("end scaning file")
