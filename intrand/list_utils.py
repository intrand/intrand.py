#!/usr/bin/env python3

def excludeListFromList(_list=[], _remove=[]):
	"""
	Builds a new list without items passed through as _remove.
	"""
	_remove = set(_remove)
	return [i for i in _list if i not in _remove]
