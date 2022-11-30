from stew_hash.main import hash


class TestMain:
    def test_greetings_return_value(self):
        assert hash('secret message') == '1419'

    def test_greetings_return_type(self):
        assert isinstance(hash('1419'), str)
