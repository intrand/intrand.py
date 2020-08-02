#!/usr/bin/env python3

def merge(incoming={}, output={}, overwrite=False):
	"""
	Resursively merges two dictionaries by taking inputs from the 'incoming' dictionary and overlaying them upon the 'output' dictionary.

	By default, no values in the resulting dictionary will be overwritten if present in both.
	Passing 'overwrite=True' will flip this behavior.

	Useful for, eg, applying some user-inputted configuration (incoming) over top of some already-existing (default) values (output).
	"""
	_output = output.copy()
	for _key, _value in incoming.items(): # loop through each key/value pair
		if (_key in _output) and isinstance(_value, dict): # detect when we need to recurse
			_output[_key] = merge(_value, _output[_key]) # recurse
		else: # _key is not in output
			if _key in _output and overwrite == False: # we check if it already exists, and if we care
				continue # don't overwrite existing values unless overwrite is 'True'
			_output[_key] = _value # add key/value pair

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
