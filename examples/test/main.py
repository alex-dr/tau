from tau import Tau

tbar = Tau(desc='testing testing 123')


@tbar.command(name='baz')
def foo():
    """Beautiful docstring."""
    print('hello world')


@tbar.command()
def bar():
    """Yet Another Beautiful docstring."""
    print('hello {}'.format('asdf'))


cli = tbar.get_provider('cli')
