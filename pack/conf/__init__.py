import sys
import pathlib
#sys.path.append('C:\\Users\\usuario\\Desktop\\TEST')

# defining variables to define path and others
#file_parents = pathlib.Path(__file__).parents

# adding the project folder to path
#sys.path.append(file_parents[1].as_posix())

from pack.conf import file_managment
from pack.conf import module_managment

__all__=["file_managment","module_managment"]
