import uuid

def gen_id():
    """
    获取32位uuid
    """
    return uuid.uuid4().hex

