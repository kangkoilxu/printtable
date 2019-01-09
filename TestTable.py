import Table

if __name__ == "__main__":

    mt = Table.Table()
    mt.set_fontcolor(97)
    mt.set_bordercolor(92)
    mt.set_align("center")
    mt.addheader( ["name","gender","age","birthday","nation"] )
    mt.addrow(  ["opmdmlwk","male","32","1090-23-90","dhand"] )
    mt.addrow ( ["oueiwjg","female","83","3o83-20-81","11222222"] )
    mt.addrow ( ["oueiwjg","female","83","3o83-20-81",""] )
    mt.printtable()

    #
    mt2 = Table.Table()
    mt2.set_fontcolor(36)
    mt2.set_bordercolor(31)
    mt2.set_align("left")
    mt2.addrow( ["This ","a","test","table","which","doesn't","has","a","header"] )
    mt2.printtable()

    #read from text
    mt3 = Table.Table()
    mt3.set_align("left")
    mt3.add_fromtext("textsample.txt",spstr = " ")
    mt3.printtable()


    #use custom split characters
    mt4 = Table.Table()
    mt4.set_align("left")
    mt4.add_fromtext("sampletexttable2.txt",spstr = ":")
    # mt4.p_list()
    mt4.printtable()
