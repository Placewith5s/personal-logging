# Personal Logging
A Python library for colored common logs with customization support.


## Installation
```sh
pip3 install personal-logging
```


## Usage
```python
from personal_logging.main import warn, error

warn("Caution!")
error("Uh oh!")
```

## Defaults
### Variables
```python
warn_emoji = "⚠️"
error_emoji = "❌"
```

### Parameters
```python
identifier_on=True
emojis=True
```
