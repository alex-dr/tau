"""The example from the readme."""
# file <package>/main.py
import tau
from tau.contracts import readable_file

iface = tau.Tau()


@iface.command()
@tau.argument(
    name='msg',
    contract='string',
    default='Hello World!',
    env_var='TAUDEMO_MSG',
    desc='Message to print',
)
def echo(msg):
    print(msg)


math = iface.group('math')

addable_arg = tau.argument(
    contract=lambda x: hasattr(x, '__add__'),
    desc='Number to add.')


@math.command()
@addable_arg
@addable_arg
def add(x, y):
    return x + y


@iface.command()
@tau.argument(
    name='fname',
    contract=readable_file,
    default='/etc/passwd',
    env_var='TAUDEMO_FILE',
    desc='Read the contents of a file on disk.',
)
@tau.option(
    name='loudly',
    contract='bool',
    desc='Read a file',
)
def read_file(fname, loudly=False):
    with open(fname, 'r') as f:
        if loudly:
            return f.read().upper()
        else:
            return f.read()


cli = iface.click()
app = iface.flask()

if __name__ == '__main__':
    app.run(host='localhost', port=62831, debug=True)
