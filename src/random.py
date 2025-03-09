import random

class RandomNumberGenerator:
    """
    A class that generates random numbers in different formats.
    """
    
    def get_random_integer(self, min_value: int, max_value: int) -> int:
        """
        Generates a random integer within a specified range.
        
        Parameters:
        min_value (int): The minimum value (inclusive).
        max_value (int): The maximum value (inclusive).
        
        Returns:
        int: A randomly chosen integer within the specified range.
        """
        return random.randint(min_value, max_value)
    
    def get_random_float(self, min_value: float, max_value: float) -> float:
        """
        Generates a random floating-point number within a specified range.
        
        Parameters:
        min_value (float): The minimum value (inclusive).
        max_value (float): The maximum value (inclusive).
        
        Returns:
        float: A randomly chosen floating-point number within the specified range.
        """
        return random.uniform(min_value, max_value)
    
    def get_multiple_random_numbers(self, count: int, min_value: int, max_value: int) -> str:
        """
        Generates multiple random integers within a specified range and returns them as a space-separated string.
        
        Parameters:
        count (int): The number of random integers to generate.
        min_value (int): The minimum value (inclusive).
        max_value (int): The maximum value (inclusive).
        
        Returns:
        str: A string containing the requested number of random integers.
        """
        if count <= 0:
            raise ValueError("Count must be greater than zero.")
        return " ".join(str(random.randint(min_value, max_value)) for _ in range(count))

# Example usage:
if __name__ == "__main__":
    generator = RandomNumberGenerator()
    print(generator.get_random_integer(1, 100))  # Prints a random integer between 1 and 100
    print(generator.get_random_float(1.0, 10.0))  # Prints a random float between 1.0 and 10.0
    print(generator.get_multiple_random_numbers(5, 1, 50))  # Prints five random integers between 1 and 50