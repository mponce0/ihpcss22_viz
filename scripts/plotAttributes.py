p = PseudocolorAttributes()
p # will print out all attributes

p.min, p.max = 1, 3 # colour map range
p.minFlag, p.maxFlag = 1, 1 # turn it on
SetPlotOptions(p) # set active plot attributes

help(SetPlotOptions)

#Revert to the original colour map range:
p.minFlag , p.maxFlag = 0,0 # turn it off
SetPlotOptions(p)

#Pick a different colour map:
p. colorTableName = "Greens" # new colour map
SetPlotOptions(p)
