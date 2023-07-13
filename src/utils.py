def is_filename_char(x):
    return True if x.isalnum() else x in ['-', '_']

def URL_to_filename(filename):
    return "".join(x for x in filename if is_filename_char(x))
