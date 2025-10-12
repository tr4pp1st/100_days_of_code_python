VALIDATION_CONFIG = {
    "website_len_min": 3,
    "user_len_min": 3,
    "password_len_min": 3,
}


class Entry:
    def __init__(self, website: str = "", user: str = "", password: str = ""):
        self.website = website
        self.user = user
        self.password = password

    def validate(self):
        """Check if the entry meets minimum length requirements."""
        errors = []

        fields = {
            "website": (self.website, VALIDATION_CONFIG["website_len_min"]),
            "user": (self.user, VALIDATION_CONFIG["user_len_min"]),
            "password": (self.password, VALIDATION_CONFIG["password_len_min"]),
        }

        for name, (value, min_len) in fields.items():
            if len(value) < min_len:
                errors.append(f"The {name} length is too short ({len(value)}). Minimum is {min_len}")

        return len(errors) == 0, errors
