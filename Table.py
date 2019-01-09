
#print Table
#kangx 01-08-2019

#add table from text

#aling = center
#align = left
# +------------+----------+-------+--------------+------------+
# |    name    |  gender  |  age  |   birthday   |   nation   |
# +------------+----------+-------+--------------+------------+
# |  opmdmlwk  |   male   |  32   |  1090-23-90  |   dhand    |
# |  oueiwjg   |  female  |  83   |  3o83-20-81  |  11222222  |
# +------------+----------+-------+--------------+------------+
# +----------+--------+-----+------------+----------+
# | name     | gender | age | birthday   | nation   |
# +----------+--------+-----+------------+----------+
# | opmdmlwk | male   | 32  | 1090-23-90 | dhand    |
# | oueiwjg  | female | 83  | 3o83-20-81 | 11222222 |
# +----------+--------+-----+------------+----------+
import sys

class Table:
    def __init__(self):
        self.header = ""
        self.list= []
        self.body =""
        self.tail = ""
        self.align = "center"
        self.hlist = []
        self.lenlist= []
        self.bcolor = "\033[92m{0}\033[0m"
        self.fcolor = "\033[93m{0}\033[0m"


    def p_list(self):
        print self.hlist
        print self.list
        print self.lenlist

    def set_bordercolor(self,ft):
        self.bcolor = "\033[" + str(ft) + "m{0}\033[0m"

    def set_fontcolor(self,ft):
        self.fcolor = "\033[" + str(ft) + "m{0}\033[0m"

    def set_align(self,al):
        if al not in ["center","left","rught"]:
            print "\033[91mError: invalid alignment input\033[0m"
            sys.exit()
        self.align = al

    def remove_whitespace_sccharacter(self,slist): # remove whitespace and string control characters
        templist = []
        for item in slist:
            if item not in [ " ",""] :
                templist.append(item.strip().strip("\n"))
        return templist

    def add_fromtext(self,txt,spstr=" "):
        linecnt = 0
        notitle = False
        with open(txt,"r") as f:
            # linescnt = sum(1 for _ in f)
            # f.seek(0,0)
            for line in f:
                if line.strip() == "":
                    continue
                if "#no_title" in line:
                    notitle = True
                    continue
                items = line.split(spstr)
                aitems = self.remove_whitespace_sccharacter(items)
                # print len(aitems),aitems
                if not notitle:
                    if not linecnt: #if it is first line in the file, It should be the heaser
                        self.addheader(aitems)
                    else:
                        self.addrow(aitems)
                else:
                    self.addrow(aitems)
                linecnt += 1

    def addheader(self,hlist):
        if type(hlist) != list:
            print "\033[91mError: invalid  input\033[0m"
            sys.exit()
        self.hlist.append(hlist)

    def addrow(self,rlist):
        if type(rlist) != list:
            print "\033[91mError: invalid  input\033[0m"
            sys.exit()
        self.list.append(rlist)

    # +----------------------------------------------------------+
    # |    name    |  gender  | age  |   birthday   |   nation   |
    # +----------------------------------------------------------+
    # |  opmdmlwk  |   male   |  32  |  1090-23-90  |   dhand    |
    # |  oueiwjg   |  female  |  83  |  3o83-20-81  |  11222222  |
    # +----------------------------------------------------------+

    #list0 | item       | ite  | sdjsdj|
    #list1 | diahkldhgk | jd91 | 2299  |
    #x    0  1  2
    #list 0 1

    def handlelist(self,inlist,is_header = False):
        if not len(inlist):
            return
        for tlist in inlist:
            self.body += self.bcolor.format("\n|")
            for index,item in enumerate(tlist):
                if self.align == "center": # space + (half leng space ) + item + (halflen space)
                    odd = (self.lenlist[index] - len(item) ) % 2
                    halflen =  (self.lenlist[index] - len(item))/2 + 2#
                    self.body += self.fcolor.format( " "* halflen +  str(item) + " "*(halflen+odd) )+ self.bcolor.format("|") #if the length of item is odd, add one space to right of item to balance len
                elif self.align == "left": #two spaces around the item
                    self.body += self.fcolor.format( " " + str(item) + " "*(self.lenlist[index] - len(item)) ) + self.bcolor.format(" |")

            if is_header:
                self.body += "\n"+self.bcolor.format(self.header)

    def printtable(self,border=0):
        self.lenlist = [] #var to store the max length of item

        if  len(self.hlist) :
            templist = self.hlist
        elif  len(self.list) :
            templist = self.list
        else :
            return
        try:
            for x in range(len(templist[0])): #Find max length of item
                itemlenMax = 0
                try:
                    if len(self.list) :
                        for tlist in self.list:
                            if itemlenMax < len(tlist[x]):
                                itemlenMax = len(tlist[x])
                except Exception as e:
                    print "\033[91mError : invalid input\033[0m",e
                try:
                    if len(self.hlist) :
                        for item in self.hlist:
                            if itemlenMax < len(item[x]):
                                itemlenMax = len(item[x])
                except Exception as e:
                    print "\033[91mError : invalid input\033[0m",e
                self.lenlist.append( itemlenMax ) #add to list
        except Exception as e:
            print "\033[91mError : invalid input\033[0m",e
            sys.exit()
        #prepare header and tail string
        self.header += "+"
        for item in self.lenlist:
            if self.align == "center":
                self.header += "-"*(item + 4) + "+"
            else :
                self.header += "-"*(item + 2)+"+"
        self.tail = "\n" + self.header

        #handle header
        if len(self.hlist):
            self.handlelist(self.hlist,is_header = True)
        if len(self.list):
            self.handlelist(self.list)
        print self.bcolor.format(self.header) \
        + self.fcolor.format( self.body ) \
        + self.bcolor.format( self.tail)
