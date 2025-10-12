import json
import os
from entry import Entry
from tkinter import messagebox
from typing import List

# NOTE: In production, make sure to add this file to .gitignore to avoid exposing sensitive data.
FILE_PATH = "data/passwords.json"


class FileManager:
    def __init__(self):
        self.data = []
        self.file_path = FILE_PATH

    def convert_entry_to_json(self, entry: Entry):
        """Convert an entry into the json format."""
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
        entries = self.convert_json_to_entry(data)
        for _ in entries:
            if _.website.lower() == new_entry.website.lower() and _.user == new_entry.user:
                return True
        return False


    def save_new_entry(self, new_entry: Entry):
        """If the file already exists, add the new entry only, else create the file with the new entry."""
        all_good, error_message = new_entry.validate()
        if not all_good:
            messagebox.showerror(title="Error", message=f"{error_message}")
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
        print(data)
        return data
