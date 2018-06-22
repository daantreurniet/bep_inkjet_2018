## ==== IMPORT SCRIPTS ====
import binascii
from hex_functions import *
from esc_functions import *




def createPs(x,r=b'\x00', size=1):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5])
	list2 = createnozzlelistsp(29,[1,3])
	list3 = createnozzlelistsp(29,[1,2,3])
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total



def createMs(x,size=1, r=b'\x00'):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5])
	list2 = createnozzlelistsp(29,[2])
	list3 = createnozzlelistsp(29,[1,2,3,4,5])
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total




def createEs(x,r=b'\x00', size=1):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5])
	list2 = createnozzlelistsp(29,[1,3,5])
	list3 = createnozzlelistsp(29,[1,5])
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
#






def createP(x,r=b'\x00', size=1,fn=0):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5,6,7],fn)
	list2 = createnozzlelistsp(29,[1,4],fn)
	list3 = list2
	list4 = list2
	list5 = createnozzlelistsp(29,[2,3],fn)
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size) + ESC_dollar(hor,x+3*dx) + ESC_i_nrs(list4,r,size) + ESC_dollar(hor,x+4*dx) + ESC_i_nrs(list5,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
	
	
def createE(x,r=b'\x00', size=1,fn=0):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5,6,7],fn)
	list2 = createnozzlelistsp(29,[1,4,7],fn)
	list3 = list2
	list4 = list2
	list5 = createnozzlelistsp(29,[1,7],fn)
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size) + ESC_dollar(hor,x+3*dx) + ESC_i_nrs(list4,r,size) + ESC_dollar(hor,x+4*dx) + ESC_i_nrs(list5,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
	
def createM(x,r=b'\x00', size=1,fn=0):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5,6,7],fn)
	list2 = createnozzlelistsp(29,[2],fn)
	list3 = createnozzlelistsp(29,[3,4],fn)
	list4 = list2
	list5 = list1
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size) + ESC_dollar(hor,x+3*dx) + ESC_i_nrs(list4,r,size) + ESC_dollar(hor,x+4*dx) + ESC_i_nrs(list5,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
	


def createN(x,r=b'\x00', size=1,fn=0):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5,6,7],fn)
	list2 = createnozzlelistsp(29,[3],fn)
	list3 = createnozzlelistsp(29,[4],fn)
	list4 = createnozzlelistsp(29,[5],fn)
	list5 = list1
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size) + ESC_dollar(hor,x+3*dx) + ESC_i_nrs(list4,r,size) + ESC_dollar(hor,x+4*dx) + ESC_i_nrs(list5,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
#


def createD(x,r=b'\x00', size=1,fn=0):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5,6,7],fn)
	list2 = createnozzlelistsp(29,[1,7],fn)
	list3 = list2
	list4 = list2
	list5 = createnozzlelistsp(29,[2,3,4,5,6],fn)
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size) + ESC_dollar(hor,x+3*dx) + ESC_i_nrs(list4,r,size) + ESC_dollar(hor,x+4*dx) + ESC_i_nrs(list5,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
#

def createL(x,r=b'\x00', size=1,fn=0):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5,6,7],fn)
	list2 = createnozzlelistsp(29,[7],fn)
	list3 = list2
	list4 = list2
	list5 = list2
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size) + ESC_dollar(hor,x+3*dx) + ESC_i_nrs(list4,r,size) + ESC_dollar(hor,x+4*dx) + ESC_i_nrs(list5,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
#

def createF(x,r=b'\x00', size=1,fn=0):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5,6,7],fn)
	list2 = createnozzlelistsp(29,[1,4],fn)
	list3 = list2
	list4 = list2
	list5 = createnozzlelistsp(29,[1],fn)
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size) + ESC_dollar(hor,x+3*dx) + ESC_i_nrs(list4,r,size) + ESC_dollar(hor,x+4*dx) + ESC_i_nrs(list5,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
#

def createT(x,r=b'\x00', size=1,fn=0):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1],fn)
	list2 = list1
	list3 = createnozzlelistsp(29,[1,2,3,4,5,6,7],fn)
	list4 = list1
	list5 = list1
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size) + ESC_dollar(hor,x+3*dx) + ESC_i_nrs(list4,r,size) + ESC_dollar(hor,x+4*dx) + ESC_i_nrs(list5,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
#


def createU(x,r=b'\x00', size=1,fn=0):
	dy = 0
	dx = (dy+1)*(1/120)
	hor = 5760
	
	list1 = createnozzlelistsp(29,[1,2,3,4,5,6],fn)
	list2 = createnozzlelistsp(29,[7],fn)
	list3 = list2
	list4 = list2
	list5 = list1
	m = len(list1)
	prefix = b'\x1b' + str_hex('i') # ESC i
	c = b'\x01' # COMPRESSED
	b = b'\x02'
	n = 1
	nL = dec_hex(n % 256)
	nH = dec_hex(n/256)
	mL = dec_hex(m % 256)
	mH = dec_hex(m/256)
	
	image = ESC_dollar(hor,x) + ESC_i_nrs(list1,r,size) + ESC_dollar(hor,x+dx) + ESC_i_nrs(list2,r,size) + ESC_dollar(hor,x+2*dx) + ESC_i_nrs(list3,r,size) + ESC_dollar(hor,x+3*dx) + ESC_i_nrs(list4,r,size) + ESC_dollar(hor,x+4*dx) + ESC_i_nrs(list5,r,size)
	
	# suffix1 = b'\x0d' #b'\x0d\x0c'
	total = image
	
	return total
#




def printTUDELFT(x=5,y=3,size=3):
	pmgmt = 720
	hor = 5760
	vert = 720
	black = b'\x00'
	dy = 0
	dx = (dy+1)*(1/120)
	size1 = size
	size2 = size
	
	rasterdata = ESC_v(pmgmt,y) + createT(x,black,size1) + createU(x+6*dx,black,size1) + createD(x+18*dx,black,size1) + createE(x+dx*24,black,size2) + createL(x+30*dx,black,size2) + createF(x+36*dx,black,size2) + createT(x+42*dx,black,size2) + b'\x0c'
	return rasterdata
	
def printTUPME(x=5,y=3,size=3):
	pmgmt = 720
	hor = 5760
	vert = 720
	black = b'\x00'
	dy = 0
	dx = (dy+1)*(1/120)
	size1 = 3
	size2 = 3
	
	rasterdata1 = ESC_v(pmgmt,y) + createT(x,black,size1) + createU(x+6*dx,black,size1) + createD(x+18*dx,black,size1) + createE(x+dx*24,black,size1) + createL(x+30*dx,black,size1) + createF(x+36*dx,black,size1) + createT(x+42*dx,black,size1)
	rasterdata2 = createP(x,black,size1,10) + createM(x+6*dx,black,size1,10) + createE(x+12*dx,black,size1,10) + createM(x+dx*20,black,size2,10) + createN(x+26*dx,black,size2,10) + createE(x+32*dx,black,size2,10)
	
	rasterdata = rasterdata1+rasterdata2+b'\x0c'
	return rasterdata
#



def printLOGO(matrix,x=5.5,y=3,size=3,r=b'\x00'):
	# if len(matrix) >= 30:
		# print('matrix dimensions error')
	pmgmt = 720
	hor = 5760
	vert = 720
	black = r
	dy = 0
	dx = (dy+1)*(1/120)
	# size1 = 3
	# size2 = 3
	
	rasterdata = b''
	
	for k in range(len(matrix)):
		rasterdata += (ESC_dollar(hor,x+k*dx) + ESC_i_nrs(matrix[k],black,size))
	image = rasterdata
	return image
#











## LOGO DATA FOR PER DOT PRINTING
def loadlogo(logo=1):
	if logo == 1:
		matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
	if logo == 2:
		matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0]]
	if logo == 3:
		matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]
	return matrix
#










def load_logo_fast():
	a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0]]
	return a
