#!/usr/bin/python
#-*- coding:utf-8 -*-

#*********************************************
# * Author       : Dr
# * Create Time  : 2017-11-26 03:17
# * Filename     : zip_crack_single.py
# * Description  : The script to crack the zip file
#*********************************************

import os
import zipfile
import optparse

class ZipCracker:
    def __init__(self,zipFile,dictFile):
        self.checkFile(zipFile)
        self.checkFile(dictFile)
        self.zipFile = zipfile.ZipFile(zipFile)
        self.dictFile = dictFile

    def checkFile(self,fileName):
        if not os.path.isfile(fileName):
            print("[-] The file %s does not exist"%(fileName))
            exit(0)

    def crackZipFile(self):
        with open(self.dictFile) as dFile:
            for line in dFile.readlines():
                password = line.strip("\n")
                self.extractZipFile(password)

    
    def extractZipFile(self,password):
        try:
            self.zipFile.extractall(pwd=password)
            print("[+]Found password %s"% password)
        except:
            pass

def parseArgs():
    parser = optparse.OptionParser("Usage -f <zipFile> -d <dictFile>")
    parser.add_option("-f",dest="zipFile",type="string",help="Specify the zip file")
    parser.add_option("-d",dest="dictFile",type="string",help="Specify the dictionary file")
    (options,args) = parser.parse_args()
    zipFile = options.zipFile
    dictFile = options.dictFile
    if (zipFile == None or dictFile == None):
        print parser.usage
        exit(0)
    return zipFile,dictFile


def main():
    zipFile,dictFile = parseArgs()
    zCracker = ZipCracker(zipFile,dictFile)
    zCracker.crackZipFile()


if __name__ == '__main__':
    main()

