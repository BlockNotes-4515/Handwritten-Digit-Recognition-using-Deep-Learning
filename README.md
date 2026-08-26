<div align="center">

# ✦ Digit AI

### Handwritten Digit Recognition using Deep Learning

**Draw a digit. Let the neural network understand it.**

A production-style computer vision project powered by  
**Convolutional Neural Networks · TensorFlow · Keras · MNIST · Streamlit**

<br>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![MNIST](https://img.shields.io/badge/Dataset-MNIST-111111?style=for-the-badge)](https://yann.lecun.com/exdb/mnist/)
[![License](https://img.shields.io/badge/License-MIT-111111?style=for-the-badge)](LICENSE)

<br>

[**Live Demo**](#-live-demo) ·
[**Architecture**](#-system-architecture) ·
[**Results**](#-model-performance) ·
[**Installation**](#-installation) ·
[**Contributing**](#-contributing)

</div>

---

## ✦ The Idea

**Digit AI** is an interactive handwritten digit recognition system that combines
deep learning with a minimal, intuitive user experience.

Instead of uploading an image, users can simply **draw a digit directly on the
screen**. The application captures the drawing, transforms it into a format
understood by the neural network, and produces a real-time prediction.

The system doesn't only return the predicted digit.

It also explains the prediction through:

- 🎯 Predicted digit
- 📊 Confidence score
- 📈 Probability distribution across all 10 classes
- 🖼️ Processed image seen by the model
- 🧠 CNN-based classification

The project covers the complete machine learning lifecycle:

```text
Data
  ↓
Preprocessing
  ↓
CNN Design
  ↓
Training
  ↓
Evaluation
  ↓
Model Serialization
  ↓
Inference Pipeline
  ↓
Interactive Web Application
  ↓
Real-Time Prediction
```
## ✦ The Idea
```
Handwritten-Digit-Recognition/
│
├── 📄 README.md
├── 📄 CONTRIBUTING.md
├── 📄 LICENSE
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 🐍 app.py
│
├── 📁 model/
│   └── digit_model.keras
│
├── 📁 src/
│   ├── __init__.py
│   ├── preprocess.py
│   └── predict.py
│
├── 📁 notebooks/
│   └── training.ipynb
│
├── 📁 assets/
│   ├── architecture.png
│   ├── input.png
│   ├── prediction.png
│   ├── probability.png
│   └── training.png
│
└── 📁 results/
    ├── accuracy.png
    ├── loss.png
    └── confusion_matrix.png

```
## ✦ The Idea
```
Python
 │
 ├── NumPy
 └── Pillow
 │
 ▼
Machine Learning
 │
 ├── Image Processing
 ├── Classification
 └── Evaluation
 │
 ▼
Deep Learning
 │
 ├── CNN
 ├── ReLU
 ├── Pooling
 ├── Dense Layers
 ├── Dropout
 └── Softmax
 │
 ▼
Application Development
 │
 └── Streamlit
 │
 ▼
Engineering
 │
 ├── Git
 ├── GitHub
 ├── Modular Architecture
 └── Documentation
