#!/usr/bin/python3


class Board(object):
	
	def __init__(self, players=None, board=None):

		initial_beads = 4


		if players==None:
			self.player_current = 'a'
			self.player_other = 'b'
		else:
			self.player_current = players[0]
			self.player_other = players[1]


		if board==None:
			self.gumot = {}
			for i in range(1,13): # Twelve gumot, six per player
				self.gumot[i] = initial_beads

			self.kupot = { self.player_current: 0, self.player_other: 0 }
		else:
			self.gumot = board['gumot']
			self.kupot = board['kupot']



	def display(self):

		g = self.gumot
		k = self.kupot

		print('')
		print('        %s' %(self.player_other, ))
		print('+======+======+======+======+======+======+======+======+')

		print('|      ', end='')
		for i in range(7,13):
			print('|  %02d  ' %g[i], end='')
		print('|  vv  |')

		print('+  %02d  +------+------+------+------+------+------+  %02d  +' % (k[self.player_other],k[self.player_current],))

		print('|      ', end='')
		for i in range(6,0,-1):
			print('|  %02d  ' % g[i], end='')
		print('|  ^^  |')

		print('+======+======+======+======+======+======+======+======+')
		print('  ** ** %s ** **' %(self.player_current, ))

		return True



	def swap_sides(self):

		# Swap players
		self.player_current, self.player_other = self.player_other, self.player_current

		# Swap gumot
		temp = self.gumot.copy()
		for i in range(1,7):
			self.gumot[i] = temp[i+6]
		for i in range(7,13):
			self.gumot[i] = temp[i-6]

		return True



def main():
	b = Board()
	b.display()

	return True



if __name__=='__main__':
	main()
