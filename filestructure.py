import os
def printDir(pth):
   if os.path.isfile(pth):
      print( "\n|-" + pth)
   else:
      print("\n\nDirectory - " + pth)
      for i in os.listdir(pth):
         printDir(pth +"/" +i)
         

initialPath = "/Users/pranav/DocuSummary/shipments"
os.chdir(initialPath)
printDir(initialPath)
    

