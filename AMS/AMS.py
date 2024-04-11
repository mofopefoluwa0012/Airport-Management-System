import uuid
import datetime

from models.aircraft import Aircraft
from models.passenger import Passenger
from models.flight import Flight
from models.booking import Booking
from managers.aircraftmanager import AircraftManager
from managers.passengermanager import PassengerManager
from managers.flightmanager import FlightManager
from managers.bookingmanager import BookingManager

aircraft_manager = AircraftManager()
passenger_manager = PassengerManager()
flight_manager = FlightManager()
booking_manager = BookingManager()

def print_welcome():
	print("WELCOME TO OUR AMS APPLICATION")
	print('\n')

def print_main_menu():
	print("---------------Main Menu----------------")
	print("\n")
	print("Manage Aircraft: 1")
	print("Manage passenger: 2")
	print("Manage Flight: 3")
	print("Manage booking: 4")
	print("End: 0")

def handle_main_menu(option: int):
	match option:
		case 0:
			print("Thank you for using our application")
			exit()
		case 1:
			print_aircraft_menu()
			handle_aircraft_menu(try_option("Enter your choice: "))

		case 2:
			print_passenger_menu()
			handle_passenger_menu(try_option("Enter your option: "))

		case 3:
			print_flight_menu()
			handle_flight_menu(try_option("Enter your option: "))

		case 4:
			print_booking_menu()
			handle_booking_menu(try_option("Enter your option: "))

		case _:
			print("Invalid option, try again:")
			print_main_menu()
			handle_main_menu(try_option("Enter your option: "))

def try_option(prompt):
	is_valid = False
	while not is_valid:
		try:
			option = int(input(prompt))
			return option
		except Exception:
			is_valid = False

def print_aircraft_menu():
	print("---------------Aircraft Menu---------------")
	print("\n")
	print("Create aircraft: 1")
	print("Update aircraft: 2")
	print("List aircraft: 3")
	print("Delete aircraft: 4")
	print("Get aircraft: 5")
	print("Back: 0")

def handle_aircraft_menu(option: int):
	match option:
		case 0:
			print_main_menu()
			handle_main_menu(try_option("Enter your option: "))

		case 1:
			name: str  = input("Enter aircraft name: ")
			regristration_number: str = input("Enter regristration number: ")
			capacity: int = int(input("Enter capacity of the aircraft: "))
			aircraft = Aircraft(name, regristration_number, capacity)
			aircraft_manager.create(aircraft)
			print(f"Aircraft created successfully------------{print_date_time()}")
			print_aircraft_menu()
			handle_aircraft_menu(try_option("Enter your option: "))

		case 2:
			id = input("Enter aircraft id: ")
			aircraft = aircraft_manager.read(id)
			if aircraft is None:
				print("Aircraft not found")
				return
			name: str = input("Enter aircraft name: ")
			aircraft.name = name
			aircraft_manager.update(aircraft)
			print(f"Aircraft was updated----------{print_date_time()}")
			print_aircraft_menu()
			handle_aircraft_menu(try_option("Enter your option: "))
		
		case 3:
			aircraft = aircraft_manager.list()
			for i in range(len(aircraft)):
				print(str(aircraft[i]))
			print_aircraft_menu()
			handle_aircraft_menu(try_option("Enter your option: "))

		case 4:
			id = input("Enter aircraft id: ")
			aircraft = aircraft_manager.read(id)
			if aircraft is None:
				print("Aircraft not found")
				return
			aircraft_manager.delete(id)
			print(f"Aircraft was deleted successfully---------------{print_date_time()}")
			print_aircraft_menu()
			handle_aircraft_menu(try_option("Enter your option: "))

		case 5:
			id = input("Enter aircraft id: ")
			aircraft = aircraft_manager.read(id)
			if aircraft is None:
				print("Aircraft not found")
				print_aircraft_menu()
				handle_aircraft_menu(try_option("Enter your option: "))
			print(str(aircraft))
			print_aircraft_menu()
			handle_aircraft_menu(try_option("Enter your option: "))

		case _:
			print("Invalid choice, try again")
			print_aircraft_menu()
			handle_aircraft_menu(try_option("Enter your option: "))

def print_passenger_menu():
	print("---------------Passenger Menu---------------")
	print("Create passenger: 1")
	print("Update passenger: 2")
	print("List passenger: 3")
	print("Delete passenger: 4")
	print("Get passenger: 5")
	print("Back: 0")


def handle_passenger_menu(option):
	match option:
		case 0:
			print_main_menu()
			handle_main_menu(try_option("Enter your option: "))

		case 1:
			first_name: str = input("Enter passenger first name: ")
			last_name: str = input("Enter passenger last name: ")
			email: str = input("Enter passenger email: ")
			phone_number: int = int(input("Enter passenger phone number: "))
			age: int = int(input("Enter passenger age: "))
			passenger = Passenger(first_name, last_name, email, phone_number, age)
			passenger_manager.create(passenger)
			print(f"Passenger created successfully---------------{print_date_time()}")
			print_passenger_menu()
			handle_passenger_menu(try_option("Enter your option: "))

		case 2:
			id: str = input("Enter passenger id: ")
			passenger = passenger_manager.read(id)
			if passenger is None:
				print("Passenger not found")
				print_passenger_menu()
				handle_passenger_menu(try_option("Enter your option: "))
			first_name: str = input("Enter passenger first name: ")
			last_name: str = input("Enter passenger last name: ")
			email: str = input("Enter passenger email: ")
			phone_number: int = int(input("Enter passenger phone number: "))
			age: int = int(input("Enter passenger age: "))
			passenger.first_name = first_name
			passenger.last_name = last_name
			passenger.email = email
			passenger.phone_number = phone_number
			passenger.age = age
			passenger_manager.update(passenger)
			print("Passenger has been updated successfully---------------{print_date_time()}")
			print_passenger_menu()
			handle_passenger_menu(try_option("Enter your option: "))

		case 3:
			passenger = passenger_manager.list()
			for i in range(len(passenger)):
				if passenger is None:
					print("Passenger not found")
					print_passenger_menu()
					handle_passenger_menu(try_option("Enter your option: "))
				print(str(passenger[i]))
				print_passenger_menu()
				handle_passenger_menu(try_option("Enter your option: "))

		case 4:
			id: str = input("Enter passenger id: ")
			passenger = passenger_manager.read(id)
			if passenger is None:
				print("Passenger not found")
				print_passenger_menu()
				handle_passenger_menu(try_option("Enetr your option: "))
			passenger_manager.delete(id)
			print("Passenger has been deleted successfully")
			print_passenger_menu()
			handle_passenger_menu(try_option("Enetr your option: "))

		case 5:
			id: str = input("Enter passenger id: ")
			passenger = passenger_manager.read(id)
			if passenger is None:
				print("Passenger not found")
				print_passenger_menu()
				handle_passenger_menu(try_option("Enter your option: "))
			print(str(passenger))
			print_passenger_menu()
			handle_passenger_menu(try_option("Enetr your option: "))


		case _:
			print("Invalid option, try again")
			print_passenger_menu()
			handle_passenger_menu()



def print_flight_menu():
	print("---------------Flight Menu---------------")
	print("Create flight: 1")
	print("Update flight: 2")
	print("List flight: 3")
	print("Delete flight: 4")
	print("Get flight: 5")
	print("Back: 0")

def __handle_date_input(prompt: str) -> datetime.datetime:
	print(prompt)
	year = int(input('Enter a year: '))
	month = int(input('Enter a month: '))
	day = int(input('Enter a day: '))
	return datetime.datetime(year, month, day)



def __get_aircraft(id: str):
	return aircraft_manager.read(id)

def __get_flight(id: str):
	return flight_manager.read(id)

def __get_passenger(id: str):
	return passenger_manager.read(id)

def handle_flight_menu(option: int):
	match option:
		case 0:
			print_main_menu()
			handle_main_menu(try_option("Enter your option: "))

		case 1:
			take_off_time: int = __handle_date_input("Enter flight take off time: ")
			destination: str = input("Enter flight destination: ")
			duration: int = int(input("Enter flight duration in hours: "))
			arrival_time = take_off_time + datetime.timedelta(hours=duration)
			price = float(input("Enter the price of flight: "))
			aircraft = __get_aircraft(input("Enter aircraft id: "))
			if aircraft is None:
				print(f"Airacraft not found")
			flight = Flight(take_off_time, destination, duration, price, arrival_time, aircraft)
			flight_manager.create(flight)
			print(f"Flight created successfully---------------{print_date_time()}")
			print_flight_menu()
			handle_flight_menu(try_option("Enter your option: "))
			
		case 2:
			id: str = input("Enter flight id: ")
			flight = flight_manager.read(id)
			if flight is None:
				print("Flight not found")
			price: float("Enter the price of flight to update: ")
			flight.price = price
			flight_manager.update(flight)
			print(f"Flight updated successfully---------------{print_date_time()}")
			print_flight_menu()
			handle_flight_menu(try_option("Enter your option: "))

		case 3:
			flight = flight_manager.list()
			for i in range(len(flight)):
				print(str(flight[i]))
				print_flight_menu()
				handle_flight_menu(try_option("Enter your option: "))

		case 4:
			id: str = input("Enter flight id: ")
			flight = flight_manager.read(id)
			if flight is None:
				print("Flight not found")
			flight_manager.delete(flight)
			print(f"Flight has been deleted successfully---------------{print_date_time()}")
			print_flight_menu()
			handle_flight_menu(try_option("Enter your option: "))

		case 5:
			id: str = input("Enter flight id: ")
			flight = flight_manager.read(id)
			if flight is None:
				print("Flight not found")
			print(str(flight))

		case _:
			print("Invalid option, try again")
			print_flight_menu()
			handle_flight_menu(try_option("Enter your option: "))

def print_booking_menu():
	print("---------------Booking Menu---------------")
	print("1 to create booking")
	print("2 to update booking")
	print("3 to list booking")
	print("4 to delete booking")
	print("5 to get booking")
	print("Back: 0")

def handle_booking_menu(option):
	match option:
		case 0:
			print_main_menu()
			handle_main_menu(try_option("Enter your option: "))

		case 1:
			flight: Flight = __get_flight(input("Enter flight id: "))
			passenger: Passenger = __get_passenger(input("Enter passenger id: "))
			aircraft: Aircraft = __get_aircraft(input("Enter aircraft id: "))
			booking = Booking(flight, passenger, aircraft, is_paid= True)
			booking_manager.create(booking)
			print(f"Booking created successfully---------------{print_date_time()}")
			print_booking_menu()
			handle_booking_menu(try_option("Enter your option: "))

		case 2:
			id: str = input("Enter existing booking id to update: ")
			booking = booking_manager.read(id)
			if booking is None:
				print("Booking not found")
				return
			is_paid: bool = False
			booking.is_paid = is_paid
			booking_manager.update(booking)
			print(f"Booking was updated successfully---------------{print_date_time()}")
			print_booking_menu()
			handle_booking_menu(try_option("Enter your option: "))
			

		case 3:
			booking = booking_manager.list()
			for i in range(len(booking)):
				if booking is None:
					print("No booking was found")
				print(str(booking[i]))
			print_booking_menu()
			handle_booking_menu(try_option("Enter your option: "))

		case 4:
			id: str = input("Enter existing booking id to update: ")
			booking = booking_manager.read(id)
			if booking is None:
				print("Booking not found")
				return
			booking_manager.delete(id)
			print(f"Booking with id {id} deleted successfully---------------{print_date_time()}")
			print_booking_menu()
			handle_booking_menu(try_option("Enter your option: "))

		case 5:
			id: str = input("Enter existing booking id to update: ")
			booking = booking_manager.read(id)
			if booking is None:
				print("Booking not found")
				return
			print(str(booking))
			print_booking_menu()
			handle_booking_menu(try_option("Enter your option: "))

		case _:
			print("Invalid option, try again")
			print_booking_menu()
			handle_booking_menu(try_option("Enter your option: "))

def print_date_time():
	return datetime.datetime.now()

def main():
	print_welcome()
	print_main_menu()
	handle_main_menu(try_option("Enter your option: "))

if __name__ == '__main__':
	main()