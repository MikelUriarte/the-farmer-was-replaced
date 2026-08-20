clear()
size = get_world_size()

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
	dir = East
	for y in range(size):
		for x in range(size):
			plant_cactus()
			if x < size - 1:
				move(dir)
		if y < size - 1:
			move(North)
			dir = reverse(dir)

# ---------------- 2. SORTING ----------------
# Sorts the cacti by size using a 2D Bubble Sort approach.
# The algorithm compares neighboring cacti and swaps them
# until the entire field is sorted.

def sort_cactus():
	sorted = False

	while not sorted:
		sorted = True
		dir = East

		for y in range(size):
			for x in range(size):
				cur = measure()

				# Compare with the cactus to the East or West
				if dir == East and x < size - 1:
					nei = measure(East)
					if nei != None and cur > nei:
						swap(East)
						sorted = False

				if dir == West and x > 0:
					nei = measure(West)
					if nei != None and cur < nei:
						swap(West)
						sorted = False

				# Compare with the cactus to the North or South
				if y < size - 1:
					up = measure(North)
					if up != None and cur > up:
						swap(North)
						sorted = False

				if y > 0:
					down = measure(South)
					if down != None and cur < down:
						swap(South)
						sorted = False

				if x < size - 1:
					move(dir)

			if y < size - 1:
				move(North)
				dir = reverse(dir)

# ---------------- 3. HARVESTING ----------------

def harvest_all():
	harvest()  # Harvesting one cactus triggers the propagation

# ---------------- MAIN LOOP ----------------

while True:
	plant_all()
	sort_cactus()
	harvest_all()