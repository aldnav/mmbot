
from utils import terms


def test_get_terms():
    text = '@aldnav hi'
    assert '@aldnav' in terms.get_terminologies(text)
    terms.save_new_terms(text)


test_get_terms()
