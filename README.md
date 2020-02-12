# intrand.py
Python utilities that are useful in their own little ways.

# Installation
pip: `pip install --upgrade intrand`

# Usage
```python
import intrand

# some default values
defaults = {
	"preferences":{
		"color":"blue",
		"size":"medium",
		"gradient":True
	}
}

# some user input (perhaps via API)
userConfig = {
	"id":1234567890,
	"name":{
		"first":"John",
		"middle":"James",
		"last":"Smith"
	},
	"preferences":{
		"color":"gray"
	}
}

intrand.dict_utils.merge(defaults, userConfig)	# merge keys present in defaults,
												# but missing in userConfig
												# into userConfig

print(userConfig)

```
