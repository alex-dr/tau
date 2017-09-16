import click


class ClickProvider(click.Group):
    def __init__(self, tau, *args, **kwargs):
        super(click.Group, self).__init__(help=tau.desc)
        self.commands = _gen_click_commands(tau.commands)


def _gen_click_commands(commands):
    """Generate click.Command objects from Tau commands."""
    return {name: click.command(name=name)(fn)
            for name, fn in commands.items()}
