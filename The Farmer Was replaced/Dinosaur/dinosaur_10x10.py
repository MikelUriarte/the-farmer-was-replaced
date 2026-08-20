# ---------------- DINOSAUR 10x10 ----------------
#
# Controls the dinosaur through a 10x10 world using a
# predefined movement pattern. When the dinosaur reaches
# an obstacle, it returns to the starting position and
# restarts the route.

def go_home():
	while get_pos_x() != 0:
		move(West)

	while get_pos_y() != 0:
		move(South)


def restart():
	change_hat(Hats.Straw_Hat)
	go_home()
	change_hat(Hats.Dinosaur_Hat)
	dinosaur()


def move_north():
	if move(North) == False:
		if move(North) == False:
			if move(North) == False:
				restart()


def move_east():
	if move(East) == False:
		if move(East) == False:
			if move(East) == False:
				restart()


def move_south():
	if move(South) == False:
		if move(South) == False:
			if move(South) == False:
				restart()


def move_west():
	if move(West) == False:
		if move(West) == False:
			if move(West) == False:
				restart()


def dinosaur():
	while True:

		# Row 1
		for _ in range(9):
			move_north()

		# Row 2
		for _ in range(9):
			move_east()
		move_south()

		# Row 3
		for _ in range(8):
			move_west()
		move_south()

		# Row 4
		for _ in range(8):
			move_east()
		move_south()

		# Row 5
		for _ in range(8):
			move_west()
		move_south()

		# Row 6
		for _ in range(8):
			move_east()
		move_south()

		# Row 7
		for _ in range(8):
			move_west()
		move_south()

		# Row 8
		for _ in range(8):
			move_east()
		move_south()

		# Row 9
		for _ in range(8):
			move_west()
		move_south()

		# Row 10
		for _ in range(8):
			move_east()
		move_south()

		# Return across the final row.
		for _ in range(9):
			move_west()


# ---------------- MAIN ----------------

set_world_size(10)

change_hat(Hats.Straw_Hat)
go_home()

change_hat(Hats.Dinosaur_Hat)

while True:
	dinosaur()