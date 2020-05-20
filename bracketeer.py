# bracketeer.py
# Small application for parsing brackets/braces and other enclosing delimiters.
# Referred to the following stackoverflow entry:
# http://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level
# Gee Hyun Kwon

"""
	Parse the given string to yield the contents between the left and right delimiters.
	Returns a generator that will yield a tuple indicating the depth of the nested enclosure, as well as the content.
	By default, parses out parenthesis ().
	Delimiters are assumed to be single characters.
	Shorthand available for parenthesis (), curly braces/brackets {}, and square brackets [].
	'pr', 'parenthesis', 'parens' for ()
	'br', 'brackets', 'curly braces', 'braces', 'dictionary', 'dict', 'json' for {}
	'sq', 'sb', 'square brackets', 'list' for []

	ex) parsing out ((b, (d)) e)
		will return [(2, 'd'), (1, 'b, (d)'), (0, '(b, (d)) e')]

	args
	s : string to parse
	left : left delimiter, default is (
	right : right delimiter, default is )
	short : optional parameter for shorthands for common forms of braces (see above)
			when supplied, the left and right delimiter arguments will be ignored.
			if given value is not one of the listed shorthands, this argument will be ignored.
"""

def parse(s, left='(', right=')', short='def'):
	# Shorthand information for each types of brackets
	PR_SHORT = ['pr', 'parenthesis', 'parens']
	BR_SHORT = ['br', 'brackets', 'curly braces', 'braces', 'dictionary', 'dict', 'json']
	SQ_SHORT = ['sq', 'sb', 'square brackets', 'list']
	# Check shorthands first to set them accordingly, if given
	if short is not 'def':
		if short in PR_SHORT:
			left = '('
			right = ')'
		elif short in BR_SHORT:
			left = '{'
			right = '}'
		elif short in SQ_SHORT:
			left = '['
			right = ']'
	# Create stack for parsing out values
	stack = []
	# Loop through each character
	for i, c in enumerate(s):
		if c == left:
			# Encountered left delimiter. Add the index to the stack
			stack.append(i)
		# If encountering right delimiter while having encountered left one, pop the stack
		elif c == right and stack:
			start = stack.pop()
			# The current length of stack after popping denotes how deep we are
			# i.e. the delimiters left to be popped
			# Since we popped one just before, we add 1 to the popped 
			yield (len(stack) + 1, s[start + 1:i])