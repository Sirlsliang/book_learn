#!/usr/bin/python
#-*- coding:utf-8 -*-

#*********************************************
# * Author       : Dr
# * Create Time  : 2017-11-26 03:17
# * Filename     : zip_crack_multi.py
# * Description  : The script to crack the zip file
#*********************************************

import os
import zipfile
import optparse
import threading

class ZipCracker(threading.Thread):
    def __init__(self,zipFile,dicts):
        super(ZipCracker,self).__init__()
        self.zipFile = zipFile
        self.dicts = dicts

    def run(self):
        self.crackZipFile()

    def crackZipFile(self):
        for password in self.dicts:
            word = password.strip("\n")
            self.extractZipFile(word)
    
    def extractZipFile(self,password):
        try:
            self.zipFile.extractall(pwd=password)
            print("[+]Found password %s"% password)
        except:
            pass

def parseArgs():
    parser = optparse.OptionParser("Usage -f <zipFile> -d <dictFile> -n <num>")
    parser.add_option("-f",dest="zipFile",type="string",help="Specify the zip file")
    parser.add_option("-d",dest="dictFile",type="string",help="Specify the dictionary file")
    parser.add_option("-n",dest="num",type="int",help="Specify the num of lines every thread has")
    (options,args) = parser.parse_args()
    zipFile = options.zipFile
    dictFile = options.dictFile
    num = options.num
    if (zipFile == None or dictFile == None):
        print parser.usage
        exit(0)
    return zipFile,dictFile,num


def main():
    zipFile,dictFile,num = parseArgs()
    if not(os.path.isfile(zipFile) or os.path.isfile(dictFile)):
        print("Please input the file that exist")
    zFile = zipfile.ZipFile(zipFile)
    dicts = []
    crackers = []
    with open(dictFile) as dFile:
        index = 0
        for line in dFile.readlines():
            dicts.append(line.strip('\n'))
            index  = index + 1
            if index % num  == 0:
                cracker = ZipCracker(zFile,dicts)
                crackers.append(cracker)
                dicts = []

    for c in crackers:
        c.start()


if __name__ == '__main__':
    main()

