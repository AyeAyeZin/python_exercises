cars=100
cars_in_space=5
drivers=20
pasengers=70
car_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_percar=passengers/cars_driven
print("There are", cars,"cars availble")
print("There are only",drivers,"drivers availble")
print("There will be",car_not_driven,"empty cars today")
print("There are",cars_in_space,"space availble in car")
print("We can transport",carpool_capacity,"peopletoday.")
print("We have", passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
