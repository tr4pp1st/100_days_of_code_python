from config import CONFIG


class Entry:
    """Represents a single password entry with basic validation."""
    def __init__(self, website: str = "", user: str = "", password: str = ""):
        self.website = website.strip()
        self.user = user.strip()
        self.password = password.strip()

    def validate(self):
        """Check if the entry meets minimum length requirements."""
        errors = []

        fields = {
            "website": (self.website, CONFIG["website_len_min"]),
            "user": (self.user, CONFIG["user_len_min"]),
            "password": (self.password, CONFIG["password_len_min"]),
        }

        for name, (value, min_len) in fields.items():
            if len(value) < min_len:
                errors.append(f"The {name} length is too short ({len(value)}). Minimum is {min_len}")

        return not errors, errors
