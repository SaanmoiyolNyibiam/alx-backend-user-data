#!/usr/bin/env python3
"""
This is a module that defines a filter datum function
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns a log message obfuscated
    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character
        is separatorarating all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                     f'{field}={redaction}{separator}', message)
    return message
