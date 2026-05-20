# Financial Simulator Suite

A clean Python command-line project that simulates three common financial analysis scenarios:

- ROI of an investment
- Real estate rental profitability
- Startup valuation using a revenue multiple

This project is designed for a GitHub portfolio and can be used to demonstrate financial reasoning, basic Python programming and structured modelling logic.

## Project Structure

```text
financial-simulator/
|-- main.py
|-- roi_calculator.py
|-- real_estate.py
|-- startup_valuation.py
|-- requirements.txt
|-- visualization.html
|-- docs/
|   `-- example_results.md
`-- tests/
    `-- test_financial_simulator.py
```

## Features

### ROI Calculator

Calculates profit and return on investment.

Formula:

```text
ROI = ((Final Value - Initial Investment) / Initial Investment) * 100
```

### Real Estate Investment

Calculates net yearly income and net rental yield.

Formula:

```text
Net Income = Annual Rent - Annual Costs
Rental Yield = (Net Income / Property Price) * 100
```

### Startup Valuation

Estimates valuation with a simple revenue multiple approach.

Formula:

```text
Adjusted Multiple = Base Multiple + (Growth Rate * 10)
Valuation = Annual Revenue * Adjusted Multiple
```

## How to Run

From the project folder:

```bash
python main.py
```

Then choose one of the menu options:

```text
1 - ROI Calculator
2 - Real Estate Investment
3 - Startup Valuation
4 - Exit
```

## How to Run Tests

From the project folder:

```bash
python -m unittest discover tests
```

The test suite validates the main formulas and input checks.

## Visual Preview

Open `visualization.html` in a browser to interact with a simple visual version of the three simulators.

No installation is required.

## Example Use Cases

- Evaluate whether an investment generated a positive return
- Analyze the profitability of a rental property
- Estimate the value of a startup based on revenue and growth

## CV Line

**GitHub Project - Financial Simulator Suite**  
Developed a Python-based financial modelling tool to simulate ROI, real estate profitability and startup valuation, with automated tests and portfolio-ready documentation.

## Possible Improvements

- Add charts with Matplotlib
- Export scenario results to CSV
- Add an Excel version
- Build a Streamlit web app
