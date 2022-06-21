# this opens the datafile, "noise.silo"
OpenDatabase("PATHtoDATA/noise.silo")
# this defines which type of plot we want to add
AddPlot("Pseudocolor" , "hardyglobal")
# this last command "draws" the plot, like pressing the draw button
DrawPlots()
