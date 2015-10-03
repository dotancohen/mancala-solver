#!/usr/bin/python3


class Board(object):
	
	def __init__(self, players=None, board=None):

		initial_beads = 4


		if players==None:
			self.player_current = 'First Player'
			self.player_other = 'Second Player'
		else:
			self.player_current = players[0]
			self.player_other = players[1]


		if board==None:
			self.gumot = {}
			for i in range(1,13): # Twelve gumot, six per player
				self.gumot[i] = initial_beads

			self.kupot = { 'current': 0, 'other': 0 }
		else:
			self.gumot = board['gumot']
			self.kupot = board['kupot']



	def display(self, show_choose=True):

		g = self.gumot
		k = self.kupot

		print('')
		print('        %s' %(self.player_other, ))
		print('+======+======+======+======+======+======+======+======+')

		print('|      ', end='')
		for i in range(7,13):
			print('|  %02d  ' %g[i], end='')
		print('|  vv  |')

		print('+  %02d  +------+------+------+------+------+------+  %02d  +' % (k['other'],k['current'],))

		print('|      ', end='')
		for i in range(6,0,-1):
			print('|  %02d  ' % g[i], end='')
		print('|  ^^  |')

		print('+======+======+======+======+======+======+======+======+')
		if show_choose:
			print('Choose:     6      5      4      3      2      1')
		print('  ** ** %s ** **' %(self.player_current, ))
		print('')

		return True



	def swap_sides(self):

		# Swap players
		self.player_current, self.player_other = self.player_other, self.player_current

		# Swap kupot
		self.kupot['current'], self.kupot['other'] = self.kupot['other'], self.kupot['current']

		# Swap gumot
		temp = self.gumot.copy()
		for i in range(1,7):
			self.gumot[i] = temp[i+6]
		for i in range(7,13):
			self.gumot[i] = temp[i-6]

		return True


def move_melissa(board, ):

		return True



def main():

	test_board = { 'gumot':{}, 'kupot':{'current':9, 'other':7} }
	for i in range(1,13):
		test_board['gumot'][i] = i

	#b = Board()
	#b = Board(players=['Meirav', 'Maayan'])
	b = Board(players=['Meirav', 'Maayan'], board=test_board)

	b.display(show_choose=False)
	b.swap_sides()
	b.display()

	return True



if __name__=='__main__':
	main()
