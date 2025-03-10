class NumberCombiner:
    """
    @class NumberCombiner
    @brief A class that provides various methods to combine numbers using arithmetic operations.
    """
    
    def add(self, a: float, b: float) -> float:
        """
        @brief Adds two numbers together.
        
        @param {float} a - The first number.
        @param {float} b - The second number.
        
        @return {float} - The sum of the two numbers.
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """
        @brief Subtracts the second number from the first.
        
        @param {float} a - The first number.
        @param {float} b - The second number.
        
        @return {float} - The difference between the two numbers.
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """
        @brief Multiplies two numbers together.
        
        @param {float} a - The first number.
        @param {float} b - The second number.
        
        @return {float} - The product of the two numbers.
        """
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        @brief Divides the first number by the second.
        
        @param {float} a - The numerator.
        @param {float} b - The denominator (must not be zero).
        
        @return {float} - The quotient of the division.
        @throws ValueError - If b is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    
    def power(self, a: float, b: float) -> float:
        """
        @brief Raises the first number to the power of the second.
        
        @param {float} a - The base number.
        @param {float} b - The exponent.
        
        @return {float} - The result of raising 'a' to the power of 'b'.
        """
        return a ** b
    
    def modulus(self, a: float, b: float) -> float:
        """
        @brief Returns the remainder of the division of the first number by the second.
        
        @param {float} a - The dividend.
        @param {float} b - The divisor (must not be zero).
        
        @return {float} - The remainder of the division.
        @throws ValueError - If b is zero.
        """
        if b == 0:
            raise ValueError("Modulus by zero is not allowed.")
        return a % b
    
    def combine_all(self, a: float, b: float) -> dict:
        """
        @brief Performs all arithmetic operations on the given numbers and returns a dictionary with results.
        
        @param {float} a - The first number.
        @param {float} b - The second number.
        
        @return {dict} - A dictionary containing the results of all operations:
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
    combiner = NumberCombiner()
    num1, num2 = 10, 3
    print(combiner.combine_all(num1, num2))
