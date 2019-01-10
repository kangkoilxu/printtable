
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
import sys,string

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
        self.config_color_char()

    def config_color_char(self,l="|",r="|",u="-",d="-",c="+",s=" ",n="\n"):
        self.lborder = self.bcolor.format(l)
        self.rborder = self.bcolor.format(r)
        self.uborder = self.bcolor.format(u)
        self.dborder = self.bcolor.format(d)
        self.cornerchar = self.bcolor.format(c)
        self.wspace = s
        self.nline = n

    def p_list(self):
        print "Header:",self.hlist
        print "Rows:",self.list
        print "Length:",self.lenlist

    def set_bordercolor(self,ft):
        self.bcolor = "\033[" + str(ft) + "m{0}\033[0m"
        self.config_color_char()

    def set_fontcolor(self,ft):
        self.fcolor = "\033[" + str(ft) + "m{0}\033[0m"
        self.config_color_char()

    def set_align(self,al):
        if al not in ["center","left"]:
            print "\033[91mError: invalid alignment input\033[0m"
            sys.exit()
        self.align = al

    def wrap_text(self,txt):
        lenlist = []
        maxlen = 0
        if not len(txt):
            return
        for line in txt.split("\n"):
            lenlist.append(len(line))
        maxlen = max(lenlist)

        border_str = ""
        border_str += self.cornerchar + self.uborder*(maxlen+2) + self.cornerchar+self.nline
        for line in txt.split("\n"):
            if line.strip() == "":
                continue
            border_str += self.lborder + self.wspace + str(line.strip("\n")) + self.wspace*( maxlen - len(line) + 1) + self.rborder+self.nline
        border_str += self.cornerchar + self.uborder*(maxlen+2) + self.cornerchar + self.nline
        print border_str

    #TODO : string split issue ; use " "  will fail
    def remove_whitespace_sccharacter(self,slist): # remove whitespace and string control characters
        templist = []
        for item in slist:
            if item not in [ " ",""] :
                templist.append(item.strip().strip("\n").strip("\t"))
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
                    if not linecnt: #if it is the first line of the file, It should be the header
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
            self.body +=  self.nline + self.lborder
            for index,item in enumerate(tlist):
                if self.align == "center": # space + (half leng space ) + item + (halflen space)
                    odd = (self.lenlist[index] - len(item) ) % 2
                    halflen =  (self.lenlist[index] - len(item))/2 + 2#
                    self.body +=  self.wspace* halflen +  self.fcolor.format(str(item)) + self.wspace*(halflen+odd) + self.rborder #if the length of item is odd, add one space to right of item to balance len
                elif self.align == "left": #two spaces around the item
                    self.body += self.wspace + self.fcolor.format(str(item)) + self.wspace*(self.lenlist[index] - len(item))  + self.wspace + self.rborder #self.bcolor.format(" |")
            if is_header:
                self.body += self.nline + self.bcolor.format(self.header)

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
        self.header += self.cornerchar
        for item in self.lenlist:
            if self.align == "center":
                self.header += self.uborder*(item + 4) +self.cornerchar
            else :
                self.header += self.dborder*(item + 2)+self.cornerchar
        self.tail = self.nline + self.header

        #handle header
        if len(self.hlist):
            self.handlelist(self.hlist,is_header = True)
        if len(self.list):
            self.handlelist(self.list)
        print self.bcolor.format(self.header) \
        + self.fcolor.format( self.body ) \
        + self.bcolor.format( self.tail)
