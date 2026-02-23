import Aircraft_Calc


# Pre-defined variable values
fuel_capacity = 1000  # gallons
fuel_consumption_rate = 50  # gallons per hour
true_air_speed = 150  # knots
payload = 5000  # pounds
fuel_weight = 6000  # pounds
moment_list = [10000, 2500]  # pound-feet
weight = 1500  # pounds
cl = 1.5  # lift coefficient
rho = 1.225  # air density in kg/m^3
v = 100  # velocity in m/s
s = 20  # wing area in m^2
cd = 0.02  # drag coefficient
mass = 5000  # mass in kg
g = 9.81  # acceleration due to gravity in m/s^2
thrust = 6000  # thrust in N
drag = 5000  # drag in N
velocity = 50  # initial velocity in m/s
acceleration = 2  # acceleration in m/s^2
time = 10  # time in seconds


distance = Aircraft_Calc.calculate_distance(velocity, time)
print(distance)
acceleration = Aircraft_Calc.calculate_acceleration(thrust, drag, weight, mass)
print(acceleration)