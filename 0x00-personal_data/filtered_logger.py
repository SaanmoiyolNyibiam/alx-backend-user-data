#!/usr/bin/env python3
"""
This is a module that defines a filter datum function
"""
import re


def filter_datum(fields: list, redaction: str, msg: str, sep: str) -> str:
    """
    Returns a log msg obfuscated
    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        msg: a string representing the log line
        sep: a string representing by which character
        is separating all fields in the log line (msg)
    """

    filtered_datum: str = msg
    for field in fields:
        pattern: str = f"(?<={field}=)[^{sep}]+"
        filtered_datum = re.sub(pattern, redaction, filtered_datum)
    return filtered_datum
