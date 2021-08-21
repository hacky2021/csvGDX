#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-----***************************************************************-----
#-----*************************Version:1.0.0*************************-----
#-----*********************Creation_Date:21/8/20*********************-----
#-----**********************CreatedDate:21/8/21**********************-----
#-----***********************creator:hacky2021***********************-----
#-----*****************https://github.com/hacky2021/*****************-----
#-----***************************************************************-----
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
import re
class copen:
    def __init__(self,file,mode):
        self.file=open(file,"r+")
        self.fileList=self.file.read().split('\n')
        self.mode=mode
        self.i=-1
        for s in self.fileList:
            self.i+=1
            self.fileList[self.i]=self.fileList[self.i].split(',')
    def setCell(self,c1,c2):
        if self.mode==1:
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c1.upper(), re.I).groups()
            self.items1=[0,0]
            self.items1[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items1[1]=int(self.itemsT[1])-1
        elif self.mode==2:
            self.items1=[0,0]
            self.items1[0]=int(c1[:c1.find(":")])
            self.items1[1]=int(c1[c1.find(":")+1:len(c1)])
        self.fileList[self.items1[1]][self.items1[0]]=str(c2)
    def getCell(self,c1):
        if self.mode==1:
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c1.upper(), re.I).groups()
            self.items1=[0,0]
            self.items1[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items1[1]=int(self.itemsT[1])-1
        elif self.mode==2:
            self.items1=[0,0]
            self.items1[0]=int(c1[:c1.find(":")])
            self.items1[1]=int(c1[c1.find(":")+1:len(c1)])
        return self.fileList[self.items1[1]][self.items1[0]]
    def addCell(self,c1,c2,c3):
        if self.mode==1:
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c1.upper(), re.I).groups()
            self.items1=[0,0]
            self.items1[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items1[1]=int(self.itemsT[1])-1
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c2.upper(), re.I).groups()
            self.items2=[0,0]
            self.items2[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items2[1]=int(self.itemsT[1])-1
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c3.upper(), re.I).groups()
            self.items3=[0,0]
            self.items3[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items3[1]=int(self.itemsT[1])-1
        elif self.mode==2:
            self.items1=[0,0]
            self.items1[0]=int(c1[:c1.find(":")])
            self.items1[1]=int(c1[c1.find(":")+1:len(c1)])
            self.items2=[0,0]
            self.items2[0]=int(c2[:c2.find(":")])
            self.items2[1]=int(c2[c2.find(":")+1:len(c2)])
            self.items3=[0,0]
            self.items3[0]=int(c3[:c3.find(":")])
            self.items3[1]=int(c3[c3.find(":")+1:len(c3)])
        self.fileList[self.items3[1]][self.items3[0]]=str(int(self.fileList[self.items1[1]][self.items1[0]])+int(self.fileList[self.items2[1]][self.items2[0]]))
    def subCell(self,c1,c2,c3):
        if self.mode==1:
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c1.upper(), re.I).groups()
            self.items1=[0,0]
            self.items1[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items1[1]=int(self.itemsT[1])-1
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c2.upper(), re.I).groups()
            self.items2=[0,0]
            self.items2[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items2[1]=int(self.itemsT[1])-1
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c3.upper(), re.I).groups()
            self.items3=[0,0]
            self.items3[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items3[1]=int(self.itemsT[1])-1
        elif self.mode==2:
            self.items1=[0,0]
            self.items1[0]=int(c1[:c1.find(":")])
            self.items1[1]=int(c1[c1.find(":")+1:len(c1)])
            self.items2=[0,0]
            self.items2[0]=int(c2[:c2.find(":")])
            self.items2[1]=int(c2[c2.find(":")+1:len(c2)])
            self.items3=[0,0]
            self.items3[0]=int(c3[:c3.find(":")])
            self.items3[1]=int(c3[c3.find(":")+1:len(c3)])
        self.fileList[self.items3[1]][self.items3[0]]=str(int(self.fileList[self.items1[1]][self.items1[0]])-int(self.fileList[self.items2[1]][self.items2[0]]))
    def mulCell(self,c1,c2,c3):
        if self.mode==1:
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c1.upper(), re.I).groups()
            self.items1=[0,0]
            self.items1[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items1[1]=int(self.itemsT[1])-1
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c2.upper(), re.I).groups()
            self.items2=[0,0]
            self.items2[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items2[1]=int(self.itemsT[1])-1
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c3.upper(), re.I).groups()
            self.items3=[0,0]
            self.items3[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items3[1]=int(self.itemsT[1])-1
        elif self.mode==2:
            self.items1=[0,0]
            self.items1[0]=int(c1[:c1.find(":")])
            self.items1[1]=int(c1[c1.find(":")+1:len(c1)])
            self.items2=[0,0]
            self.items2[0]=int(c2[:c2.find(":")])
            self.items2[1]=int(c2[c2.find(":")+1:len(c2)])
            self.items3=[0,0]
            self.items3[0]=int(c3[:c3.find(":")])
            self.items3[1]=int(c3[c3.find(":")+1:len(c3)])
        self.fileList[self.items3[1]][self.items3[0]]=str(int(self.fileList[self.items1[1]][self.items1[0]])*int(self.fileList[self.items2[1]][self.items2[0]]))
    def shrCell(self,c1,c2,c3):
        if self.mode==1:
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c1.upper(), re.I).groups()
            self.items1=[0,0]
            self.items1[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items1[1]=int(self.itemsT[1])-1
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c2.upper(), re.I).groups()
            self.items2=[0,0]
            self.items2[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items2[1]=int(self.itemsT[1])-1
            self.itemsT=re.match(r"([A-Z]+)([0-9]+)",c3.upper(), re.I).groups()
            self.items3=[0,0]
            self.items3[0]=int(self.itemsT[0].replace("A","1").replace( "B","2").replace( "C","3").replace( "D","4").replace( "E","5").replace( "F","6").replace( "G","7").replace( "H","8").replace( "I","9").replace( "J","a").replace( "K","b").replace( "L","c").replace( "M","d").replace( "N","e").replace( "O","f").replace( "P","g").replace( "Q","h").replace( "R","i").replace( "S","j").replace( "T","k").replace( "U","l").replace( "V","m").replace( "W","n").replace( "X","o").replace( "Y","p").replace( "Z","q"),27)-1
            self.items3[1]=int(self.itemsT[1])-1
        elif self.mode==2:
            self.items1=[0,0]
            self.items1[0]=int(c1[:c1.find(":")])
            self.items1[1]=int(c1[c1.find(":")+1:len(c1)])
            self.items2=[0,0]
            self.items2[0]=int(c2[:c2.find(":")])
            self.items2[1]=int(c2[c2.find(":")+1:len(c2)])
            self.items3=[0,0]
            self.items3[0]=int(c3[:c3.find(":")])
            self.items3[1]=int(c3[c3.find(":")+1:len(c3)])
        self.fileList[self.items3[1]][self.items3[0]]=str(int(self.fileList[self.items1[1]][self.items1[0]])/int(self.fileList[self.items2[1]][self.items2[0]]))
    def save(self):
        self.fileSF=""
        for s1 in self.fileList:
            self.i=0
            for s2 in s1:
                self.i+=1
                if self.i<len(s1):
                    self.fileSF=self.fileSF+s2+","
                else:
                    self.fileSF=self.fileSF+s2
            self.fileSF=self.fileSF+"\n"
        self.fileSF=self.fileSF[:len(self.fileSF)-1]
        with self.file as file:
            data=self.file.read()
            file.seek(0)
            file.write(self.fileSF)
            file.truncate()
