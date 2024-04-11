from abc import ABCMeta, abstractmethod
from typing import Any

class BaseManager(metaclass = ABCMeta):

	@abstractmethod
	def create(self, value: Any) -> Any:
		raise NotImplementedError
	
	@abstractmethod
	def read(self, value: Any) -> Any:
		raise NotImplementedError
	
	@abstractmethod
	def update(self, value: Any) -> Any:
		raise NotImplementedError
	
	@abstractmethod
	def delete(self, value: Any) -> Any:
		raise NotImplementedError
	
	@abstractmethod
	def list(self):
		raise NotImplementedError