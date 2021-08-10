#	Switch-Case class for Python
#    Copyright (C) 2021 UltraStudioLTD
#	This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations
from typing import Optional, Any

__all__ = ["Switch"]

class Switch(object):
	"""Switch-Case class for Python"""
	
	def __init__(self, cases: dict = {}, default: Optional[Any] = None):
		"""
		Initializes Switch class with empty cases if no argument is inputed
	
		Parameters
		----------
		cases : dict, default: {}
			Cases dictionary
		default : Optional[Any], default: None
			Default key
		"""
		if isinstance(cases, dict) is False:
			raise TypeError("Cases should be dict (dictionary)")
		self.cases, self.default = cases, default
	
	def case(self, key, value):
		"""
		Add case in cases list
		[It overrides existing Case with same key]
		
		Parameters
		----------
		key
			Case
		value
			Value of Case (key)
		"""
		self.cases[key] = value
	
	def changeDefault(self, key):
		"""
		Changes default key
		
		Parameters
		----------
		key
			new default key
		"""
	self.default = key

	def switch(self, key) -> Any:
		"""
		Switcher

		Parameters
		----------
		key
			key to switch

		Returns
		-------
			value corresponding to key if it exists else default
		"""
		return self.cases[key] if key in self.cases else (self.cases[self.default] if self.default in self.cases else None)
