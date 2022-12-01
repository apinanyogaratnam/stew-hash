def hash(message: str) -> str:
    """
    Hashes a message
    """
    # return hashlib.sha256(message.encode()).hexdigest()
    sum_of_ascii_values = sum(ord(char) for char in message)
    return str(sum_of_ascii_values)


def hash_1(message: str) -> str:
    """
    Hashes a message
    """
    ascii_values = [ord(char) for char in message]
    ascii_values = [ascii_value ** 2 for ascii_value in ascii_values]
    return str(sum(ascii_values))
