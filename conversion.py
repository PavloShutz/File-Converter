import os
from constants import AVAILABLE_FORMATS, SECRET
import convertapi
from dataclasses import dataclass


@dataclass
class FileConversion:
	"""Class for file conversion."""
	file: str

	def _extract_file_extension(self):
		"""Returns file extension"""
		return os.path.splitext(self.file)[1][1:]


	def convert_file(self):
		"""Conversion of input file"""
		extension = self._extract_file_extension()
		if extension not in AVAILABLE_FORMATS.keys():
			return "Sorry, couldn't find extension for this file."
		return AVAILABLE_FORMATS[extension]
