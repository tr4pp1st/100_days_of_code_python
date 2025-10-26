import json
import os
from entry import Entry
from tkinter import messagebox
from typing import List
from config import CONFIG


class FileManager:
    """Handles file operations for storing and retrieving password entries."""
    def __init__(self):
        self.data = []
        self.file_path = CONFIG.get("data_file_path", "")

    def convert_entry_to_json(self, entry: Entry):
        """Convert an entry into JSON format."""
        return {
            "website": entry.website,
            "user": entry.user,
            "password": entry.password
        }


    def convert_json_to_entry(self, data: List[dict]) -> list[Entry]:
        """Convert a list of JSON dicts to a list of Entry objects."""
        entries = []
        for item in data:
            entry_obj = Entry(
                website=item.get("website", ""),
                user=item.get("user", ""),
                password=item.get("password", "")
            )
            entries.append(entry_obj)
        return entries


    def entry_already_exists(self, data: List[dict], new_entry: Entry) -> bool:
        """Check whether an entry with the same website and user already exists."""
        entries = self.convert_json_to_entry(data)
        for _ in entries:
            if _.website.lower() == new_entry.website.lower() and _.user == new_entry.user:
                return True
        return False

    def save_new_entry(self, new_entry: Entry):
        """If the file already exists, add the new entry only, else create the file with the new entry."""
        all_good, errors = new_entry.validate()
        if not all_good:
            messagebox.showerror(title="Validation Error", message="\n".join(errors))
            return

        json_entry = self.convert_entry_to_json(new_entry)

        data = self.load_file()
        if not self.entry_already_exists(data, new_entry):
            data.append(json_entry)
        else:
            messagebox.showinfo(title="Info", message="Entry already exists.")
            return

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
            messagebox.showinfo(title="Info", message="Added new entry successfully.")

    def load_file(self) -> []:
        """Load the file if exists, else return []."""
        data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        return data

    def search_password(self, website: str, user: str):
        """Search for a password by website and user."""
        data = self.load_file()
        if not data:
            messagebox.showinfo(title="No Data", message="Password file is empty or missing.")
        else:
            entries = self.convert_json_to_entry(data)
            for _ in entries:
                if _.website.lower() == website.lower() and _.user.lower() == user.lower():
                    messagebox.showinfo(title=f"{website}", message=f"Mail: {user}\nPassword: {_.password}")
                    return
            messagebox.showinfo(title=f"{website}", message=f"Mail: {user}\nPassword: No password found.")
