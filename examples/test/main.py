import tau

tbar = tau.Tau(desc='testing testing 123')


@tbar.command(name='baz')
def foo():
    """Beautiful docstring."""
    print('hello world')


@tbar.command()
@tau.argument(
    'eilo',
    short='e',
    desc='Meow.',
)
def bar(eilo):
    """Yet Another Beautiful docstring."""
    print('hello {}'.format(eilo))


cli = tbar.get_provider('cli')
