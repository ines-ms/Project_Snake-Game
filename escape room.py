class Room:
    def __init__(self, name, description, puzzles, transitions):
        self.name = name
        self.description = description
        self.puzzles = puzzles  # Now a list of puzzles
        self.transitions = transitions  # Dict mapping from puzzle answers to next rooms

    def enter_room(self, inventory):
        print(f"\n{self.description}")

        for puzzle in self.puzzles:
            print(puzzle["question"])
            player_answer = input("> ")

            if player_answer.lower() in puzzle["answers"]:
                print("Correct answer!")
                if "item" in puzzle:
                    inventory.add(puzzle["item"])
                    print(f"You found a {puzzle['item']}!")
            else:
                print("That's not right. You can try the puzzle again, explore the room, or use an item.")
                break  # Breaks out of the puzzle loop to explore or use items

        action = input("What would you like to do? (explore/use item/move on) > ")
        if action == "use item":
            item_used = input("Which item would you like to use? > ")
            if item_used in inventory:
                print(f"Using {item_used}...")
                if item_used in self.transitions:
                    return self.transitions[item_used]
                else:
                    print(f"Nothing happened with the {item_used}.")
                    return self.name
            else:
                print("You don't have that item.")
                return self.name
        elif action == "move on":
            return self.transitions.get("next", self.name)
        else:
            return self.name


class Game:
    def __init__(self, rooms):
        self.rooms = rooms
        self.current_room = 'start'
        self.inventory = set()

    def play(self):
        while True:
            next_room_name = self.rooms[self.current_room].enter_room(self.inventory)
            if next_room_name == 'exit':
                print("\nCongratulations! You've escaped the room and uncovered the secret of the mansion!")
                break
            self.current_room = next_room_name
def main():
    rooms = {
        'start': Room("start",
                      "You wake up in a cold, dimly lit room. A locked door stands ominously before you.",
                      [{"question": "A note says, 'To leave this place, you must find the truth hidden in plain sight.' What is 9+10?",
                        "answers": ["19"]}],
                      {"next": "library"}),
        'library': Room("library",
                        "Books line the walls, a dust-covered tome catches your eye.",
                        [{"question": "The tome whispers, 'I can bring down cities but not a whisper. What am I?'",
                          "answers": ["silence"],
                          "item": "key"}],
                        {"key": "secret_study"}),
        'secret_study': Room("secret_study",
                             "A secret room filled with ancient artifacts. A locked chest sits in the center.",
                             [{"question": "The chest demands, 'Feed me and I live, yet give me a drink and I die. What am I?'",
                               "answers": ["fire"],
                               "item": "map"}],
                             {"map": "hidden_passage"}),
        'hidden_passage': Room("hidden_passage",
                               "A narrow passage hidden behind the study, leading to the unknown.",
                               [],
                               {"next": "exit"}),
        'exit': Room("exit",
                     "The light of the outside world greets you. You've uncovered the secret and escaped with knowledge untold.",
                     [],
                     {})
    }

    game = Game(rooms)
    game.play()

if __name__ == "__main__":
    main()
