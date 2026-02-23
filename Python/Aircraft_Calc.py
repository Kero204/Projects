

def calculate_lift(cl, rho, v, s):
    return 0.5 * cl * rho * v**2 * s

def calculate_drag(cd, rho, v, s):
    return 0.5 * cd * rho * v**2 * s

def calculate_weight(mass, g):
    return mass * g

def calculate_acceleration(thrust, drag, weight, mass):
    return (thrust - drag - weight) / mass

def calculate_velocity(velocity, acceleration, time):
    return velocity + acceleration * time

def calculate_distance(velocity, time):
    return velocity * time

def calculate_moment(weight, arm):
    return weight * arm

def calculate_cg_position(moment_list, total_weight):
    total_moment = sum(moment_list)
    return total_moment / total_weight





def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    range_in_hours = fuel_capacity / fuel_consumption_rate
    range_in_miles = range_in_hours * true_air_speed
    return range_in_miles

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hours = fuel_capacity / fuel_consumption_rate
    return endurance_in_hours



# Helper function to pretty print performance data
def pretty_print(range_, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance):
    print("Performance Calculations:")
    print(f"Range: {calculate_range} miles".format(range_))
    print(f"Endurance: {endurance} hours".format(endurance))
    print(f"Total Weight: {total_weight} pounds".format(total_weight))
    print(f"Center of Gravity Position: {cg_position} feet".format(cg_position))
    print(f"Lift: {calculate_lift} Newtons".format(lift))
    print(f"Drag: {calculate_drag} Newtons".format(drag))
    print(f"Weight: {weight} Newtons".format(weight))
    print(f"Acceleration: {calculate_acceleration} m/s^2".format(acceleration))
    print(f"Velocity: {velocity} m/s".format(velocity))
    print(f"Distance: {distance} meters".format(distance))