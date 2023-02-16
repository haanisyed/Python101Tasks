"""
This program calculates the force needed to accelerate a car (at 0.05 m/s/s) of the given mass 700kg
Date: Sept 2022
"""
#the mass of the car can be entered below (700kg)
car_mass = int(input("Enter the mass: "))
#the acceleration of the car can be entered below (0.05m/s/s)
driver_acceleration = float(input("Enter the Acceleration Rate: "))
#below is the mathematical calculation to get the force needed
force_calculation = (float(car_mass) * float(driver_acceleration))
# last line represents the final statement required
needed_force = input("To Move an object of mass = " + str(car_mass) + "kg" + " at an acceleration rate of " + str(driver_acceleration) + "m/s/s" + " we need a force equal to " + str(force_calculation) + "N")
