clear()
size = get_world_size()

# Pumpkin farming using multiple drones.
#
# The field is divided into columns between multiple drones.
# Drones work in parallel to plant pumpkins and replant pumpkins
# that have failed to grow. Multiple replanting passes are performed
# before harvesting the entire field.

# ---------------- 1. INITIAL PLANTING ----------------

def plant_columns(start_x, end_x):
	# Move to the starting position (start_x, 0).
	move(South)
	for i in range(start_x):
		move(East)
	
	# Plant every column assigned to this drone.
	for x in range(start_x, end_x):
		# Plant the entire column.
		for y in range(size):
			if can_harvest():
				harvest()

			if get_ground_type() == Grounds.Grassland:
				till()

			plant(Entities.Pumpkin)

			if y < size - 1:
				move(North)
		
		# Move to the next column.
		if x < end_x - 1:
			move(East)


def Plantar1():
	drones = []
	num_workers = max_drones()
	cols_per_drone = size // num_workers
	
	# Divide the field into column ranges for each drone.
	for i in range(num_workers):
		start = i * cols_per_drone

		if i == num_workers - 1:
			end = size
		else:
			end = start + cols_per_drone
		
		def task():
			plant_columns(start, end)
		
		drone = spawn_drone(task)

		if drone:
			drones.append(drone)
		else:
			task()
	
	# Wait for all drones to finish planting.
	for drone in drones:
		wait_for(drone)


# ---------------- 2. REPLANTING FAILED PUMPKINS ----------------

def replant_columns(start_x, end_x):
	move(South)

	for i in range(start_x):
		move(East)
	
	for x in range(start_x, end_x):
		for y in range(size):
			# Replant pumpkins that failed to grow.
			if can_harvest() == False:
				plant(Entities.Pumpkin)

			if y < size - 1:
				move(North)
		
		if x < end_x - 1:
			move(East)


def plantar2():
	num_workers = max_drones()
	cols_per_drone = size // num_workers
	
	# Perform five replanting passes.
	for pasada in range(5):
		drones = []
		
		for i in range(num_workers):
			start = i * cols_per_drone

			if i == num_workers - 1:
				end = size
			else:
				end = start + cols_per_drone
			
			def task():
				replant_columns(start, end)
			
			drone = spawn_drone(task)

			if drone:
				drones.append(drone)
			else:
				task()
		
		# Wait for all drones to finish the current pass.
		for drone in drones:
			wait_for(drone)


# ---------------- 3. HARVESTING ----------------

def harvest_all():
	move(South)  # Return to the origin.
	harvest()  # One harvest propagates through the entire field.


# ---------------- MAIN LOOP ----------------

while True:
	Plantar1()
	plantar2()
	harvest_all()