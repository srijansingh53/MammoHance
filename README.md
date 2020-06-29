# Adaptive Mammographic Image Enhancement  

Pythonic Implementation of the [paper](https://ieeexplore.ieee.org/abstract/document/640739):

Jong Kook Kim, Jeong Mi Park, Koun Sik Song, Hyun Wook Park. ["Adaptive Mammographic Image Enhancement
Using First Derivative and Local Statistics"](https://ieeexplore.ieee.org/abstract/document/640739). IEEE Trans Med Imaging
. 1997 Oct;16(5):495-502. doi: 10.1109/42.640739..

## Content

- [Prerequisites](https://github.com/srijansingh53/IP_project#prerequisites)
- [Dataset](https://github.com/srijansingh53/IP_project#dataset)
- [Scripts](https://github.com/srijansingh53/IP_project#scripts)
    - [main.ipynb](https://github.com/srijansingh53/IP_project#mainipynb)
    - [steps.py](https://github.com/srijansingh53/IP_project#stepspy)
    - [main.py](https://github.com/srijansingh53/IP_project#mainpy)
    - [compare.py](https://github.com/srijansingh53/IP_project#comparepy)
- [Algorithm](https://github.com/srijansingh53/IP_project#algorithm)
    - [Flow Chart](https://github.com/srijansingh53/IP_project#flowchart)
    - [Pseudo Code](https://github.com/srijansingh53/IP_project#pseudocode)
- [Results](https://github.com/srijansingh53/IP_project#results)
    - [1st Step](https://github.com/srijansingh53/IP_project#first-step)
    - [2nd Step](https://github.com/srijansingh53/IP_project#second-step)
    - [3rd Step](https://github.com/srijansingh53/IP_project#third-step)
    - [Compared Results](https://github.com/srijansingh53/IP_project#compared-results)
- [Contribution](https://github.com/srijansingh53/IP_project#contribution)

## Installation
Clone and install the dependencies for the project.
```
git clone https://github.com/srijansingh53/IP_project.git
cd IP_project
pip install -r requirements.txt
```

## Dataset

The Dataset is taken from [MIAS (Mammographic Image Analysis Society) Mammography Mini-Dataset](http://peipa.essex.ac.uk/info/mias.html) and divided into two classes [normal](https://github.com/srijansingh53/IP_project/tree/master/dataset/normal) and [circ-calc](https://github.com/srijansingh53/IP_project/tree/master/dataset/circ-calc)

## Scripts

The module contains different python programs that are interdependent for use in the project

- ### [main.ipynb](https://github.com/srijansingh53/IP_project/tree/master/main.ipynb) : A jupyter notebook that contains all the steps and visualization of the algorithm

- ### [main.py](https://github.com/srijansingh53/IP_project/tree/master/main.py) : It is the driving python script which import steps of the algorithm

- ### [steps.py](https://github.com/srijansingh53/IP_project/tree/master/steps.py) : It is a class based script which function code of the algorithm step-wise

- ### [compare.py](https://github.com/srijansingh53/IP_project/tree/master/compare.py) : It compares the proposed algorithm with some prevalent IP enhancement techniques like Histogram Equalization and CLAHE

## Algorithm
- Flow Chart
    ![Flow Chart](/assets/flowchart.png)
- Pseudo Code
    ![Pseudo code](/assets/pseudocode.png)

## Results
The goal of the project is to enhance the breast mammographic images so as to ease the detection of micro-calcifications or granular masses that may be malignant.

### First Step
The film-artifacts were removed using a 5x5 averaging kernel and then taking the difference between the original and mean image thresholded over a value. 

![filtered](/outputs/filtered.jpg)

### Second Step
The gradient images using both horizontal and vertical sobel operators were calculated.

![gradient](/outputs/gradient.jpg)

### Third Step
The adaptive signal gain is calculated for each gradient images and the multiplied to it and then added to the filtered image.

![enhanced](/outputs/enhanced.jpg)

### Compared Results
The results were compared with existing engancement techniques like histogram equalization and CLAHE

![comparison](/outputs/comparison.jpg)

## Contribution
- Mentor - Dr. Pritee Khanna
- Team - [Srijan Singh](https://github.com/srijansingh53) and [Rishikesh Ghule](https://github.com/rushi04)
- Course - CS313a - Image Processing
- Indian Institute of Information Technology, Design and Manufacturing, Jabalpur
