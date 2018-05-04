import  socket
from colorama import init, AnsiToWin32
print('''   ,---,.            ,--,               ,--,           
  ,'  .'  \  ,--,   ,--.'|             ,--.'|           
,---.' .' |,--.'|   |  | :             |  | :           
|   |  |: ||  |,    :  : '             :  : '           
:   :  :  /`--'_    |  ' |      ,---.  |  ' |           
:   |    ; ,' ,'|   '  | |     /     \ '  | |           
|   :     \'  | |   |  | :    /    /  ||  | :           
|   |   . ||  | :   '  : |__ .    ' / |'  : |__         
'   :  '; |'  : |__ |  | '.'|'   ;   /||  | '.'|        
|   |  | ; |  | '.'|;  :    ;'   |  / |;  :    ;        
|   :   /  ;  :    ;|  ,   / |   :    ||  ,   /         
|   | ,'   |  ,   /  ---`-'   \   \  /  ---`-'          
`----'      ---`-'             `----' ''')
server = raw_input('Enter your website : ')

def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((server,port))
        return True
    except:
        return False
for x in range(0,100000):
    if pscan(x):
        print('Port',x,'is open')
    else:
        print('Port',x,'is closed')
