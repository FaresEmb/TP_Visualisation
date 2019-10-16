from zipfile import ZipFile

# Load brut.zip
with ZipFile('data/brut.zip', 'r') as zipObj:
   
   # Get list of files names in zip
   listOfiles = zipObj.namelist()
   # Iterate over the list of file names in given list & print them
   for elem in listOfiles:
       print(elem)