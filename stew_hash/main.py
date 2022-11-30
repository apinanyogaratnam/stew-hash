def hash(message: str) -> str:
    """
    Hashes a message
    """
    # return hashlib.sha256(message.encode()).hexdigest()
    sum_of_ascii_values = sum(ord(char) for char in message)
    return str(sum_of_ascii_values)
