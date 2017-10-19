from time import sleep
from AllMyVariousFunctions.tdl_utilities import center
from tdl import *
def cetc(y, con):
	sleep(.2)
	center(y, "Press enter to continue...", con)
	tdl.flush()
	while 1:
		k = tdl.event.key_wait()
		if k.keychar == "ENTER":
			break