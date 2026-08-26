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
## ✦ Learning Outcomes
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

```
## ✦ Main Commands to Run this Project
```
# Clone
git clone https://github.com/YOUR_USERNAME/Handwritten-Digit-Recognition.git

# Enter project
cd Handwritten-Digit-Recognition

# Create environment
python -m venv venv

# Activate Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py

# Check changes
git status

# Stage changes
git add .

# Commit
git commit -m "Update project"

# Push
git push origin main

---
```
# ✦ Result Pipeline
```
```text
                    USER
                     │
                     ▼
              Draw Handwritten
                  Digit
                     │
                     ▼
              Image Capture
                     │
                     ▼
              Preprocessing
                     │
                     ▼
                 28 × 28
                   Image
                     │
                     ▼
                   CNN
                     │
                     ▼
              Softmax Output
                     │
                     ▼
          ┌──────────────────────┐
          │                      │
          ▼                      ▼
    Predicted Digit        Probability
                              Scores
          │                      │
          └──────────┬───────────┘
                     ▼
              Streamlit UI
                     │
                     ▼
        Prediction + Confidence
             + Probabilities

```
# ✦ Model Results

<div align="center">

| Training Accuracy | Training Loss |
|:---:|:---:|
| <img src="results/accuracy.png" width="420"> | <img src="results/loss.png" width="420"> |
| **Training & Validation Accuracy** | **Training & Validation Loss** |

<br>

| Confusion Matrix | Model Architecture |
|:---:|:---:|
| <img src="results/confusion_matrix.png" width="420"> | <img src="results/architecture.png" width="420"> |
| **Classification Performance** | **CNN Architecture** |

<br>

| User Input | AI Prediction |
|:---:|:---:|
| <img src="assets/input.png" width="420"> | <img src="assets/prediction.png" width="420"> |
| **Handwritten Digit Input** | **Predicted Digit & Confidence** |

<br>

| Probability Distribution |
|:---:|
| <img src="results/probability.png" width="850"> |
| **Class-wise Prediction Probability** |

</div>
