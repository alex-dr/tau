"""Simple pycontract contracts."""
from contracts import new_contract
from string import ascii_lowercase, ascii_uppercase


single_char = new_contract(
    'tau_single_char',
    lambda x: len(x) == 1 and x in ascii_lowercase)

single_char = new_contract(
    'tau_desc',
    lambda x: x[0] in ascii_uppercase and x.endswith('.'))
