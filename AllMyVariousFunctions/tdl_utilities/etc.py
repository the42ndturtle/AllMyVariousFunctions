from time import sleep 
from AllMyVariousFunctions.tdl_utilities import printf
from tdl import *
def etc(x, y, con):
	sleep(.2)
	printf(x, y, "Press enter to continue...", con)
	tdl.flush()
	while 1:
		k = tdl.event.key_wait()
		if k.keychar == "ENTER":
			break