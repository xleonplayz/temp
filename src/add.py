class NumberCombiner:
    """
    A class that provides various methods to combine numbers using arithmetic operations.
    """
    
    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers together.
        
        Parameters:
        a (float): The first number.
        b (float): The second number.
        
        Returns:
        float: The sum of the two numbers.
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """
        Subtracts the second number from the first.
        
        Parameters:
        a (float): The first number.
        b (float): The second number.
        
        Returns:
        float: The difference between the two numbers.
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """
        Multiplies two numbers together.
        
        Parameters:
        a (float): The first number.
        b (float): The second number.
        
        Returns:
        float: The product of the two numbers.
        """
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Divides the first number by the second number.
        
        Parameters:
        a (float): The numerator.
        b (float): The denominator (must not be zero).
        
        Returns:
        float: The quotient of the division.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    
    def power(self, a: float, b: float) -> float:
        """
        Raises the first number to the power of the second number.
        
        Parameters:
        a (float): The base number.
        b (float): The exponent.
        
        Returns:
        float: The result of raising 'a' to the power of 'b'.
        """
        return a ** b
    
    def modulus(self, a: float, b: float) -> float:
        """
        Returns the remainder of the division of the first number by the second number.
        
        Parameters:
        a (float): The dividend.
        b (float): The divisor (must not be zero).
        
        Returns:
        float: The remainder of the division.
        """
        if b == 0:
            raise ValueError("Modulus by zero is not allowed.")
        return a % b
    
    def combine_all(self, a: float, b: float) -> dict:
        """
        Performs all operations (addition, subtraction, multiplication, division, power, modulus) 
        on the given numbers and returns a dictionary with results.
        
        Parameters:
        a (float): The first number.
        b (float): The second number.
        
        Returns:
        dict: A dictionary containing the results of all operations.
        """
        results = {
            "addition": self.add(a, b),
            "subtraction": self.subtract(a, b),
            "multiplication": self.multiply(a, b),
            "division": self.divide(a, b) if b != 0 else "undefined",
            "power": self.power(a, b),
            "modulus": self.modulus(a, b) if b != 0 else "undefined"
        }
        return results

# Example usage:
if __name__ == "__main__":
    combiner = NumberCombiner()
    num1, num2 = 10, 3
    print(combiner.combine_all(num1, num2))
