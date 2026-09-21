"""
Entropy estimation and generation. The crack-time number is a simplified
model (guesses per second is a round assumption, not a benchmark) -- good
for relative comparison, not a precise security audit.
"""

import math
import secrets
import string

GUESSES_PER_SECOND = 1e10  # rough offline-attack assumption

