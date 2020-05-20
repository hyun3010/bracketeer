# Bracketeer unit test module
import bracketeer, pytest

# Since the parse function in bracketeer returns a generator, we need to pack it into a list of tuples

def test_bracketeer():
	# Define test cases

	# Test case input
	# Case 1: Simple test for parenthesis
	in_1 = '(parenthesis)'
	# Case 2: Simple test for nested parenthesis
	in_2 = '(parenthesis (inside parenthesis))'
	# Case 3: Mixed test to verify extraction of values inside parenthesis only
	in_3 = 'outside (inside) again outside'
	# Case 4: Test for parenthesis values between nested values
	in_4 = '(parens (between) another parens)'
	# Case 5: Complex test for multiple levels of nesting
	in_5 = 'outside (first (second (third (fourth)) (another third)) level (another (3)second))'
	# Case 6: Test for brackets
	in_6 = '{{first}, {second, bracket}, {third, {third nested}}}'
	# Case 7: Test for square brackets
	in_7 = '[[first] [second [third]]]'
	# Case 8: Test for custom delimiters - left delimiter is &, right is !

	# Expected test case output
	# Case 1: Simple test for parenthesis
	out_1 = [(1, 'parenthesis')]
	# Case 2: Simple test for nested parenthesis
	out_2 = [(2, 'inside parenthesis'), (1, 'parenthesis (inside parenthesis)')]
	# Case 3: Mixed test to verify extraction of values inside parenthesis only
	out_3 = [(1, 'inside')]
	# Case 4: Test for parenthesis values between nested values
	out_4 = [(2, 'between'), (1, 'parens (between) another parens')]
	# Case 5: Complex test for multiple levels of nesting
	out_5 = [(4, 'fourth'), (3, 'third (fourth)'), (3, 'another third'), (2, 'second (third (fourth)) (another third)'),
			(3, '3'), (2, 'another (3)second'), (1, 'first (second (third (fourth)) (another third)) level (another (3)second)')]
	# Case 6: Test for brackets
	out_6 = [(2, 'first'), (2, 'second, bracket'), (3, 'third nested'), (2, 'third, {third nested}'), 
			(1, '{first}, {second, bracket}, {third, {third nested}}')]
	# Case 7: Test for square brackets
	out_7 = [(2, 'first'), (3, 'third'), (2, 'second [third]'), (1, '[first] [second [third]]')]
	# Case 8: Test for custom delimiters - left delimiter is &, right is !

	# Assertion for each case
	# When available, the default arguments - () and the shorthands will be tested for each case
	# Because bracketeer's parse function returns a generator, we need to iterate and wrap into a list

	# Case 1: Test using default left, right parameters
	assert out_1 == [t for t in bracketeer.parse(in_1)]
	assert out_1 == [t for t in bracketeer.parse(in_1, short='pr')]
	assert out_1 == [t for t in bracketeer.parse(in_1, left='(', right=')')]
	assert out_2 == [t for t in bracketeer.parse(in_2)]
	assert out_3 == [t for t in bracketeer.parse(in_3)] 
	assert out_4 == [t for t in bracketeer.parse(in_4)]
	assert out_5 == [t for t in bracketeer.parse(in_5)]
	assert out_6 == [t for t in bracketeer.parse(in_6, short='br')]
	assert out_6 == [t for t in bracketeer.parse(in_6, left='{', right='}')]
	assert out_7 == [t for t in bracketeer.parse(in_7, left='[', right=']')]
	assert out_7 == [t for t in bracketeer.parse(in_7, short='sq')]
