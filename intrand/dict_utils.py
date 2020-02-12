#!/usr/bin/env python3

def merge(_input={}, _output={}):
	"""
	Recursively puts missing fields/values into _output (dict) using _input (dict) as input.
	Useful for, eg, applying some default values to a dictionary of user inputted configuration.
	"""
	_output = _output.copy()
	for _key, _value in _input.items(): # loop through each key/value pair
		if (_key in _output) and isinstance(_value, dict): # detect when we need to recurse
			_output[_key] = merge(_value, _output[_key]) # recurse
		else: # _key is not in output
			if not _key in _output: # don't overwrite existing values
				_output[_key] = _value # add missing key/value pair

	return _output # give back the merged dict

def classToDict(obj=None):
	"""
	Transform an object into a dict so it can be JSONified.
	Useful for turning custom classes into JSON-compatible dictionaries.
	"""
	if obj == None:
		return {}

	_obj = {}
	_obj.update(obj.__dict__)

	return _obj
