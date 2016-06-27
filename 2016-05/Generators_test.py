import pytest
import Generators

def test_multiples():
	

def test_get_number_from_user():
	assert Generators.get_number_from_user() > 0
	assert Generators.get_number_from_user() != str

def test_euler_one_generator():
	assert Generators.euler_one_generator(9) == 23
	assert Generators.euler_one_generator(999) == 233168