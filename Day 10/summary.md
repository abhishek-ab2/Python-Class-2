## Covered Topics
- Packages/Modules/library

### import 
- Used to import from libraries/modules/packages

Syntax:

from <module_name> import <obj_name> as <alias_name> # Importing a specific object from module

import <module_name> as <alias_name> # Importing the whole module

from <package_name>.<module_name> import <obj_name> # Importing from packages
import <package_name>.<module_name>
import <package_name>

#### Relative imports 
from . import module1 # import from current path/directoty
from .module1 import func_of_m1 # import a specific object from module
from .<package_name>.<module_name> import <obj_name> # Importing from packages in relative import

#### Naming convention
module > package/library > frameworks


#### Precedence:
Local Directory
Built - imports
Third-party packages


### Commonly used - built in packages
os
sys
threading
math
functools


### Third party packages
numpy - multidimensional arrays
scipy
pandas
tkinter
pyqt
django


### Assignment:
- Install any third-party package, mention its uses. 
- Create a package (no nesting, no sub-packages) and import a function or object from any of the modules.
