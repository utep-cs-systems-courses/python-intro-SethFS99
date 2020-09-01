# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:04:26 2020

@author: sethf
"""
import sys, re


def checkW(String, myDict):#updates dicttionary
    if String in myDict:
        myDict[String] +=1
    else:
        myDict[String] = 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python WordCount.py " + "<input file> <output file>" )#error message
        sys.exit()
    myDict = {}
    with open(sys.argv[1], mode="r", encoding="utf-8") as input_file, \
            open(sys.argv[2], mode="w", encoding="utf-8") as output_file:
                file = input_file.read()#reads the entire file
                file = re.split("[; |, |. |! |? |-|:|\n|\s|\t|']\s*",file)#splits file by all spaces and punctuation plus some extra
                
                for word in file:
                    if len(word) == 0:
                        continue
                    if "-" in word:#some words with the - character don't parse correctly with the above Regular Expression so they are parsed again here
#                        print(word)#this was testing
                        newWords = word.split("-")
                        for x in newWords:#parsing out empty characters
                            if len(x) ==0:
                                continue
                            newX = x.lower()
                            checkW(newX,myDict)
                        continue# if worth with '-' character found and entered continue to next word
                    newWord = word.lower()#converts word to lowercase
                    checkW(newWord,myDict)#updates dictionary
                myDict = sorted(myDict.items())
#                myDict = sorted(myDict.items(), key=lambda x: x[1], reverse=True)#sorts dictionary in deceding values
                
#                print(myDict[:5]) #testing to see if my dictionary works correctly
                for myWord in myDict:
                    text = myWord[0] + " " + str(myWord[1]) + "\n"
                    output_file.write(text)#writes the word, number of appearances and starts new line
                
                    
                