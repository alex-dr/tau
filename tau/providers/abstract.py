class NotImplementedError(Exception):
    """Function is not implemented."""
    pass


class AbstractProvider(object):
    """Abstract tau provider class.

    Abstract interface for tau providers.

    Providers can take many forms, from REST servers and Click interfaces to
    RabbitMQ servers and workers or Slackbots.

    Feel free to build your own provider! Before you do so, first read through
    these methods and docstrings to get a better feeling for what each method
    does.
    """
    def __init__(self, tbar):
        """Instantiate your provider class.

        This is the best way to add runtime configuration to your provider.

        For example, a REST server might want to be configured with the
        binding address and port, or a slackbot configured with secrets.

        Parameters
        ----------
        tbar : tau.Tau
            Instantiated tbar from which to build the provider.
        """
        return None
