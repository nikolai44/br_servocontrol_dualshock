import requests
import logging
from os import path


class _Api:
	BASE_URL = 'http://37.110.86.243:3141/'

	def led(self, value):
		"""send True if led on and False otherwise"""
		return requests.post(path.join(self.BASE_URL, 'led/'), json={'led': value == 'on'})

	def serial(self, data):
		return requests.post(path.join(self.BASE_URL, 'serial/'), json={'command': data})


class ServocontrolApi:
	def __init__(self):
		self.api = _Api()
		self.api.led(True)
		print('led on')

	def __del__(self):
		self.api.led(False)
		print('led off')

	def set_led(self, value):
		self.api.led(value)

	def set_speed(self, value):
		r = self.api.serial(f'speed:{value}')
		print(r.status_code)
		print(r.content)
		print(f'set speed to {value}')

	def set_smooth_speed(self, value):
		self.api.serial(f'smooth_speed:{value}')
		print(f'set smooth speed to {value}')

	def set_transfer_time(self, value):
		"""время переходного процесса в секундах"""
		value *= 10		# перевод в десятые секунды
		self.api.serial(f'transfer_time:{value}')
		print(f'set transfer_time to {value}')
