""" temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event it cancelled")
else:
    print("THe outdoor event is still scheduled")


 """

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("it is HOT outside ")
    print("it is SUNNY ")
elif temp <= 0 and is_sunny:
    print("It is COLD outside ")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside ")
    print("it is SUNNY ")
elif temp >= 28 and not is_sunny:
    print("it is HOT outside ")
    print("it is Cloudy ")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside ")
    print("It is Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside ")
    print("it is Cloudy ")

