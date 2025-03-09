import random

class NameGenerator:
    """
    A class that provides random names on request.
    """
    
    def __init__(self):
        """
        Initializes the NameGenerator with a list of sample names.
        """
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isaac", "Jack"]
    
    def get_name(self) -> str:
        """
        Returns a single random name from the list.
        
        Returns:
        str: A randomly chosen name.
        """
        return random.choice(self.names)
    
    def get_multiple_names(self, count: int) -> str:
        """
        Returns a string containing multiple random names, separated by spaces.
        
        Parameters:
        count (int): The number of names to retrieve.
        
        Returns:
        str: A string containing the requested number of names.
        """
        if count <= 0:
            raise ValueError("Count must be greater than zero.")
        return " ".join(random.choices(self.names, k=count))

# Example usage:
if __name__ == "__main__":
    generator = NameGenerator()
    print(generator.get_name())  # Prints a single random name
    print(generator.get_multiple_names(3))  # Prints three random names