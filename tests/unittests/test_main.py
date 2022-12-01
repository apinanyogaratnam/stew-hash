from stew_hash.main import hash, hash_1


class TestMain:
    def test_greetings_return_value(self: 'TestMain'):
        assert hash('secret message') == '1419'

    def test_greetings_return_type(self: 'TestMain'):
        assert isinstance(hash('1419'), str)

    def test_greetings_return_value_1(self: 'TestMain'):
        assert hash_1('secret message') == '149655'

    def test_greetings_return_type_1(self: 'TestMain'):
        assert isinstance(hash_1('secret message'), str)
