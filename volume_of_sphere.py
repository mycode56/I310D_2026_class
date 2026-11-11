def calculate_volume_of_sphere(radius):
	pi = 3.14
	volumn = 4/3*pi * radius * radius * radius
	return volumn

radius1 = 30
volumn1 = calculate_volume_of_sphere(radius1)
print(f"The volumn of sphere with radius {radius1} is: {volumn1}")

radius2 = 40
volumn2 = calculate_volume_of_sphere(radius2)
print(f"The volumn of sphere with radius {radius2} is: {volumn2}")
