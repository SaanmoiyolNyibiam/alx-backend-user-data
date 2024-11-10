#!/usr/bin/env python3
"""
This is a module that defines a filter datum function
"""
import re


def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    """
    Returns a log message obfuscated
    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character
        is separating all fields in the log line (message)
    """

    filtered_datum: str = message
    for field in fields:
        pattern: str = f"(?<={field}=)[^{separator}]+"
        filtered_datum = re.sub(pattern, redaction, filtered_datum)
    return filtered_datum
