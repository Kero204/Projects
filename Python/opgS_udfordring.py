astronaut_name = "Kerim"
astronaut_age = 27
fuel = 46.5

is_engine_running = False
is_engine_running = True

if is_engine_running:
    print("Engine is running!")
else:
    print("Engine is idle.")

astronauts = ["Ali", "Hicham", "Sebastian"]
astronaut_ages = {
    "Ali": 34,
    "Hicham": 29,
    "Sebastian": 42
}


travel_time = 10
speed = 5000
fuel_efficiency = 10

distance = speed * travel_time 
fuel_consumption = distance / fuel_efficiency
time_to_destination = distance / speed


first_name = "Kerim"
last_name = "Ribic"
full_name = first_name + " " + last_name

print(f"Astronaut is: {astronaut_name}")
print(f"The astronaut is: {astronaut_age} years old")
print(f"Fuel is: {fuel}")
print(f"The other other astronauts are: {astronaut_ages}")
print(f"what is the total distance traveled: {distance}")
print(f"What is the total fuel consumed: {fuel_consumption}")
print(f"How long to reach the destination: {time_to_destination}")
print(full_name)


