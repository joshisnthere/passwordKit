"""
Entropy estimation and generation. The crack-time number is a simplified
model (guesses per second is a round assumption, not a benchmark) -- good
for relative comparison, not a precise security audit.
"""

import math
import secrets
import string

GUESSES_PER_SECOND = 1e10  # rough offline-attack assumption


def _charset_size(password):
    size = 0
    if any(c.islower() for c in password):
        size += 26
    if any(c.isupper() for c in password):
        size += 26
    if any(c.isdigit() for c in password):
        size += 10
    if any(c in string.punctuation for c in password):
        size += len(string.punctuation)
    return max(size, 1)


def analyze(password):
    charset_size = _charset_size(password)
    entropy = round(len(password) * math.log2(charset_size), 1)