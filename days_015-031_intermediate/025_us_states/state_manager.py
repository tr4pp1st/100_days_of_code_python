import pandas


class StateManager:
    """Handles state data, guesses, and saving progress."""

    def __init__(self, csv_path: str):
        self.data = pandas.read_csv(csv_path)
        self.all_states = self.data.state.tolist()
        self.guessed_states = []

    def is_correct(self, name: str) -> bool:
        """Check if a guessed state is valid and not already guessed."""
        name = name.title()
        if name in self.all_states and name not in self.guessed_states:
            self.guessed_states.append(name)
            return True
        return False

    def get_coordinates(self, state_name: str) -> tuple[int, int]:
        """Return (x, y) coordinates of a state."""
        state = self.data[self.data.state == state_name]
        return int(state.x.item()), int(state.y.item())

    def save_missing_states(self, output_path: str):
        """Save a CSV of states not yet guessed."""
        missing_states = []
        for state in self.all_states:
            if state not in self.guessed_states:
                missing_states.append(state)

        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv(output_path)

        # Shorter.
        # missing_states = [state for state in self.all_states if state not in self.guessed_states]
        # pandas.DataFrame(missing_states).to_csv(output_path)

    def all_states_guessed(self):
        return len(self.guessed_states) >= len(self.all_states)

    def correct_count(self):
        return len(self.guessed_states)
