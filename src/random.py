#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file random_number_generator.py
@brief This module provides a class for generating random numbers in different formats.
"""

import random

## @class RandomNumberGenerator
#  @brief A class that generates random numbers in different formats.
class RandomNumberGenerator:
    ## @brief Generates a random integer within a specified range.
    #  @param {int} min_value - The minimum value (inclusive).
    #  @param {int} max_value - The maximum value (inclusive).
    #  @return {int} - A randomly chosen integer within the specified range.
    def get_random_integer(self, min_value: int, max_value: int) -> int:
        return random.randint(min_value, max_value)
    
    ## @brief Generates a random floating-point number within a specified range.
    #  @param {float} min_value - The minimum value (inclusive).
    #  @param {float} max_value - The maximum value (inclusive).
    #  @return {float} - A randomly chosen floating-point number within the specified range.
    def get_random_float(self, min_value: float, max_value: float) -> float:
        return random.uniform(min_value, max_value)
    
    ## @brief Generates multiple random integers within a specified range and returns them as a space-separated string.
    #  @param {int} count - The number of random integers to generate.
    #  @param {int} min_value - The minimum value (inclusive).
    #  @param {int} max_value - The maximum value (inclusive).
    #  @return {str} - A string containing the requested number of random integers.
    #  @throws {ValueError} - If count is less than or equal to zero.
    def get_multiple_random_numbers(self, count: int, min_value: int, max_value: int) -> str:
        if count <= 0:
            raise ValueError("Count must be greater than zero.")
        return " ".join(str(random.randint(min_value, max_value)) for _ in range(count))

## @brief Example usage of the RandomNumberGenerator class.
if __name__ == "__main__":
    generator = RandomNumberGenerator()
    print(generator.get_random_integer(1, 100))    # Prints a random integer between 1 and 100
    print(generator.get_random_float(1.0, 10.0))     # Prints a random float between 1.0 and 10.0
    print(generator.get_multiple_random_numbers(5, 1, 50))  # Prints five random integers between 1 and 50
