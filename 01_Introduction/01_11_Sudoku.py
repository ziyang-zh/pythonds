import numpy as np

sudoku=np.array([
	[0,5,0,0,6,1,0,0,0],
	[0,1,4,0,3,8,0,0,6],
	[6,0,0,0,0,0,7,5,1],
	[8,0,2,0,0,7,3,0,0],
	[4,0,0,0,2,0,0,0,5],
	[0,0,0,4,8,0,0,7,0],
	[0,0,6,3,0,0,1,0,0],
	[0,7,1,0,0,0,9,0,0],
	[0,0,0,6,0,9,0,2,7]
	])

def run_app():
	try:
		row,col=get_zero()
	except TypeError:
		return

	for i in range(1,10):
		if can_put(i,row,col):
			sudoku[row,col]=i
			run_app()
			sudoku[row,col]=0

def get_zero():
	try:
		return np.argwhere(sudoku==0)[0]
	except IndexError:
		print(sudoku)
		exit(0)

def can_put(number,row,col):
	return check_row(number,row) and check_col(number,col) and check_square(number,row,col)

def check_row(number,row):
	return not sudoku[row,:].__contains__(number)
	#return number not in sudoku[row,:]

def check_col(number,col):
	return not sudoku[:,col].__contains__(number)

def check_square(number,row,col):
	x=row//3*3
	y=col//3*3
	return not sudoku[x:x+3,y:y+3].__contains__(number)

if __name__=="__main__":
	run_app()
	print(sudoku)


