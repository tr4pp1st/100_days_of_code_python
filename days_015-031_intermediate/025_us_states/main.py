# 100 Days of Code: Python
# Day 25 Project: U.S. States Game

from map_view import MapView
from state_manager import StateManager

# --- Initialize game components ---
map_view = MapView("data/blank_states_img.gif")
state_manager = StateManager("data/50_states.csv")

# --- Game loop ---
while not state_manager.all_states_guessed():
    answer_state = map_view.prompt_for_state(state_manager.correct_count())

    # User closed dialog.
    if not answer_state:
        break

    if answer_state.lower() == "exit":
        state_manager.save_missing_states("output/states_to_learn.csv")
        break

    if state_manager.is_correct(answer_state):
        x, y = state_manager.get_coordinates(answer_state)
        map_view.mark_state(answer_state, x, y)

map_view.exit_on_click()
