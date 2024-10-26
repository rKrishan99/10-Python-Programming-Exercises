import json

class Recipe:
    def __init__(self, name, ingredients, instructions):
        """Initialize a recipe with a name, ingredients, and instructions."""
        self.name = name
        self.ingredients = ingredients  # List of ingredients
        self.instructions = instructions  # Cooking instructions

    def to_dict(self):
        """Convert the Recipe object to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }

class RecipeBook:
    def __init__(self, filename='recipes.json'):
        """Initialize the RecipeBook with a filename and load existing recipes."""
        self.filename = filename
        self.recipes = self.load_recipes()

    def load_recipes(self):
        """Load recipes from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                recipes_data = json.load(file)
                return [Recipe(**recipe) for recipe in recipes_data]  # Convert dict to Recipe objects
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return an empty list if file not found or empty

    def save_recipes(self):
        """Save the current recipes to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([recipe.to_dict() for recipe in self.recipes], file, indent=4)

    def add_recipe(self):
        """Add a new recipe to the recipe book."""
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma separated): ").split(',')
        instructions = input("Enter cooking instructions: ")
        recipe = Recipe(name, [ingredient.strip() for ingredient in ingredients], instructions)
        self.recipes.append(recipe)  # Add recipe to the list
        self.save_recipes()  # Save recipes to file
        print(f"Recipe '{name}' added successfully!")

    def remove_recipe(self):
        """Remove a recipe from the recipe book by name."""
        name = input("Enter the name of the recipe to remove: ")
        # Use case insensitive matching to find and remove the recipe
        original_count = len(self.recipes)  # Count before removal
        self.recipes = [recipe for recipe in self.recipes if recipe.name.lower() != name.lower()]  # Remove recipe
        if len(self.recipes) < original_count:  # Check if a recipe was removed
            self.save_recipes()  # Save changes to file
            print(f"Recipe '{name}' removed successfully!")
        else:
            print(f"No recipe found with the name '{name}'.")

    def search_recipe(self):
        """Search for a recipe by name."""
        name = input("Enter the name of the recipe to search for: ")
        found_recipes = [recipe for recipe in self.recipes if recipe.name.lower() == name.lower()]
        if found_recipes:
            for recipe in found_recipes:
                print(f"\nRecipe: {recipe.name}\nIngredients: {', '.join(recipe.ingredients)}\nInstructions: {recipe.instructions}")
        else:
            print(f"No recipe found with the name '{name}'.")

    def display_recipes(self):
        """Display all recipes in the recipe book."""
        if not self.recipes:
            print("No recipes found.")
            return
        for recipe in self.recipes:
            print(f"\nRecipe: {recipe.name}\nIngredients: {', '.join(recipe.ingredients)}\nInstructions: {recipe.instructions}")

def recipe_book_system():
    """Manage a recipe book through a command-line interface."""
    recipe_book = RecipeBook()  # Create a RecipeBook instance

    while True:
        print("\nOptions:")
        print("1. Add a recipe")
        print("2. Remove a recipe")
        print("3. Search for a recipe")
        print("4. Display all recipes")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            recipe_book.add_recipe()  # Add a recipe

        elif choice == '2':
            recipe_book.remove_recipe()  # Remove a recipe

        elif choice == '3':
            recipe_book.search_recipe()  # Search for a recipe

        elif choice == '4':
            recipe_book.display_recipes()  # Display all recipes

        elif choice == '5':
            print("Exiting the recipe book system.")
            break

        else:
            print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    recipe_book_system()
