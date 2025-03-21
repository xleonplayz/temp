#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
Dateiname    : visualisierungen.py
Beschreibung : Dieses Skript zeigt verschiedene Diagrammtypen anhand von 
               Eingabedaten. Alle Funktionen sind im Oxygen-Stil dokumentiert.
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
def plot_line_chart(x, y, title="Linienchart"):
    """
    ===============================================================================
    Funktion     : plot_line_chart
    Beschreibung : Erzeugt ein Linien-Diagramm anhand der übergebenen x- und y-Daten.
    Parameter    :
                   - x: Liste oder Array von Werten für die x-Achse.
                   - y: Liste oder Array von Werten für die y-Achse.
                   - title: Titel des Diagramms (Standard: 'Linienchart').
    Rückgabe   : Keine, es wird ein Diagramm angezeigt.
    ===============================================================================
    """
    plt.figure()
    plt.plot(x, y, marker='o', linestyle='-', linewidth=2)
    plt.title(title)
    plt.xlabel("X-Achse")
    plt.ylabel("Y-Achse")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------------------------
def plot_bar_chart(categories, values, title="Balkendiagramm"):
    """
    ===============================================================================
    Funktion     : plot_bar_chart
    Beschreibung : Erstellt ein Balkendiagramm basierend auf Kategorien und zugehörigen Werten.
    Parameter    :
                   - categories: Liste von Kategorien (x-Achse).
                   - values: Liste von Werten (Höhe der Balken).
                   - title: Titel des Diagramms (Standard: 'Balkendiagramm').
    Rückgabe   : Keine, es wird ein Diagramm angezeigt.
    ===============================================================================
    """
    plt.figure()
    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel("Kategorien")
    plt.ylabel("Werte")
    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------------------------
def plot_scatter_chart(x, y, title="Streudiagramm"):
    """
    ===============================================================================
    Funktion     : plot_scatter_chart
    Beschreibung : Erzeugt ein Streudiagramm anhand der übergebenen x- und y-Daten.
    Parameter    :
                   - x: Liste oder Array von Werten für die x-Achse.
                   - y: Liste oder Array von Werten für die y-Achse.
                   - title: Titel des Diagramms (Standard: 'Streudiagramm').
    Rückgabe   : Keine, es wird ein Diagramm angezeigt.
    ===============================================================================
    """
    plt.figure()
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel("X-Achse")
    plt.ylabel("Y-Achse")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------------------------
def plot_histogram(data, bins=10, title="Histogramm"):
    """
    ===============================================================================
    Funktion     : plot_histogram
    Beschreibung : Erstellt ein Histogramm aus den übergebenen Daten.
    Parameter    :
                   - data: Liste oder Array von Werten.
                   - bins: Anzahl der Balken (Standard: 10).
                   - title: Titel des Diagramms (Standard: 'Histogramm').
    Rückgabe   : Keine, es wird ein Diagramm angezeigt.
    ===============================================================================
    """
    plt.figure()
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel("Werte")
    plt.ylabel("Häufigkeit")
    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------------------------
def plot_pie_chart(labels, sizes, title="Kreisdiagramm"):
    """
    ===============================================================================
    Funktion     : plot_pie_chart
    Beschreibung : Erzeugt ein Kreisdiagramm anhand der übergebenen Labels und Größen.
    Parameter    :
                   - labels: Liste von Beschriftungen für die Segmente.
                   - sizes: Liste von Größenanteilen für die Segmente.
                   - title: Titel des Diagramms (Standard: 'Kreisdiagramm').
    Rückgabe   : Keine, es wird ein Diagramm angezeigt.
    ===============================================================================
    """
    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Kreisdiagramm rund darstellen
    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------------------------
def main():
    """
    ===============================================================================
    Funktion     : main
    Beschreibung : Beispielhafte Verwendung der Diagrammfunktionen mit Beispiel-Daten.
    Parameter    : Keine.
    Rückgabe   : Keine.
    ===============================================================================
    """
    # Beispiel 1: Linienchart
    x_values = np.linspace(0, 10, 50)
    y_values = np.sin(x_values)
    plot_line_chart(x_values, y_values, title="Sinus-Funktion")

    # Beispiel 2: Balkendiagramm
    categories = ['A', 'B', 'C', 'D']
    values = [23, 17, 35, 29]
    plot_bar_chart(categories, values, title="Kategorienwerte")

    # Beispiel 3: Streudiagramm
    np.random.seed(0)  # Für Reproduzierbarkeit
    x_rand = np.random.rand(50)
    y_rand = np.random.rand(50)
    plot_scatter_chart(x_rand, y_rand, title="Zufällige Streuung")

    # Beispiel 4: Histogramm
    data = np.random.randn(1000)  # Normalverteilte Daten
    plot_histogram(data, bins=20, title="Normalverteilte Werte")

    # Beispiel 5: Kreisdiagramm
    labels = ['Kategorie 1', 'Kategorie 2', 'Kategorie 3', 'Kategorie 4']
    sizes = [15, 30, 45, 10]
    plot_pie_chart(labels, sizes, title="Verteilung der Kategorien")

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
