import uuid
class Passenger:
	def __init__(self,first_name: str,last_name: str,email: str,phone_number: int,age:int):
		self.__id = str(uuid.uuid4())[1]
		self.__first_name = first_name
		self.__last_name = last_name
		self.__email = email
		self.__phone_number = phone_number
		self.__age = age

	@property
	def id(self) -> str:
		return self.__id
	
	@property
	def first_name(self) -> str:
		return self.__first_name
	
	@first_name.setter
	def first_name(self,value: str):
		self.__first_name = value

	@property
	def last_name(self) -> str:
		return self.__last_name
	
	@last_name.setter
	def last_name(self,value:str):
		self.__last_name = value

	@property
	def email(self) -> str:
		return self.__email
	
	@last_name.setter
	def email(self,value:str):
		self.__email = value

	@property
	def phone_number(self) -> int:
		return self.__phone_number
	
	@last_name.setter
	def phone_number(self,value:int):
		self.__phone_number = value

	@property
	def age(self) -> int:
		return self.__age
	
	@last_name.setter
	def age(self,value:int):
		self.__age = value

	def __str__(self) -> str:
		return f"ID: {self.__id}\nFirst name: {self.__first_name}\nLast name: {self.__last_name}\nEmail: {self.__email}\nPhone number: {self.__phone_number}\nAge: {self.__age}"