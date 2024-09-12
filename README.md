## Requirements

+ [Python 3.7+](https://www.python.org/)
+ [python3-venv](https://docs.python.org/3/library/venv.html)
+ requirements.txt

## Installation or Getting Started

Getting started:

sudo apt install python3-venv	
cd test_electronic_device_calculator.py
python3 -m venv /cal_python/venv
source venv/bin/activate
pip install -r requirements.txt

## Testing

# run tests normally
pytest -vv  test_electronic_device_calculator.py 
	
# perform tests with line (node) coverage report
pytest -vv  test_electronic_device_calculator.py  --cov=cal

# perform tests with branch coverage report
pytest -vv  test_electronic_device_calculator.py  --cov=cal  --cov-branch  --cov-report html

# run tests with mutmut
mutmut run --paths-to-mutate=/home/jrosa/Documentos/UFS/Teste_Software/Teste_Software_Mutantes_2024_Conceicao_Joao/test/test_electronic_device_calculator.py



# Calculator
Simple Calculator class with 100% coverage by pytest


<div align="center">
  <h1 align="center">Calculator</h1>
</div>


## About

Simple Calculator class with allow user use basic math and read file. The bigger focus in this project was on test and by using pytest prject reach 100% coverage. In the project was also used Mock and Fixtures.

## Table of Contents
* [Getting started](#getting-started)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Project Status](#project-status)
* [Screenshots](#screenshots)


## GETTING STARTED

1. Checking Python version.
    - To be able to use this script you'll need to have Python installed, you can check whether you have it installed or not by typing in terminal:  
`python3 --version`  
or:  
`python --version` 
    - This script was written using version 3.9.0 and it is advised to use the same version.
    - If you don't have Python installed you can go to [Python.org](https://www.python.org/downloads/) to download it.
    
 2. Creating Virtual Environment 
    - To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:  
    `python3 -m venv your-env`  
    - Once you’ve created a virtual environment, you may activate it.  
    `source your-env/bin/activate`
    
 3. Download
     - You need to clone repository to your local destination  
    `cd path/to/your/workspace`  
    `https://github.com/robert-adamczyk/Calculator.git`
    
 4. Requirements
    - Once your virtual environment is activated and project is cloned you need to install requirements:  
    `pip install -r requirements.txt` 
    
## Features
   List the features here:
   - check battery: show how much bettery left
   - charge battery
   - count average numbers in the file
   - math action on numbers: add, substract, multiply, divide, quare, is even, n to power off
   
  
## Technologies Used:
  - pytest==7.2.0
  - pytest-cov==4.0.0
  - coverage==6.5.0

## Screenshots:

### Coverage report
<a href="https://ibb.co/r7FJPFH"><img src="https://i.ibb.co/tmQ5fQD/coverage-report.png" alt="coverage-report" border="0"></a>
### Calculator ceverage detail report
<a href="https://ibb.co/RzG6rP4"><img src="https://i.ibb.co/J5Wp62F/coverage-detailpng.png" alt="coverage-detailpng" border="0"></a>

## Project Status:
  
Project is: _done_

  
## License

MIT License.
