
class Util(object):
	@classmethod
	def string_to_upper(cls, str_in):
		if str_in.isdigit() is False:
			return str_in.upper()
		else:
			return 0
	@classmethod
	def cut_string(cls, str_in):
		if str_in.isdigit() is False:
			size = len(str_in) - 10
			if size <= 0:
				raise Exception("String too low")

			result = str_in[:size] + "..."
			return result
		else:
			return 0

