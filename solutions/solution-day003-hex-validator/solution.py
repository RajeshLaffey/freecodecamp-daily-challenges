def is_valid_hex(s):
    hex_char = "abcedf0123456789"
    modified_s = s[1:]

    if not isinstance(s, str):
        return False
    
    if len(modified_s) not in (3,6):
        return False
    
    if s.startswith("#"):
        for letter in modified_s:
            if letter.lower() not in hex_char:
                return False
        return True
