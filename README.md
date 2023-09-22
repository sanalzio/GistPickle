# GistPickle
It uses the pickle module to save variables to Gists, allowing you to save variables to a file and retrieve them in another code.

# Requirements
- Python 3
- **pygistdb** (My module) [Download!](https://github.com/sanalzio/PyGistDB)
- requests
  - `pip install requests`
- os
- pickle

# Usage

## add variable
code1:
```py
import gistpicke
gist=gistpicke.congist("gistid", "filename", "token")
x="Hello, gistpickle!"
gist.save_var("example1", x)
```
code2:
```py
import gistpicke
gist=gistpicke.congist("gistid", "filename", "token")
print(gist.get_var("example1"))
```
code2 output:
> Hello, gistpickle!

## get variable
code:
```py
import gistpicke
gist=gistpicke.congist("gistid", "filename", "token")
print(gist.get_var("example1"))
```
code output:
> Hello, gistpickle!

## set variable
code1:
```py
import gistpicke
gist=gistpicke.congist("gistid", "filename", "token")
x="Hello"
gist.set_var("example1", x)
```
code2:
```py
import gistpicke
gist=gistpicke.congist("gistid", "filename", "token")
print(gist.get_var("example1"))
```
code2 output:
> Hello

## delete variable
code:
```py
import gistpicke
gist=gistpicke.congist("gistid", "filename", "token")
gist.del_var("example1")
```