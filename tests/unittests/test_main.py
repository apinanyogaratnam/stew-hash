from stew_hash.main import hash


class TestMain:
    def test_greetings_return_value(self):
        print(hash('secret message'))
        assert hash('secret message') == "secret message"

    def test_greetings_return_type(self):
        assert isinstance(hash('secret message'), str)
