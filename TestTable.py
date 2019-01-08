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
    mt.printlist()


    mt2 = Table.Table()
    mt2.set_fontcolor(36)
    mt2.set_bordercolor(31)
    mt2.set_align("left")
    mt2.addheader( ["name","gender","age","birthday","nation"] )
    mt2.addrow(  ["opmdmlddddddd","male","32","1090-23-90","dhand"] )
    mt2.addrow ( ["oueiwjg","female","83","3o83-20-81","11222222"] )
    mt2.printlist()
