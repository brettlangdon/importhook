Importhook
=========

[![PyPI version](https://badge.fury.io/py/importhook.svg)](https://badge.fury.io/py/importhook)

`importhook` is a Python package that lets you configure functions to call whenever a specific module is imported.


## Installation

```bash
pip install importhook
```

## Usage
Configure a hook to be called when `socket` module is imported.

```python
import importhook

# Setup hook to be called any time the `socket` module is imported and loaded into module cache
@importhook.on_import('socket')
def on_socket_import(socket):
    print('"socket" module has been imported')

# Import module
import socket
```


You can also use `importhook` to intercept and modify a module on import by returning a Python module from your hook function.

```python
import importhook

# Setup hook to be called any time the `socket` module is imported and loaded into module cache
@importhook.on_import('socket')
def on_socket_import(socket):
    new_socket = importhook.copy_module(socket)
    setattr(new_socket, 'gethostname', lambda: 'patched-hostname')
    return new_socket

# Import module
import socket

# Prints: 'patched-hostname'
print(socket.gethostname())
```


`importhook` also comes with helpers to reload modules that have already been imported.

```python
import socket
import importhook


# Setup hook to be called any time the `socket` module is imported and loaded into module cache
# DEV: `on_socket_import` will be called immediately because the `socket` module is already loaded
@importhook.on_import('socket')
def on_socket_import(socket):
    print('"socket" module has been imported')


# Reload the socket module
# DEV: Reassign to `socket` in case one of our hooks modifies the module
socket = importhook.reload_module(socket)
```
## Design decisions
### Overwriting sys.meta_path
If a Python developer wants to modify the import behavior they can do so by adding a new `importlib.abc.Finder`
class into `sys.meta_path`.

```python
import sys

# Add our custom `importlib.abc.Finder` to `sys.meta_path`
sys.meta_path.append(MyCustomFinder)
```

One of the major design decisions we have taken with `importhook` is to wrap/overwrite `sys.meta_path`.
What it means is that `importhook` will continue to work as expected regardless of any other modifications of `sys.meta_path`.

There is however one caveat, if you were to do `sys.meta_path = [MyCustomFinder] + sys.meta_path` then `sys.meta_path` will get
converted back into a `list`. Existing modifications to the finders in `sys.meta_path` will still work as expected, but any
new finders added will not get hooked.
