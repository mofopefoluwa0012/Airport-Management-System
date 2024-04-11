import uuid

class Aircraft:
	def __init__(self,name:str,regristation_number:str,capacity:int):
		self.__id = str(uuid.uuid4()).split("-")[1]
		self.__name = name
		self.__code = str(uuid.uuid4()).split('-')[-1].upper()
		self.__regristation_number = regristation_number
		self.__capacity = capacity
		self.__is_available = True

	@property
	def id(self) -> uuid:
		return self.__id
	
	@property
	def name(self) -> str:
		return self.__name
	
	@name.setter
	def name(self, value:str) -> str:
		self.__name = value

	@property
	def code(self) -> str:
		return self.__code
	
	@property
	def regristation_number(self) -> str:
		return self.__regristation_number
	
	@property
	def capacity(self) -> int:
		return self.__capacity
	
	@property
	def is_available(self) -> None:
		return self.__is_available
	
	@is_available.setter
	def is_available(self,value:bool) -> bool:
		self.__is_available = value

	def __str__(self) -> str:
		return f"ID: {self.__id}\nAircraft name: {self.__name}\nAircraft code: {self.__code}\nRegristration number: {self.__regristation_number}\nCapacity: {self.__capacity}\nAvailability: {self.__is_available}"
