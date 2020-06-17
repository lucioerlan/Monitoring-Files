
from CONTROLLER import funcoes as f


#Colors
W = '\033[0m'  # white
R = '\033[31m' # red

try:
    ff = f.funcoes()
    ff.banner()
    ff.chooseDep()
    ff.displaysMenu()
    ff.chooseOption()

except KeyboardInterrupt:
    print('\n\n\n\n' +  R + 'Program Ended!'+ W)