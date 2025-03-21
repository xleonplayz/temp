#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file visualisierungen_mit_klasse_doxygen.py
@brief Dieses Skript zeigt verschiedene Diagrammtypen anhand von Eingabedaten,
       die in einer Klasse gekapselt werden. Die Klasse DataVisualizer beinhaltet
       Methoden für Linien-, Balken-, Streu-, Histogramm- und Kreisdiagramme.
"""

import matplotlib.pyplot as plt
import numpy as np

## @class DataVisualizer
#  @brief Eine Klasse zur Darstellung verschiedener Diagramme.
#
#  Diese Klasse kapselt Methoden zur Visualisierung von Diagrammen. Mit Hilfe
#  dieser Klasse können Linien-, Balken-, Streu-, Histogramm- und Kreisdiagramme
#  erstellt werden.
class DataVisualizer:
    ## @brief Konstruktor der Klasse DataVisualizer.
    #  @return None
    def __init__(self):
        pass

    ## @brief Erstellt ein Liniendiagramm.
    #  @param x Liste oder Array von Werten für die x-Achse.
    #  @param y Liste oder Array von Werten für die y-Achse.
    #  @param title Titel des Diagramms (Standard: "Linienchart").
    #  @return None
    def plot_line_chart(self, x, y, title="Linienchart"):
        plt.figure()
        plt.plot(x, y, marker='o', linestyle='-', linewidth=2)
        plt.title(title)
        plt.xlabel("X-Achse")
        plt.ylabel("Y-Achse")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    ## @brief Erstellt ein Balkendiagramm.
    #  @param categories Liste von Kategorien (x-Achse).
    #  @param values Liste von Werten, die die Höhe der Balken darstellen.
    #  @param title Titel des Diagramms (Standard: "Balkendiagramm").
    #  @return None
    def plot_bar_chart(self, categories, values, title="Balkendiagramm"):
        plt.figure()
        plt.bar(categories, values)
        plt.title(title)
        plt.xlabel("Kategorien")
        plt.ylabel("Werte")
        plt.tight_layout()
        plt.show()

    ## @brief Erstellt ein Streudiagramm.
    #  @param x Liste oder Array von Werten für die x-Achse.
    #  @param y Liste oder Array von Werten für die y-Achse.
    #  @param title Titel des Diagramms (Standard: "Streudiagramm").
    #  @return None
    def plot_scatter_chart(self, x, y, title="Streudiagramm"):
        plt.figure()
        plt.scatter(x, y)
        plt.title(title)
        plt.xlabel("X-Achse")
        plt.ylabel("Y-Achse")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    ## @brief Erstellt ein Histogramm.
    #  @param data Liste oder Array von Werten.
    #  @param bins Anzahl der Balken im Histogramm (Standard: 10).
    #  @param title Titel des Diagramms (Standard: "Histogramm").
    #  @return None
    def plot_histogram(self, data, bins=10, title="Histogramm"):
        plt.figure()
        plt.hist(data, bins=bins, edgecolor='black')
        plt.title(title)
        plt.xlabel("Werte")
        plt.ylabel("Häufigkeit")
        plt.tight_layout()
        plt.show()

    ## @brief Erstellt ein Kreisdiagramm.
    #  @param labels Liste von Beschriftungen für die Segmente.
    #  @param sizes Liste von Größenanteilen für die Segmente.
    #  @param title Titel des Diagramms (Standard: "Kreisdiagramm").
    #  @return None
    def plot_pie_chart(self, labels, sizes, title="Kreisdiagramm"):
        plt.figure()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.axis('equal')  # Kreisdiagramm rund darstellen
        plt.tight_layout()
        plt.show()

## @brief Hauptfunktion zur Demonstration der DataVisualizer-Klasse.
#  @return None
def main():
    # Instanziiere die DataVisualizer-Klasse
    visualizer = DataVisualizer()

    # Beispiel 1: Linienchart
    x_values = np.linspace(0, 10, 50)
    y_values = np.sin(x_values)
    visualizer.plot_line_chart(x_values, y_values, title="Sinus-Funktion")

    # Beispiel 2: Balkendiagramm
    categories = ['A', 'B', 'C', 'D']
    values = [23, 17, 35, 29]
    visualizer.plot_bar_chart(categories, values, title="Kategorienwerte")

    # Beispiel 3: Streudiagramm
    np.random.seed(0)  # Für Reproduzierbarkeit
    x_rand = np.random.rand(50)
    y_rand = np.random.rand(50)
    visualizer.plot_scatter_chart(x_rand, y_rand, title="Zufällige Streuung")

    # Beispiel 4: Histogramm
    data = np.random.randn(1000)  # Normalverteilte Daten
    visualizer.plot_histogram(data, bins=20, title="Normalverteilte Werte")

    # Beispiel 5: Kreisdiagramm
    labels = ['Kategorie 1', 'Kategorie 2', 'Kategorie 3', 'Kategorie 4']
    sizes = [15, 30, 45, 10]
    visualizer.plot_pie_chart(labels, sizes, title="Verteilung der Kategorien")

if __name__ == "__main__":
    main()
