# Jordan Tunstill - 012227272 - jtuns18@wgu.edu

from datetime import datetime, timedelta
from hashTable import HashTable
from package import Package
from truck import Truck
from loader import load_package_data, load_distance_data
from deliveryAlgorithm import deliver_packages

    def initialize_trucks(start_time):
        truck1 = Truck(1, 16, 18, start_time)
        truck2 = Truck(2, 16, 18, start_time)
        truck3 = Truck(3, 16, 18, start_time)
        return [truck1, truck2, truck3]


#sets a single start time for all trucks: 8:00 AM
    start_time = datetime(2024, 10, 11, 8, 0)
    trucks = initialize_trucks(start_time)

#returns truck information
    for truck in trucks:
        print(truck)

    def load_trucks(trucks, package_table):
#I will manually load the trucks here

    def deliver_packages(trucks, package_table):
#I am going to need to implement the delivery algo here

    def check_package_status(package_table, package_id, time):
#I am going to need to implement my package check here

#implements a viewer for total mileage of the trucks
    def view_total_mileage(trucks):
        total_mileage = sum(truck.mileage for truck in trucks)
        print(
            f"Total Mileage for all trucks: {total_mileage:.1f} miles")

    def main():
#initialization of hash table
    package_table = HashTable(40)

#loading package and distance data from file
    load_package_data("WGUPS Package File.csv", package_table)
    load_distance_data("WGUPS Distance Table.csv")

#daily start time for the trucks
    start_time = datetime(2024, 10,11,8,0)

#initialize the trucks
    trucks = initialize_trucks(start_time)

#begin the program
    simulation_run = False

    #this is the CLI
    while True:
        print("\nWGUPS Package Delivery System")
        if not simulation_run:
            print("1. Start delivery simulation")
        print("2. Check package status")
        print("3. View total mileage")
        print("4. Exit")
        choice = input("Enter your choice: ")

    #this tells users if the simulation has been run, and is not visible once it has been run, as it can only be run once
        if choice == '1' and not simulation_run:
            deliver_packages(trucks, package_table)
            print("Delivery simulation completed.")
            simulation_run = True

    #this allows users to check the delivery info for a package at a given time, if the simulation has been run
        elif choice == '2':
            if simulation_run:
                package_id = input("Enter package ID: ")
                time = input("Enter time (HH:MM): ")
                check_package_status(package_table, package_id, time)
            else:
                print("Please run the simulation first.")

    #this allows users to check the mileage of the trucks at a given time, if the simulation has been run
        elif choice == '3':
            if simulation_run:
                view_total_mileage(trucks)
            else:
                print("Please run the simulation first.")

    #this ends the program, and includes a break statement for the overall loop for error handling
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

    if __name__ == "__main__":
        main()