import uuid
from managers.base_manager import BaseManager
from typing import Any, List
from models.flight import Flight
from exception.domain_exception import DomainException

class FlightManager(BaseManager):
	__flight = List[Flight]

	def __init__(self):
		self.__flight = []

	def create(self, flight: Flight) -> Flight:
		self.__add(flight)
		return flight
	
	def update(self, value: Flight) -> Flight:
		self.__remove(value)
		self.__add(value)

	def read(self, id: uuid.uuid4) -> Flight:
		flight = self.__find(id)
		if flight is None:
			raise DomainException(f"Flight with the id {id} not found")
		return flight
	
	def delete(self, id: Any) -> Any:
		flight = self.__find(id)
		if flight is None:
			raise DomainException(f"Flight with the id {id} not found")
		self.__remove(flight)

	def list(self):
		return self.__flight
	
	def __add(self, flight: Flight):
		self.__flight.append(flight)

	def __find(self, id) -> [None, Flight]:
		for i in range(len(self.__flight)):
			if str(self.__flight[i].id) == id:
				return self.__flight[i]
			return None
	
	def __remove(self, value: Flight):
		self.__flight.remove(value)