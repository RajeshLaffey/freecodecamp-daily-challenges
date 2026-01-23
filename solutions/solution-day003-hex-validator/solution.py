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

is_valid_hex("#ABCDEF")   # True
is_valid_hex("#0a1B2c")   # True
is_valid_hex("#fff")      # True

is_valid_hex("ABCDEF")    # False
is_valid_hex("#12345")    # False
is_valid_hex("#12x")      # False
