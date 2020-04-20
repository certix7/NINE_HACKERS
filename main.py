








# Console colors
bg ='' # '\033[44m'  # gray
W = bg+'\033[0m'  # white (normal)
R = bg+'\033[31m'  # red
G = bg+'\033[32m'  # green
O = bg+'\033[33m'  # orange
B = bg+'\033[34m'  # blue
P = bg+'\033[35m'  # purple
C = bg+'\033[36m'  # cyan
GR = bg+'\033[37m'  # gray
Y="\033[33m"

logo=Y+'''
   ____  U _____ u U  ___ u       ____     ____    U  ___ u 
U /"___|u\| ___"|/  \/"_ \/    U | __")uU |  _"\ u  \/"_ \/ 
\| |  _ / |  _|"    | | | |     \|  _ \/ \| |_) |/  | | | | 
 | |_| |  | |___.-,_| |_| |      | |_) |  |  _ <.-,_| |_| | 
  \____|  |_____|\_)-\___/       |____/   |_| \_\\_)-\___/  
  _)(|_   <<   >>     \\        _|| \\_   //   \\_    \\    
 (__)__) (__) (__)   (__)      (__) (__) (__)  (__)  (__)   

'''+C

print(logo)
print("created by A_naser present for the good course and freindship\n")
from   EXPLOIT  import *
from OSINT import *
from  Scanning  import *
if __name__ == '__main__':

	options=['\033[34m1-OSINT','\033[33m2-SCANING','\033[35m3-EXPLOIT',"4-exit [*]"]
	for i in options:    print(i)


	opt=input (R+"put your option pls :"+G) 
	if opt == "1":

		osint()
	elif opt=="2":
		scan()
	elif opt=="3":
		exploit()
	elif opt=="*":
		exit()
		


