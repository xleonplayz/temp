import random

class NameGenerator:
    """
    @class NameGenerator
    @brief A class that provides random names on request.
    """
    
    def __init__(self):
        """
        @brief Initializes the NameGenerator with a list of sample names.
        """
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isaac", "Jack"]
    
    def get_name(self) -> str:
        """
        @brief Returns a single random name from the list.
        
        @return {str} - A randomly chosen name.
        """
        return random.choice(self.names)
    
    def get_multiple_names(self, count: int) -> str:
        """
        @brief Returns a string containing multiple random names, separated by spaces.
        
        @param {int} count - The number of names to retrieve.
        
        @return {str} - A string containing the requested number of names.
        @throws ValueError - If count is less than or equal to zero.
        """
        if count <= 0:
            raise ValueError("Count must be greater than zero.")
        return " ".join(random.choices(self.names, k=count))

# Example usage:
if __name__ == "__main__":
    generator = NameGenerator()
    print(generator.get_name())  # Prints a single random name
    print(generator.get_multiple_names(3))  # Prints three random names
