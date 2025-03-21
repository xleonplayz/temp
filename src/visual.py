#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file combined_module_with_visualizer.py
@brief This module provides three classes:
       1) RandomNumberGenerator for generating random numbers
       2) NumberCombiner for performing arithmetic operations
       3) DataVisualizer for visualizing data in various plot types
"""

import random
import matplotlib.pyplot as plt

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


class DataVisualizer:
    """
    @class DataVisualizer
    @brief A class that offers multiple methods to visualize data with different plot types.
    """

    def plot_line(self, x_values: list, y_values: list, title: str = "Line Plot") -> None:
        """
        @brief Creates a line plot from x and y data.

        @param {list} x_values - The list of x-coordinates.
        @param {list} y_values - The list of y-coordinates.
        @param {str} title     - The title of the plot (optional).

        @return {None} - Displays the line plot.
        """
        plt.figure()
        plt.plot(x_values, y_values)
        plt.title(title)
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.show()

    def plot_scatter(self, x_values: list, y_values: list, title: str = "Scatter Plot") -> None:
        """
        @brief Creates a scatter plot from x and y data.

        @param {list} x_values - The list of x-coordinates.
        @param {list} y_values - The list of y-coordinates.
        @param {str} title     - The title of the plot (optional).

        @return {None} - Displays the scatter plot.
        """
        plt.figure()
        plt.scatter(x_values, y_values)
        plt.title(title)
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.show()

    def plot_bar(self, categories: list, values: list, title: str = "Bar Plot") -> None:
        """
        @brief Creates a bar plot from category labels and their corresponding values.

        @param {list} categories - The list of category labels.
        @param {list} values     - The list of values corresponding to each category.
        @param {str} title       - The title of the plot (optional).

        @return {None} - Displays the bar plot.
        """
        plt.figure()
        plt.bar(categories, values)
        plt.title(title)
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.show()

    def plot_histogram(self, data: list, bins: int = 10, title: str = "Histogram") -> None:
        """
        @brief Creates a histogram from a list of numerical data.

        @param {list} data - The list of numerical values.
        @param {int} bins  - Number of bins (optional).
        @param {str} title - The title of the plot (optional).

        @return {None} - Displays the histogram.
        """
        plt.figure()
        plt.hist(data, bins=bins)
        plt.title(title)
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

    def plot_pie(self, labels: list, sizes: list, title: str = "Pie Chart") -> None:
        """
        @brief Creates a pie chart from labels and corresponding sizes.

        @param {list} labels - The list of labels (slices).
        @param {list} sizes  - The list of sizes (fractions) for each slice.
        @param {str} title   - The title of the plot (optional).

        @return {None} - Displays the pie chart.
        """
        plt.figure()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title(title)
        plt.show()

    def plot_box(self, data: list, title: str = "Box Plot") -> None:
        """
        @brief Creates a box plot from a list of numerical data.

        @param {list} data - The list of numerical values.
        @param {str} title - The title of the plot (optional).

        @return {None} - Displays the box plot.
        """
        plt.figure()
        plt.boxplot(data)
        plt.title(title)
        plt.ylabel("Values")
        plt.show()


# Example usage of all classes:
if __name__ == "__main__":
    # Random numbers
    rng = RandomNumberGenerator()
    print(rng.get_random_integer(1, 100))
    print(rng.get_random_float(1.0, 10.0))
    print(rng.get_multiple_random_numbers(5, 1, 50))

    # Arithmetic
    combiner = NumberCombiner()
    num1, num2 = 10, 3
    print(combiner.combine_all(num1, num2))

    # Visualization
    visualizer = DataVisualizer()
    x_vals = [1, 2, 3, 4, 5]
    y_vals = [2, 5, 3, 8, 7]
    visualizer.plot_line(x_vals, y_vals, "Line Plot Example")
    visualizer.plot_scatter(x_vals, y_vals, "Scatter Plot Example")
    visualizer.plot_bar(["A", "B", "C", "D", "E"], [3, 7, 1, 5, 9], "Bar Plot Example")
    visualizer.plot_histogram([random.gauss(0, 1) for _ in range(1000)], bins=20, title="Histogram Example")
    visualizer.plot_pie(["Cats", "Dogs", "Birds"], [45, 30, 25], "Pie Chart Example")
    visualizer.plot_box([random.gauss(0, 1) for _ in range(1000)], "Box Plot Example")
