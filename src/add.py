class NumberCombiner:
    """
    @class NumberCombiner
    @brief A class that provides various methods to combine numbers using arithmetic operations.
    
    @details This class supports several arithmetic operations such as addition, subtraction,
             multiplication, division, exponentiation, and modulus. It also holds instance attributes 
             that must be provided during object construction.
    
    @var version
        The current version of the NumberCombiner instance.
    @var supported_operations
        A list of all arithmetic operations supported by this instance.
    @var default_value
        A default numerical value used as a fallback.
    """

    def __init__(self, version: str, supported_operations: list, default_value: float):
        """
        @brief Constructor for NumberCombiner.
        
        @param version The version string of this NumberCombiner instance.
        @param supported_operations A list of operations supported by this instance.
        @param default_value The default value used as a fallback.
        """
        self.version = version
        self.supported_operations = supported_operations
        self.default_value = default_value

    def add(self, a: float, b: float) -> float:
        """
        @brief Adds two numbers together.
        
        @param a The first number.
        @param b The second number.
        
        @return The sum of the two numbers.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        @brief Subtracts the second number from the first.
        
        @param a The first number.
        @param b The second number.
        
        @return The difference between the two numbers.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        @brief Multiplies two numbers together.
        
        @param a The first number.
        @param b The second number.
        
        @return The product of the two numbers.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        @brief Divides the first number by the second.
        
        @param a The numerator.
        @param b The denominator (must not be zero).
        
        @return The quotient of the division.
        @throws ValueError If b is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def power(self, a: float, b: float) -> float:
        """
        @brief Raises the first number to the power of the second.
        
        @param a The base number.
        @param b The exponent.
        
        @return The result of raising a to the power of b.
        """
        return a ** b

    def modulus(self, a: float, b: float) -> float:
        """
        @brief Returns the remainder of the division of the first number by the second.
        
        @param a The dividend.
        @param b The divisor (must not be zero).
        
        @return The remainder of the division.
        @throws ValueError If b is zero.
        """
        if b == 0:
            raise ValueError("Modulus by zero is not allowed.")
        return a % b

    def combine_all(self, a: float, b: float) -> dict:
        """
        @brief Performs all arithmetic operations on the given numbers and returns a dictionary with results.
        
        @param a The first number.
        @param b The second number.
        
        @return A dictionary containing the results of all operations:
                - "addition": Result of addition.
                - "subtraction": Result of subtraction.
                - "multiplication": Result of multiplication.
                - "division": Result of division (or "undefined" if division by zero).
                - "power": Result of exponentiation.
                - "modulus": Result of modulus (or "undefined" if modulus by zero).
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
    # Required instance attributes must be passed during object creation.
    version = "1.0"
