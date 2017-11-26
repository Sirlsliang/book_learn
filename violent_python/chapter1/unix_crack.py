#!/usr/bin/python
#-*- coding:utf-8 -*-

#*********************************************
# * Author       : Dr
# * Create Time  : 2017-11-26 01:34
# * Filename     : unix_crack.py
# * Description  : a script of crack password 
#*********************************************

import os

import crypt
import optparse

class PassCracker:

    def __init__(self,passFile,dictFile):
        self.checkFile(passFile)
        self.checkFile(dictFile)
        self.passFile = passFile
        self.dictFile = dictFile

    def checkFile(self,fileName):
        if not os.path.isfile(fileName):
            print("[-] The file %s does not exist"%(fileName))
            exit(0)
        
    def crackPass(self):
        self.parsePassFile()

    def parsePassFile(self):
        if not os.path.isfile(self.passFile):
            print('[-] The file you specify does not exist')
            exit(0)
        with open(self.passFile) as pFile:
            for line in pFile.readlines():
                if ':' in line:
                    self.parsePassLine(line)

    def parsePassLine(self,passLine):
        line = passLine.split(":")
        user = line[0]
        encrypt_word = line[1]
        if len(encrypt_word) > 3:
            pos = encrypt_word.rfind("$")
            salt = encrypt_word[0:pos]
            self.testPass(user,salt,encrypt_word)

    def testPass(self,user,salt,password):
        print("Cracking password for %s"%(user))
        with open(self.dictFile) as dicts:
            for word in dicts.readlines():
                w = word.strip('\n')
                pas = crypt.crypt(w,salt)
                if pas == password:
                    print "  [+]Found password for user %s, password is:%s" %(user,word)


def parseArgs():
    parser = optparse.OptionParser("usage: -f <target_file> -d <dictinary file>")
    parser.add_option("-f",dest='passFile',type='string',help='Specify password file')
    parser.add_option("-d",dest='dictFile',type='string',help='Specify dictionary file')
    (options,args) = parser.parse_args()
    passFile = options.passFile
    dictFile = options.dictFile
    if (passFile == None or dictFile == None):
        print('[-] You must specify a target passFile and a dictionary file')
        exit(0)
    return passFile,dictFile

def main():
    passFile,dictFile = parseArgs()
    cracker = PassCracker(passFile,dictFile)
    cracker.crackPass()
          

if __name__ == '__main__':
    main()
