import string
import random

PASSWORD_CONFIG = {
    "lowercase": 4,
    "uppercase": 4,
    "numbers": 2,
    "symbols": 4
}


# NOTE: In production, passwords should always be stored in an encrypted form instead of plain text.
class PasswordGenerator:
    def __init__(self):
        self.config = PASSWORD_CONFIG
        self.raw = []

    def generate_password(self) -> str:
        self.raw = []

        char_sets = {
            "lowercase": string.ascii_lowercase,
            "uppercase": string.ascii_uppercase,
            "numbers": string.digits,
            "symbols": string.punctuation,
        }

        for key, chars in char_sets.items():
            for _ in range(self.config[key]):
                self.raw.append(random.choice(chars))

        random.shuffle(self.raw)
        return "".join(self.raw)
