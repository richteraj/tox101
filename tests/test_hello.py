"""A simple test to demonstrate tox's testing matrix."""

from tox101.hello import hello_world


def test_hello_string():
    """This is how You write this phrase."""
    assert hello_world() == "Hello, world!"
