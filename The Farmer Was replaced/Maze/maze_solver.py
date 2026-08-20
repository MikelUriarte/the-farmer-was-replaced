clear()
size = get_world_size()

# ---------------- CREATE MAZE ----------------

def create_maze():
	# Plant a bush to create the maze.
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Bush)
	
	# Calculate the required amount of Weird Substance.
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)


# ---------------- SOLVE MAZE ----------------

def turn_right(direction):
	if direction == North:
		return East
	if direction == East:
		return South
	if direction == South:
		return West
	if direction == West:
		return North


def turn_left(direction):
	if direction == North:
		return West
	if direction == West:
		return South
	if direction == South:
		return East
	if direction == East:
		return North


def solve_maze():
	# Algorithm: Right-Hand Rule.
	direction = North  # Initial direction
	
	while get_entity_type() != Entities.Treasure:
		# Try turning right.
		right_dir = turn_right(direction)

		if move(right_dir):
			direction = right_dir

		# If right is blocked, try moving forward.
		elif move(direction):
			pass

		# If forward is blocked, turn left.
		else:
			direction = turn_left(direction)
	
	# Treasure found.
	harvest()


# ---------------- MAIN LOOP ----------------

while True:
	create_maze()
	solve_maze()