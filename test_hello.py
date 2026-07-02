from hello import hello_world

def test_hello_world_with_name():
    assert hello_world("Alice") == "Hello, Alice!"
    assert hello_world("Bob") == "Hello, Bob!"

def test_hello_world_with_empty_string():
    assert hello_world("") == "Hello, !"
