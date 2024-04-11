import uuid
from exception.domain_exception import DomainException
from managers.base_manager import BaseManager
from typing import Any, List
from models.passenger import Passenger

class PassengerManager(BaseManager):
	__passenger = List[Passenger]

	def __init__(self):
		self.__passenger = []

	def create(self, passenger: Passenger) -> Passenger:
		self.__add(passenger)
		return passenger
	
	def update(self, value: Passenger) -> Passenger:
		self.__remove(value)
		self.__add(value)
		return value
	
	def read(self, id: uuid.uuid4) -> Passenger:
		passenger = self.__find(id)
		if passenger is None:
			raise DomainException(f"Passenger with the id {id} not found")
		return passenger
	
	def delete(self, id: Any) -> Any:
		passenger = self.__find(id)
		if passenger is None:
			raise DomainException(f"Passenger with the id {id} not found")
		self.__remove(passenger)

	def list(self):
		return self.__passenger
	
	def __add(self, passenger: Passenger):
		self.__passenger.append(passenger)

	def __find(self, id) -> [None, Passenger]:
		for i in range(len(self.__passenger)):
			if str(self.__passenger[i].id) == id:
				return self.__passenger[i]
			return None
		
	def __remove(self, value: Passenger):
		self.__passenger.remove(value)