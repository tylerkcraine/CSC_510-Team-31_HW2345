E_OPTION = "eg"
D_OPTION = "dump"
F_OPTION = "file"
H_OPTION = "help"
N_OPTION = "nums"
SMALL_S_OPTION = "seed"
BIG_S_OPTION = "separator"

HELP_STRING = """
CSV : summaried csv file
(c) Fall 2022 CSC 510 Team 31 
<ntgomes,tylerkcraine,AbhimanyuBellam,guptaabhishek785,vishalveerareddy> 
MIT license

USAGE: python src/__init__.py [OPTIONS]

OPTIONS:
 -e  --""" + E_OPTION + """        start-up example                      =nothing 
 -d  --""" + D_OPTION + """        on test failure exit with stack dump  =false 
 -f  --""" + F_OPTION + """        file with csv data                    =./data/auto93.csv 
 -h  --""" + H_OPTION + """        show help                             =false 
 -n  --""" + N_OPTION + """        number of nums to keep                =512 
 -s  --""" + SMALL_S_OPTION + """  random number seed                    =10019 
 -S  --""" + BIG_S_OPTION + """    field separator                       =,"""