from pathlib import Path
from zipfile import ZipFile

#Zip file
with ZipFile("files.zip", 'w') as zip:
  for path in  Path("ecommerce").rglob("*.*"):
    zip.write(path)
    
#Print and extract from zip
with ZipFile("files.zip") as zip:
  print(zip.namelist())
  info = zip.getinfo("ecommerce/__init__.py")
  print(info.file_size)
  print(info.compress_size)
  zip.extractall("extract")
