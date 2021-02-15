import uuid


def get_random_code():
    """
    :return: a generated universally unique identifier ie random objects of 128 bits as ids
    """
    code = str(uuid.uuid4())[:8].replace('-', '').lower()
    return code
