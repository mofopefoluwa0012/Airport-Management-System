import datetime
import uuid

from models.aircraft import Aircraft
from models.flight import Flight
from models.passenger import Passenger

class Booking:
	def __init__(self, flight:Flight, passenger:Passenger,aircraft:Aircraft, is_paid: bool):
		self.__id = str(uuid.uuid4()).split('-')[1]
		self.__flight = flight
		self.__passenger = passenger
		self.__aircraft = aircraft
		self.__is_paid = is_paid
		self.__refrence_code = str(uuid.uuid4()).split('-')[1].upper()

	@property
	def id(self) -> str:
		return self.__id

	@property
	def flight(self) -> Flight:
		return self.__flight
	
	@flight.setter
	def flight(self, value:Flight):
		self.__flight = value

	@property
	def passenger(self) -> Passenger:
		return self.__passenger		
	
	@passenger.setter
	def passenger(self,value:Passenger):
		self.__passenger = value

	@property
	def is_paid(self) -> bool:
		return self.__is_paid 
	
	@is_paid.setter
	def is_paid(self,value:True) -> bool:
		self.__is_paid = value

	@property
	def refrence_code(self) -> str:
		return self.__refrence_code

	def __str__(self) -> str:
		return f"ID: {self.__id}\nTake Off Time: {self.__flight.take_off_time}\nPassenger email: {self.__passenger.email}\nAircraft availabilty: {self.__aircraft.is_available}\nTransaction Condition: {self.__is_paid}\nRefrence code: {self.__refrence_code}"
		