def number(n):
    n = int(n + (0.5 if n > 0 else -0.5))
    return n


def human_read_format(size):
    if size >= 1024 * 1024 * 1024:
        return str(int_r(size / (1024 * 1024 * 1024))) + 'ГБ'
    elif size >= 1024 * 1024:
        return str(int_r(size / (1024 * 1024))) + 'МБ'
    elif size >= 1024:
        return str(int_r(size / 1024)) + 'КБ'
    else:
        return str(size) + 'Б'



print(human_read_format(15000))