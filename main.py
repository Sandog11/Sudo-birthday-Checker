from datetime import date
from sudo import creationdate
today = date.today()



d1 = today.strftime("%d/%m")
print("today is", d1)
class bcolors:
    Happy = "\033[92m"
    Orange = "\033[33m"
    Red = "\033[91m"
    
if(creationdate == d1):
    print(bcolors.Happy + """\ ██░ ██  ▄▄▄       ██▓███   ██▓███ ▓██   ██▓    ▄▄▄▄    ██▓ ██▀███  ▄▄▄█████▓ ██░ ██ ▓█████▄  ▄▄▄     ▓██   ██▓
▓██░ ██▒▒████▄    ▓██░  ██▒▓██░  ██▒▒██  ██▒   ▓█████▄ ▓██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓██░ ██▒▒██▀ ██▌▒████▄    ▒██  ██▒
▒██▀▀██░▒██  ▀█▄  ▓██░ ██▓▒▓██░ ██▓▒ ▒██ ██░   ▒██▒ ▄██▒██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒██▀▀██░░██   █▌▒██  ▀█▄   ▒██ ██░
░▓█ ░██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██▄█▓▒ ▒ ░ ▐██▓░   ▒██░█▀  ░██░▒██▀▀█▄  ░ ▓██▓ ░ ░▓█ ░██ ░▓█▄   ▌░██▄▄▄▄██  ░ ▐██▓░
░▓█▒░██▓ ▓█   ▓██▒▒██▒ ░  ░▒██▒ ░  ░ ░ ██▒▓░   ░▓█  ▀█▓░██░░██▓ ▒██▒  ▒██▒ ░ ░▓█▒░██▓░▒████▓  ▓█   ▓██▒ ░ ██▒▓░
 ▒ ░░▒░▒ ▒▒   ▓▒█░▒▓▒░ ░  ░▒▓▒░ ░  ░  ██▒▒▒    ░▒▓███▀▒░▓  ░ ▒▓ ░▒▓░  ▒ ░░    ▒ ░░▒░▒ ▒▒▓  ▒  ▒▒   ▓▒█░  ██▒▒▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░▒ ░     ░▒ ░     ▓██ ░▒░    ▒░▒   ░  ▒ ░  ░▒ ░ ▒░    ░     ▒ ░▒░ ░ ░ ▒  ▒   ▒   ▒▒ ░▓██ ░▒░ 
 ░  ░░ ░  ░   ▒   ░░       ░░       ▒ ▒ ░░      ░    ░  ▒ ░  ░░   ░   ░       ░  ░░ ░ ░ ░  ░   ░   ▒   ▒ ▒ ░░  
 ░  ░  ░      ░  ░                  ░ ░         ░       ░     ░               ░  ░  ░   ░          ░  ░░ ░     
                                    ░ ░              ░                                ░                ░ ░     
  ██████  █    ██ ▓█████▄  ▒█████                                                                              
▒██    ▒  ██  ▓██▒▒██▀ ██▌▒██▒  ██▒                                                                            
░ ▓██▄   ▓██  ▒██░░██   █▌▒██░  ██▒                                                                            
  ▒   ██▒▓▓█  ░██░░▓█▄   ▌▒██   ██░                                                                            
▒██████▒▒▒▒█████▓ ░▒████▓ ░ ████▓▒░                                                                            
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░                                                                             
░ ░▒  ░ ░░░▒░ ░ ░  ░ ▒  ▒   ░ ▒ ▒░                                                                             
░  ░  ░   ░░░ ░ ░  ░ ░  ░ ░ ░ ░ ▒                                                                              
      ░     ░        ░        ░ ░         
      """)
    print(bcolors.Orange + """\..            ...####...........((((##(((((((((((((((((((((####################################################..........,######(     ...            .
         ...     ####/...........##(((((((((((((((((((((###################################################((............###(((((...            ...   
    ..           (####............((((((((((((((((((##################################################((((((............/(((((((           ...        
.             ..  ##(((/...........(((((((((((((###################(*,*****,*((######(############(((((((##*.........../((((((((     ....          ...
        ...       (((###(.........../((((((((#############(*****,***************,******(######(((((((######...........(((((((((,...           ........
  ...            ..#((/((((...........(((#############(*********,************************,,,/((((#########...........(,../(((((         ....... ......
             .     ,(((......(...........#########(,************(#################(**,,,,,,,,***(######((*..............((((((     ....... ...........
                    /(((............,##########(,*********,######################(((((((/**********/((((.(((........../((((((..(((( . ................
  .               /((((((..............#######**,******#####################(((((((((#######(**,,,,,,/(((((.........(((/,,((((((((....................
                  (((((((##.............####********####################(((((((((##########(((((,,,,,,,/((((/....../,,,,,,,,(((###.................,,.
                   ((#########(..........(,******(##################((((((((###########(((((((((((/,,,,,,/....../,,,,,,,,,**#####.............,,......
                 ..  ##########.........*******#################((((((((###########((((((((((((((((((,,,,,,...,,,,,,,,******(##,.........,............
             . /######(*(#########(....******##############(((((((((###########(((((((((((*********((((,,,(,,,,,,,**********#/.(##...............,,,,,
                  ,#(*********(#######*****(######////#(((((((((###########((((((((((((***************((,,,,((************(*(###............,,,,,.....
..            ..... /***********,**##/,,**(###/////********(###########(((((((((((((((*****************(#****###(********(**################..........
         .....      ((**************##,***##///********//////######((((((((((((((((((*************(((####*****####******(**(##############......,,,...
   ....#########(....,(*,***,***,*(##(**,(#(*******///////////#(((((((((((((((((((((********/((((########%****#####****(***###########((*..,,,........
...   . ##############***********####**,,*(((((#####////////**/(((((((((((((((((((((****(((((#######///###*****###//**(***########((((,,,............,
 .........#############,*(******(##(/,,,,/(############(((/****((((((((((((((((((((((((((##########////###*****#///#/*****####(((((#...,((((#..,,,,,,,
...........#############***/**,,**((/,,**/#########(((((((((((((((((((((((((((((((((###############///####*****(///##****#((((((((((((((((((,,,,.,,,,,
***..........##(***######,,,,,,/(*//(*****##///*((((((((((((((((((((((((((((((((##//##############//######*****##(//**,,(((((((((((((((((((,,,,,.,,(/,
**/........./*******##((((/,,,*##///#*****#(((***/((((((((((((((((*(((((((((#####################//#######*****###(*,,/((((((((((/*****/((*,,,,,,,,***
.*(.......(***,,,,,,((((((##****//###,*,,,,((((((**(((((((((((((((((((((########################//#######%****(((((,,((((((((((((*****,***,,,,,,,,,**,
,*(...,,(**/,,....,,((#######((**##(((,,,,,/(((((((**((((((((((((((########################//////########**,,,((((,(((((((((#((((**,,,,,,***,,,,,,,*/,
,*/...(***........**#######(***,*,(((((,,,,,(((((((((**((((((((#######////////////########//(##########((,,,,((//((((*,*,/((((((((**,,,,,,,*****,,,*/,
,*/,,*,,,.....,,,,*(#####(*,,,,,,(,(((((,,,,,((((((((((****//#####////#############////////########(((((,,,,/(((((((/******((#####*/,,,,,,,,/***,,,*/,
,*./,,,...,,,,,,,**####(,,,....,,/(((,(((,,,,,((((((((#######/////#############################((((((((/((((((((((((**,,,,***####(**,,,,,,,,,,***(**/,
,,,,,,**,,,,,,,,**((((,,,......*,,(((((((/(,,,,(((#########################################((((((((((((((((((((((((***,,,,,,***(*,/**,,,,,,,,,****/**,
((#######/*****,,,((/,,.........,,((((((((((((#########################################(((((((((((/((((((((((((((##**/,,,,,,,,**(##*******************
###########((((((((,,,.........,,,(((((((###########(##############################(((((((((((((((((((((((((#######***,,,,,,,,,***##*#################
#######((((((((((((((,,,......*,,,(((##########################################(((((((((((((((((((((((((##########(/***,,,,,,,***#####################
##(((((((((((((((((((((,,,...*,,*##########################################(((((((((((((((((((((((((##########((((((****,,,***########################
********/((((((((((((((((,,*****###(***#########################(######(((((((((((((((((((((((((##########((((****###(******##############///////(/((#
************(((((((((((###****/********(###########################((((///(////((((((((((((############(((((((*********(***/###########//////(((((((((
""")
else:
    print(bcolors.Red + """\███    ██  ██████  ████████     ████████  ██████  ██████   █████      ██         ██ 
████   ██ ██    ██    ██           ██    ██    ██ ██   ██ ██   ██  ██  ██      ██ ██  
██ ██  ██ ██    ██    ██           ██    ██    ██ ██   ██ ███████   ████          ██  
██  ██ ██ ██    ██    ██           ██    ██    ██ ██   ██ ██   ██    ██        ██ ██  
██   ████  ██████     ██           ██     ██████  ██████  ██   ██    ██             ██ 
                                                                                      
""")
    print("sudo's birthday is on", creationdate)
    

