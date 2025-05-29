# currency_converter
# Currency Converter

This is a simple currency converter application built using Python and the `tkinter` library for the graphical user interface.  It allows users to convert amounts between different currencies.

## Features

* **Currency Conversion:** Converts amounts between various currencies.
* **User-Friendly Interface:** Provides a graphical interface for easy interaction.
* **Dynamic Exchange Rates:** Calculates exchange rates based on predefined USD-based rates.
* **Error Handling:** Handles invalid input (e.g., negative amounts, non-numeric input).
* **Real-time Conversion:** Updates the converted amount as the input amount or selected currencies change.
* **Wide Currency Support:** Supports a range of global currencies.

## Requirements

* Python 3.x
* tkinter (usually included with Python)

## Installation

1.  Clone the repository:

    ```bash
    git clone <https://github.com/SUPRIYA410/currency_converter-project-for-Micro-IT/tree/main>
    cd <currency_converter-project-for-Micro-IT>
    ```

2.  (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  No additional packages need to be installed beyond the Python standard library.

## Usage

1.  Run the script:

    ```bash
    python Currency_Converter.py
    ```

2.  Enter the amount you want to convert in the "Amount" field.
3.  Select the base currency from the "From Currency" dropdown menu.
4.  Select the target currency from the "To Currency" dropdown menu.
5.  The converted amount will be displayed automatically.

## Code Description

* `Currency_Converter.py`: The main Python script containing the currency converter application logic.

    * `usd_rates`: A dictionary containing exchange rates relative to the US dollar (USD).  This serves as the base for calculating other exchange rates.
    * `get_exchange_rate(base_currency, target_currency)`:  A function that calculates the exchange rate between any two currencies by using the USD as an intermediary.  It retrieves the rates from the `usd_rates` dictionary.
    * `convert_currency(event=None)`:  A function that performs the currency conversion.  It gets the input amount and selected currencies from the GUI, validates the input, calculates the converted amount using `get_exchange_rate()`, and updates the GUI with the results.
    * GUI Construction: The script uses `tkinter` to create the main window, frames, labels, entry fields, and dropdown menus (comboboxes).  It also defines the layout and styling of these elements.  Event bindings are used to trigger the `convert_currency` function when the user interacts with the GUI (e.g., typing in the amount or changing the selected currencies).

##  Important Notes

* **Exchange Rate Accuracy:** The exchange rates in the `usd_rates` dictionary are static and included directly in the code.  For a real-world application, you would typically fetch exchange rates from a live API to ensure accuracy.  This example is for demonstration purposes.
* **Error Handling:** The application includes basic error handling to ensure the input amount is a valid positive number.

## Credits

* Developed by \[Jaladurgam supriya/SUPRIYA410]

