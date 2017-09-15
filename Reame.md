# Tau

## Installation

```bash
cd tau
mkvirtualenv tau
pip install -e .
```

## Usage

Say you have a simple Python library.

```python
# file readme/main.py
def echo(msg):
    print(msg)


def add(x, y):
    return x + y


def cat(file, loudly=False):
    with open(file, 'r') as f:
        if loudly:
            return f.read().upper
        else:
            return f.read()
```

Nice work!
Now you want to turn these functions into a CLI, or a REST API server, while still allowing other developers to use them in their own code.

Everyone knows how to use libraries like Click and Flask to create powerful applications.
However, you'd like to create multiple interfaces, with consistent input validation, and minimal boilerplate code.

You'd also like to be able to set your parameter values as config files, environment variables, CLI flags, query parameters, or more.
Surely there's some tool that can take some functions, their inputs, and their outputs, and create these interfaces for you automatically.

As a good programmer, you'd like to make it easy to test these functions, without excessive mocks or boilerplate code.

And finally, you'd like to keep adding new features and refactoring as easy as possible.

That's what `tau` is for.

With `tau` it's easy to create simple, clean interfaces to your library functions without tedious boilerplate code.
You simply declare your interfaces in-place and `tau` takes care of the rest.

Let's see `tau` in action.
Check out how to use `tau` with the above libray example in the [examples](examples/readme/) folder.
If you're familiar with `Click` and `pycontracts`, some of this will seem familiar.

Now that we've read through the implementation, let's see what we can do:

### tau Example Usage
```bash
$ pip install examples/readme/
$ readme --help
Usage: readme [OPTIONS] COMMAND [ARGS]...

  Example Readme Command-Line Interface.

Options:
  --help  Show this message and exit.

Commands:
  echo  Display a message on stdout.
  math  Utterly trivial math utilities.
  cat   Read a file, quietly?
$ readme cat /tmp/foo --loud
OH HAI DER
$ readme-serve
Usage: readme-serve [OPTIONS] command [ARGS]...

  Example Readme REST Interface Server.

Options:
  --help  Show this message and exit.

Commands:
  debug       Run server in debug mode.
  production  Run server in production mode.
$ python -c 'from readme import math; print(math.add(1, 2))'
3
$
```

## Why the name?

`τ` is the name of my cat.

`tau` is easier to spell.

What else do you want?
