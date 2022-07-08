from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import base

from constants import GREETING_MESSAGE, TOKEN


class FileConverter(Bot):
	def __init__(self, token: base.String):
		super().__init__(token)
		self.dp = Dispatcher(self)

		@self.dp.message_handler(commands=['start', 'help'])
		async def greet_user(message: types.Message):
			await self.send_message(message.from_user.id, GREETING_MESSAGE)


if __name__ == '__main__':
	file_converter = FileConverter(token=TOKEN)
	executor.start_polling(file_converter.dp, skip_updates=True)
