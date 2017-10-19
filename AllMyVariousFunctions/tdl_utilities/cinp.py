from tdl import *
from center import center
lowercase = 'abcdefghijklmnopqrstuvwxyz`1234567890[];\',./'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*(){}:"<>?'
def cinp(y, limit, con):
	var = ''
	while 1:
		k = tdl.event.key_wait()
		if k.keychar == "ENTER":
			break
		elif k.keychar != '' and k.shift:
			var += uppercase[lowercase.find(k.keychar):lowercase.find(k.keychar)+1]
		elif k.keychar == 'BACKSPACE':
			var = var[:len(var)-1]
		else:
			var += k.char
		if len(var) > limit:
			var = var[:len(var)-1]
		center(y, ' '*limit, con)
		center(y, var, con)
	return var