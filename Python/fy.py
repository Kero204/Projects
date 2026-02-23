# 1. & 2. Personal Info (using strings and ints)
astronaut_name = "Sally" 
astronaut_age = 35

# 3. Fuel restricted to 30.0 - 53.0 (Float)
fuel = 36.5

# 4. Engine status (Boolean)
is_engine_running = True

# 5. List of astronaut names (Strings)
astronauts = ["Ali", "Hicham", "Sebastian"]

# 6. Dictionary of names (Keys) and ages (Values)
astronaut_ages = {
    "Ali": 34,
    "Hicham": 29,
    "Sebastian": 42
}

# --- Calculations using provided image data ---
travel_time = 10         # hours
speed = 5000             # km/h
fuel_efficiency = 10     # km/L
first_name = "Sally"
last_name = "Ride"

# 7. Total distance traveled: Distance = Speed * Time
total_distance = speed * travel_time

# 8. Total fuel consumed: Consumption = Distance / Efficiency
total_fuel_consumed = total_distance / fuel_efficiency

# 9. Total time to destination: Time = Distance / Speed
# (Using the calculated total_distance)
time_to_destination = total_distance / speed

# 10. Full Name variable
full_name = first_name + " " + last_name

# --- Print Outputs ---
print(f"Astronaut Name: {astronaut_name}")
print(f"Astronaut Age: {astronaut_age}")
print(f"Fuel Level: {fuel}")
print(f"Engine Running: {is_engine_running}")
print(f"Astronaut List: {astronauts}")
print(f"Astronaut Ages Dict: {astronaut_ages}")
print(f"Total Distance Traveled: {total_distance} km")
print(f"Total Fuel Consumed: {total_fuel_consumed} Liters")
print(f"Total Time to Destination: {time_to_destination} hours")
print(f"Full Name: {full_name}")