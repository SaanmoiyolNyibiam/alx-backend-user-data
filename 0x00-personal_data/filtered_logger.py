#!/usr/bin/env python3
"""
This is a module that defines a filter datum function
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, msg: str, sep: str) -> str:
    """
    Returns a log msg obfuscated
    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        msg: a string representing the log line
        sep: a string representing by which character
        is separating all fields in the log line (msg)
    """
    for field in fields:
        msg = re.sub(f'{field}=.*?{sep}',
                     f'{field}={redaction}{sep}', msg)
    return msg
