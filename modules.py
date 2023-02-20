## Creating Modules
    # Modules are files 
    # How to decide which functions or classes
    # snake writing for files
def calc_tax():
    pass

def calc_shipping():
    pass
    # import from other files
    # to import all use from sales import *
    # for specific function/classes
        # from file_name import function, class
        # does not need relative path
    # can also use the import file_name
        # then use the dot notation to implement functions 

## Compiled Python Files
    # first running will add folder in __pycache__

## Module Search Path
    # import sys
        # sys.path will show you all the paths python looks through to find the right folder

## Packages
    # adding sub folders
    # a package is for one or more files
    # to import from separate folders
        # import folder_name.file_name   
        # from folder_name.file_name import function, class
    # for multiple functions/classes
        # from folder_name import file_name
    # to get all files in folder
        # MUST ADD __init__.py

## Sub-packages
    # sub_package are files in files
    # MUST ADD __init__.py
    # from folder.sub_folder import file

## Intra-package References
    # best practice is absolute import
    # absolute import
        # from folder.sub_folder import file
    # dot import
        # from ..sub_folder import file

## The dir Function
    # you can get a list of methods and attributes in a file
    # mainly for debugging
        # dir(imported_file)

## Executing Modules as Scripts
    # go to the __init__.py

           