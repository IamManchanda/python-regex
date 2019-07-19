import re
def parse_name(input):
	name_regex = re.compile(r"^(Mr\.|Mrs\.|Ms\.|Mdme\.)\s(?P<first>[A-Za-z]+)\s(?P<last>[A-Za-z]+)$")
	matches = name_regex.search(input)
	print(matches.group())
	print(matches.group('first'))
	print(matches.group('last'))

parse_name("Mrs. Tilda Swinton")
