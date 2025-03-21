#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file combined_module.py
@brief This module provides two classes:
       1) RandomNumberGenerator for generating random numbers
       2) NumberCombiner for performing arithmetic operations
"""

import random

class RandomNumberGenerator:
    """
    @class RandomNumberGenerator
    @brief A class for generating random numbers in various formats.
    """
    
    def get_random_integer(self, min_value: int, max_value: int) -> int:
        """
        @brief Generates a random integer within a specified range.

        @param {int} min_value - The minimum value (inclusive).
        @param {int} max_value - The maximum value (inclusive).

        @return {int} - A randomly chosen integer within the specified range.
        """
        return random.randint(min_value, max_value)
    
    def get_random_float(self, min_value: float, max_value: float) -> float:
        """
        @brief Generates a random floating-point number within a specified range.

        @param {float} min_value - The minimum value (inclusive).
        @param {float} max_value - The maximum value (inclusive).

        @return {float} - A randomly chosen floating-point number within the specified range.
        """
        return random.uniform(min_value, max_value)
    
    def get_multiple_random_numbers(self, count: int, min_value: int, max_value: int) -> str:
        """
        @brief Generates multiple random integers within a specified range
               and returns them as a space-separated string.

        @param {int} count - The number of random integers to generate.
        @param {int} min_value - The minimum value (inclusive).
        @param {int} max_value - The maximum value (inclusive).

        @return {str} - A string containing the requested number of random integers.
        @throws ValueError - If count <= 0.
        """
        if count <= 0:
            raise ValueError("Count must be greater than zero.")
        return " ".join(str(random.randint(min_value, max_value)) for _ in range(count))

# Example usage:
if __name__ == "__main__":
    generator = RandomNumberGenerator()
    print(generator.get_random_integer(1, 100))              # Random integer between 1 and 100
    print(generator.get_random_float(1.0, 10.0))            # Random float between 1.0 and 10.0
    print(generator.get_multiple_random_numbers(5, 1, 50))  # Five random integers between 1 and 50


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

        @return {float} - The difference (a - b).
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

        @return {float} - The remainder (a % b).
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
