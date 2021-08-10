# Switch
Switch-Case for Python (before 3.10)


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
	
	def __repr__(self) -> str:
		keys = list(self.cases.keys())
		if len(keys) == 0:
			return "Switch(key):\n\tEmpty"
		out = "Switch(key):"
		for key in keys:
			if key != self.default and key is not None:
				val = self.cases[key]
				if isinstance(val, str):
					val = f'"{val}"'
				out += f"\n\tCase({key}):\n\t\t{val}"
		if self.default != None:
			out += f"\n\tDefault({self.default}):\n\t\t{self.cases[self.default]}"
		return out
	
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
		return self.cases[key] if key in self.cases else (self.cases[self.default] if self.default in self.cases and self.default is not None else None)
