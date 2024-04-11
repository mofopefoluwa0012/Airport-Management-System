import uuid
from exception.domain_exception import DomainException
from models.booking import Booking
from typing import Any, List
from managers.base_manager  import BaseManager

class BookingManager(BaseManager):
	__booking: List[Booking]

	def __init__(self):
		self.__booking = []
	
	def create(self, booking: Booking) -> Booking:
		self.__add(booking)
		return booking
	
	def update(self, value: Booking) -> Booking:
		self.remove(value)
		self.__add(value)
	
	def read(self, id: uuid.uuid4) -> Booking:
		booking = self.__find(id)
		if booking is None:
			raise DomainException(f"Booking with the id {id} not found")
		return booking
	
	def delete(self, id) -> [None, Booking]:
		booking = self.__find(id)
		if booking is None:
			raise DomainException(f"Booking with the id {id} not found")
		self.__remove(booking)

	def list(self):
		return self.__booking
	
	def __add(self, booking: Booking):
		self.__booking.append(booking)

	def __find(self, id) -> [None, Booking]:
		for i in range(len(self.__booking)):
			if str(self.__booking[i].id) == id:
				return self.__booking[i]
			return None
		
	def __remove(self, value: Booking):
		self.__booking.remove(value)