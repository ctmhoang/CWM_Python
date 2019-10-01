from pathlib import Path

Path(r"C:\Program Files\Microsoft")
path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
#path.withname("file.txt") #change name and extension of file
path = path.with_suffix(".txt")
print(path)
print(path.absolute())
