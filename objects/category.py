class Category():
    def __init__(self, name, api_provider, toggle = False):
        self.name = name
        self.toggle = toggle
        self.api_provider = api_provider
        self.list = []

    def toggle_prompt(self):
        self.toggle = input(f"\nWould you like to generate a {self.name} JSON file? \nYes: Any No: n ") != "n"

    def print_shopping_list(self):
        print(f"Current {self.name} shopping list:")
        for item in self.list:
            print(f"\n-{item}")

    def shopping_list(self):
        print(f"This category uses {self.api_provider}. Please browse there for your selections.")
        while True:
            self.print_shopping_list()
            response = input("\nPlease insert item ID to add, BACK to remove last option or DONE to finish: ")

            if response == "BACK":
                if self.list:
                    self.list.pop()
                continue
            if response == "DONE":
                break

            self.list.append(response)






