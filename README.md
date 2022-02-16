# CalCalc-GO
CalCalc repo for HW3 in AstroPythonData Course, Spring 2022

A simple module to evaluate string input of mathematical expression, or answer simple questions using the [Wolfram Alpha API](https://products.wolframalpha.com/short-answers-api/documentation/)

Simple test commands:
1. Numerical input: `CalCalc.main("2*2")`
2. Wolfram input: `Distance from Berkeley, CA to Albuquerque, NM`

## Setup instructions
Instruction clone repo and install the `CalCalc` module into the `PYTHONPATH`
```bash
git clone https://github.com/gregottino/CalCalc-GO.git
cd CalCalc-GO
python -m pip install --upgrade pip
python -m pip install -e .
```
