from models.aircraft import Aircraft
import uuid
from exception.domain_exception import DomainException
from managers.base_manager import BaseManager
from typing import Any, List


class AircraftManager(BaseManager):
	__aircraft: List[Aircraft]

	def __init__(self):
		self.__aircraft = []

	def create(self, aircraft: Aircraft) -> Aircraft:
		self.__add(aircraft)
		return aircraft
	
	def update(self, value: Aircraft) -> Aircraft:
		self.__remove(value)
		self.__add(value)
		return value

	def read(self,id: uuid.uuid4) -> Aircraft:
		aircraft = self.__find(id)
		if aircraft is None:
			raise DomainException(f"Aircraft with id {id} not found")
		return aircraft
	
	def delete(self, id: Any) -> Any:
		aircraft = self.__find(id)
		if aircraft is None:
			raise DomainException(f"Aircraft with id {id} not found")
		self.__remove(aircraft)

	def list(self):
		return self.__aircraft
	
	def __add(self, aircraft: Aircraft):
		self.__aircraft.append(aircraft)

	def __find(self, id) -> [None, Aircraft]:
		for i in range(len(self.__aircraft)):
			if  str(self.__aircraft[i].id) == id:
				return self.__aircraft[i]
			return None

	def __remove(self, value: Aircraft):
		self.__aircraft.remove(value) 