class Category():
    def __init__(self, name, api_provider, toggle = False):
        self.name = name
        self.toggle = toggle
        self.api_provider = api_provider
        self.list = []

    def toggle_prompt(self):
        self.toggle = input(
            f"\nWould you like to generate a {self.name} JSON file?\n"
            "Yes: any | No: n\n> "
        ) != "n"

    def print_shopping_list(self):
        print(f"\nCurrent {self.name} shopping list:")
        for item in self.list:
            print(f"- {item}")

    def shopping_list(self):
        print(
            f"\nThis category uses {self.api_provider}. "
            "Please browse there for your selections."
        )
        while True:
            self.print_shopping_list()
            response = input(
                "\nEnter an item ID to add it. To bulk import seperate id by comma ','\n"
                "Enter BACK to remove the last item or DONE to finish.\n> "
            )

            if response == "BACK":
                if self.list:
                    self.list.pop()
                continue
            
            elif response == "DONE":
                if self.list == []:
                    print("\nCan't proceed with an empty list.")
                    continue
                else:
                    break

            elif "," in response:
                responses = response.split(",")
                responses = [item.strip() for item in responses]
                self.list.extend(responses)
                continue

            elif response == "":
                print("\nPlease enter something.")
                continue

            self.list.append(response)





