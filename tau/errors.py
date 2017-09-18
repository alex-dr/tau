class SpecValidationError(Exception):
    """Some object failed to validate its specification."""
    def __init__(self, item, exc=None):
        self.exc = exc
        self.item = item

    def __str__(self):
        if self.exc:
            msg = ('Spec failed to validate this key: {}\n'
                   'Exception raised was: {}: {}'.format(self.item,
                                                         type(self.exc),
                                                         self.exc))
            return msg
