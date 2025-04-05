#By: Sabria Fafach
#Date: April 4, 2025
#Title: car_test.py

import Car

def main():
    ymod=input("Enter the year model of the car:")
    make=input("Enter the make of the car:")
    car=Car.car(ymod,make)

    for count in range(1,6):
        car.accelerate()
        print(f"After accelerating {count} times, the speed is {car.get_speed()}mph.")

    for count in range(1,6):
        car.brake()
        print(f"After braking {count} times, the speed is {car.get_speed()}mph.")

if __name__ == '__main__':
    main()
