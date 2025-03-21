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
