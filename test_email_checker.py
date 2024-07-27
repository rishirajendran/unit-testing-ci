import pytest


@pytest.mark.parametrize("input, expected", [
    ("rRAJ123", True),
    ("r.raGj1", True),
    ("r1--raj", False),
    ("r__raj", False),
    ("r..raj", False),
    ("r.-r8aj", True),
    ("-rra5j", False),
    (".rr3aj", False),
    ("_rraj", False),
    ("rraj-", False),
    ("rraj.", False),
    ("rraj_", False),
    ("rrTaj ", True),
    ("9rraj  ", False),
    (" rraj ", False),
    ("rraj 6", False)
    ])
def test_is_prefix(input, expected):
    from email_checker import is_prefix
    answer = is_prefix(input)
    assert answer == expected


@pytest.mark.parametrize("input, expected", [
    ("rRA-J12-3", True),
    ("r.raGj1", False),
    ("r1--raj", False),
    ("r__raj", False),
    ("r.ra4j", False),
    ("r.-r8aj", False),
    ("-rra5j", False),
    ("rra5j-", False),
    (".rr3aj", False),
    ("_rraj", False),
    ("rraj-", False),
    ("rraj.", False),
    ("rraj*", False),
    ("rrT3aj ", False),
    (" 9rraj ", False),
    (" rR1aj", True),
    ("rraj 6", False)
    ])
def test_is_domain(input, expected):
    from email_checker import is_domain
    answer = is_domain(input)
    assert answer == expected


@pytest.mark.parametrize("input, expected", [
    ("rRA-J12-3", False),
    ("rRaGj", True),
    (" 9rraj ", False),
    (" rR1aj", False),
    ("rrAj l", False)
    ])
def test_is_toplevel(input, expected):
    from email_checker import is_toplevel
    answer = is_toplevel(input)
    assert answer == expected


@pytest.mark.parametrize("input, expected", [
    ("r1.Ra3J@duke.edu", True),
    ("r1.Ra7J @duke.edu", True),
    ("r1.2Ra9J @ duke.edu", True),
    ("  r1.Ra3J @ duke.edu  ", True),
    ("r1.Ra3Jduke.edu", False),
    ("r1.Ra3J  @duke.edu", False),
    ("r1.Ra3J@  duke.edu", False),
    (" ", False),
    ("  @  ", False),
    ("d..w@duke.edu", False),
    ("1d.-w@duke.edu", True),
    ("1d.-w@dukeedu", False)
    ])
def test_is_email(input, expected):
    from email_checker import is_email
    answer = is_email(input)
    assert answer == expected
