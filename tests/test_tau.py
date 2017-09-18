import tau

import pytest


@pytest.fixture()
def tbar():
    return tau.Tau(desc='Test instance.')


def test_command(tbar):
    @tbar.command()
    def foo():
        pass

    assert tbar.commands
    assert isinstance(tbar.commands, dict)
    assert tbar.commands['foo']
    assert foo.func_name == 'foo'
    assert foo() is None


def test_command_name(tbar):
    @tbar.command(name='bar')
    def foo():
        print('hi alex')
        return True

    fn = tbar.commands['bar']
    assert fn
    assert fn.func_name == 'foo'
    # ipdb.set_trace()
    assert fn() is True
    assert foo() is True


def test_command_with_arg(tbar):
    @tbar.command()
    @tau.argument('bar', default='baz')
    def foo(bar):
        return 'called with {}'.format(bar)

    assert tbar.commands
    assert 'baz' in foo()


def test_arg_schema():
    for name, spec in tau.ARG_SCHEMA.items():
        assert 'contract' in spec
        assert 'desc' in spec
