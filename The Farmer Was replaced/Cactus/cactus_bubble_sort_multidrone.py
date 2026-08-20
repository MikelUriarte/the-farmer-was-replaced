clear()
size = get_world_size()

# Cactus sorting using multiple drones.
#
# Each drone starts from a different row and performs a sorting pass
# across the entire field. Multiple drones work in parallel to reduce
# the time required to sort the cactus field.

# ---------------- UTILITIES ----------------

def reverse(d):
	if d == East:  
		return West
	if d == West:  
		return East
	if d == North: 
		return South
	if d == South: 
		return North

def plant_cactus():
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Cactus)

# ---------------- 1. PLANTING ----------------

def plant_all():
	def row():
		for _ in range(get_world_size()):
			harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Cactus)
	
			move(East)

	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

# ---------------- 2. SORTING ----------------

def sort_pass_from_row(start_row):
	# This drone processes all rows, starting from start_row.
	made_swap = False
	
	# Move to the starting row.
	move(South)
	for i in range(start_row):
		move(North)
	
	# Determine the initial direction.
	if start_row % 2 == 0:
		dir = East
	else:
		dir = West
		for i in range(size - 1):
			move(East)
	
	# Process all rows, wrapping around the field.
	for offset in range(size):
		y = (start_row + offset) % size
	
		for x in range(size):
			cur = measure()
			
			# Compare with the cactus to the East or West.
			if dir == East and x < size - 1:
				nei = measure(East)
				if nei != None and cur > nei:
					swap(East)
					made_swap = True

			if dir == West and x > 0:
				nei = measure(West)
				if nei != None and cur < nei:
					swap(West)
					made_swap = True
			
			# Compare with the cactus to the North or South.
			if y < size - 1:
				up = measure(North)
				if up != None and cur > up:
					swap(North)
					made_swap = True

			if y > 0:
				down = measure(South)
				if down != None and cur < down:
					swap(South)
					made_swap = True
			
			if x < size - 1:
				move(dir)
		
		if offset < size - 1:
			move(North)
			dir = reverse(dir)
	
	return made_swap


def sort_cactus():
	sorted = False
	
	while not sorted:
		sorted = True
		drones = []
		spacing = 5
		
		# Drones start at rows 0, 5, 10, 15, 20, 25, 30...
		for i in range(max_drones()):
			start = i * spacing

			if start >= size:
				break
			
			def task():
				return sort_pass_from_row(start)
			
			drone = spawn_drone(task)

			if drone:
				drones.append(drone)
			else:
				if task():
					sorted = False
		
		# Wait for all drones to finish their sorting pass.
		for drone in drones:
			if wait_for(drone):
				sorted = False

# ---------------- 3. HARVESTING ----------------

def harvest_all():
	harvest()  # Harvesting one cactus triggers the propagation.

# ---------------- MAIN LOOP ----------------

while True:
	plant_all()
	sort_cactus()
	harvest_all()