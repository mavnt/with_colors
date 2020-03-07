# with_colors

Wrapper for python module [colorama](https://github.com/tartley/colorama).

with `colorama`:

```python
from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
```

with `with_colors`:

```python
from with_colors import *

with color(red):
    print('some red text')
    with background(green):
        print('and a green background')
        with style(dim):
            print('and in dim text')
print('back to normal now')
```
