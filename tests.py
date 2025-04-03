import pytest
from dashboard import health_checker

def test_health_checker():
    assert health_checker('vm_ubuntu')=='Offline'

test_health_checker()