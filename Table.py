
#print Table
#kangx 01-08-2019
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
        self.bcolor = ""
        self.fcolor = ""

    def set_bordercolor(self,ft):
        self.bcolor = "\033[" + str(ft) + "m{0}\033[0m"

    def set_fontcolor(self,ft):
        self.fcolor = "\033[" + str(ft) + "m{0}\033[0m"

    def set_align(self,al):
        if al not in ["center","left","rught"]:
            print "\033[91mError: invalid alignment input\033[0m"
            sys.exit()
        self.align = al

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
        if len(inlist):
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

    def printlist(self,border=0):
        self.lenlist = [] #var to store the max length of item
        try:
            for x in range(len(self.list[0])): #Find max length of item
                itemlenMax = 0
                for tlist in self.list:
                    if itemlenMax < len(tlist[x]):
                        itemlenMax = len(tlist[x])
                for item in self.hlist:
                    if itemlenMax < len(item[x]):
                        itemlenMax = len(item[x])
                self.lenlist.append( itemlenMax ) #add to list
        except Exception as e:
            print "\033[91mError : invalid input\033[0m"
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
        self.handlelist(self.hlist,is_header = True)
        self.handlelist(self.list)
        print self.bcolor.format(self.header) \
        + self.fcolor.format( self.body ) \
        + self.bcolor.format( self.tail)

#test case
if __name__ == "__main__":

    mt = Table()
    mt.set_align("center")
    mt.addheader( ["name","gender","age","birthday","nation"] )
    mt.addrow(  ["opmdmlwk","male","32","1090-23-90","dhand"] )
    mt.addrow ( ["oueiwjg","female","83","3o83-20-81","11222222"] )
    mt.printlist()
