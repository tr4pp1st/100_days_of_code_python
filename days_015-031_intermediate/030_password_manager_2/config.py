"""
Central configuration for the Password Manager project.

Note:
In a production environment, sensitive or user-specific values should be loaded from environment variables
or a secure config store, not hardcoded.
"""

CONFIG = {
    # --- UI Defaults ---
    "user_mail_standard_value": "testuser@testmail.com",    # TODO: Load from env var in PROD.

    # --- Validation Rules ---
    "website_len_min": 1,
    "user_len_min": 5,
    "password_len_min": 8,

    # --- Password Generation Rules ---
    "lowercase": 4,
    "uppercase": 4,
    "numbers": 2,
    "symbols": 4,

    # --- File Management ---
    "data_file_path": "data/passwords.json"     # TODO: Add to .gitignore in PROD.
}
