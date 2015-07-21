__author__ = 'riqv'
from validate import Validator

def test_players(config):
        validator = Validator()
        val = config.validate(validator)
        return val