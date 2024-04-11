import datetime
import uuid

from models.aircraft import Aircraft

class Flight:
	def __init__(self,take_off_time:datetime,destination:str,duration:int,price:float,arrival_time:datetime, aircraft: Aircraft) :
		self.__id = str(uuid.uuid4()).split('-')[1].upper()
		self.__take_off_time = take_off_time
		self.__code = str(uuid.uuid4()).split('-')[1].upper()
		self.__destination = destination
		self.__duration = duration
		self.__price = price
		self.__arrival_time = arrival_time
		self.__aircraft = aircraft

	
	@property
	def id(self) -> str:
		return self.__id
	
	@property
	def take_off_time(self) -> datetime:
		return self.__arrival_time
	
	@take_off_time.setter
	def take_off_time(self, value:datetime):
		self.__take_off_time = value

	@property
	def code(self) -> str:
		return self.__code

	@property
	def destination(self) -> str:
		return self.__destination
	
	@destination.setter
	def destination(self,value:str):
		self.__destination = value

	@property
	def duration(self) -> int:
		return self.__duration
	
	@duration.setter
	def duration(self,value:int):
		self.__duration = value

	@property
	def price(self) -> float:
		return self.price 
	
	@price.setter
	def price(self,value:float):
		self.__price = value

	@property
	def arrival_time(self) -> datetime:
		return self.__arrival_time
	
	@arrival_time.setter
	def arrival_time(self,value:datetime):
		self.__arrival_time

	@property
	def aircraft(self) -> Aircraft:
		return self.__aircraft
	
	@aircraft.setter
	def aircraft(self,value:Aircraft):
		self.aircraft = value

	def __str__(self) -> str:
		return f"ID: {self.__id}\nTake off time: {self.__take_off_time}\nCode: {self.__code}\nDestination: {self.__destination}\nDuration: {self.__duration}\nPrice: {self.__price}\nArrival time: {self.__arrival_time}\nAircraft name: {self.__aircraft.name}\nAircraft Capacity: {self.__aircraft.capacity}"
	
