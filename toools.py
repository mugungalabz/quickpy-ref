
def sha256(s):
    import hashlib
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def reverse_string(s):
    return s[::-1]
