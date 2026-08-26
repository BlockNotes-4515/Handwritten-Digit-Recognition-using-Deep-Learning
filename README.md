# Handwritten Digit Recognition using Deep Learning

## Project Overview

This project recognizes handwritten digits using a Convolutional Neural Network (CNN).

The model is trained on the MNIST handwritten digit dataset.

## Technologies Used

- Python
- TensorFlow
- Keras
- CNN
- MNIST
- NumPy
- Scikit-learn
- Streamlit
- Streamlit Drawable Canvas

## Model Architecture

Input: 28 x 28 x 1

Conv2D - 32 filters
MaxPooling

Conv2D - 64 filters
MaxPooling

Flatten

Dense - 128 neurons
Dropout - 0.5

Output - 10 neurons
Softmax

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```
