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

		print('+======+======+======+======+======+======+======+======+')

		print('|      ', end='')
		for i in range(7,13):
			print('|  %02d  ' %g[i], end='')
		print('|      |')

		print('+  %02d  +------+------+------+------+------+------+  %02d  +' % (k[0],k[1],))

		print('|      ', end='')
		for i in range(6,0,-1):
			print('|  %02d  ' % g[i], end='')
		print('|      |')

		print('+======+======+======+======+======+======+======+======+')

		return True



def main():
	b = Board()
	b.display()

	return True



if __name__=='__main__':
	main()
