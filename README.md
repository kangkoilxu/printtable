##Python class for print tables


#Features:
	* support center and left alignments
	* support single line table

#example :

    mt = Table.Table()
    mt.set_fontcolor(97)
    mt.set_bordercolor(92)
    mt.set_align("center")
    mt.addheader( ["name","gender","age","birthday","nation"] )
    mt.addrow(  ["opmdmlwk","male","32","1090-23-90","dhand"] )
    mt.addrow ( ["oueiwjg","female","83","3o83-20-81","11222222"] )
    mt.addrow ( ["oueiwjg","female","83","3o83-20-81",""] )
    mt.printlist()


output:

+------------+----------+-------+--------------+------------+
|    name    |  gender  |  age  |   birthday   |   nation   |
+------------+----------+-------+--------------+------------+
|  opmdmlwk  |   male   |  32   |  1090-23-90  |   dhand    |
|  oueiwjg   |  female  |  83   |  3o83-20-81  |  11222222  |
|  oueiwjg   |  female  |  83   |  3o83-20-81  |            |
+------------+----------+-------+--------------+------------+


