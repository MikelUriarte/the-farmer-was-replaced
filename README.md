# The Farmer Was Replaced — Scripts & Algorithms

A collection of scripts and solutions I developed while playing **The Farmer Was Replaced**.

The project started with simple farming automation and gradually evolved into more advanced solutions using **multiple drones, algorithms, and parallel task execution**.

## 📂 Project Structure

### 🌳 Trees

* `plant_trees.py` — Plants trees in a checkerboard pattern and fills the remaining tiles with bushes.
* `trees_at_max.py` — Plants trees across the entire field for maximum tree density.
* `multi_drone_trees.py` — Uses multiple drones to automate tree and bush planting.

### 🌵 Cacti

* `cactus_bubble_sort.py` — Sorts cacti using a 2D Bubble Sort approach.
* `cactus_bubble_sort_multidrone.py` — Uses multiple drones to perform the cactus sorting process in parallel.

### 🎃 Pumpkins

* `pumpkin_multidrone.py` — Divides the field between multiple drones to plant and replant pumpkins.

### 🥕 Carrots

* `plant_carrots.py` — Continuously plants and harvests carrots.
* `carrots_multidrone.py` — Uses multiple drones to continuously harvest and replant carrots.

### 🌾 Hay

* `harvest_hay.py` — Continuously harvests hay and uses water when available.
* `hay_multidrone.py` — Uses multiple drones to harvest hay across the field.

### 🧩 Maze

* `maze_solver.py` — Creates and solves mazes using the **Right-Hand Rule** algorithm.

### 🦖 Dinosaur

* `dinosaur_10x10.py` — Controls the dinosaur through a 10×10 world using a predefined movement pattern.

### 🛠️ Utilities

* `convert_soil.py` — Converts the field to tilled soil.
* `return_to_start.py` — Returns the drone to the starting position `(0, 0)`.

## 🧠 Algorithms & Concepts

Some of the concepts explored in these scripts include:

* **Bubble Sort**
* **2D grid traversal**
* **Right-Hand Rule maze solving**
* **Parallel task execution**
* **Multi-drone automation**
* **Field partitioning**
* **Coordinate-based patterns**
* **Resource management**

## 🚁 Multi-Drone Automation

Several scripts use multiple drones to divide the field into smaller tasks.

Instead of having a single drone process the entire field sequentially, the work is distributed between several drones that operate concurrently.

This was particularly useful for:

* Tree farming
* Cactus sorting
* Pumpkin farming
* Carrot farming
* Hay farming

## 🎯 About

These scripts were created as part of my playthrough of **The Farmer Was Replaced**, experimenting with different ways to automate the farm and improve efficiency.

The repository contains both simple solutions and more advanced implementations developed as I progressed through the game.
