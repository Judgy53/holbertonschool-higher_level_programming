#!/usr/bin/python3
def remove_char_at(str, n):
    out = ""
    for (idx, c) in enumerate(str):
        if idx != n:
            out += c

    return out
