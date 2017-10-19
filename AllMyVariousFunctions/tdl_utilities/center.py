from tdl import *
def center(y, text, con):
	con.draw_str((con.width/2)-(len(text)/2), y, text)
	tdl.flush()