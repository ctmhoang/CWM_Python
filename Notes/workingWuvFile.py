from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")
Path.exists()
path.rename("init.txt")
path.unlink()
path.stat().st_ctime #replace for st_mtime
path.read_text()
path.write_text("...")
path.write_bytes()

# shutil.copy(src,targ)
