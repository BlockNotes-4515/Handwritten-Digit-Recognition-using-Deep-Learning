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

# ✦ Model Results

<div align="center">

### Training Performance

The CNN was trained and evaluated on the MNIST handwritten digit dataset.
The following visualizations summarize the model's learning and classification
performance.

</div>

---

## 📈 Training Accuracy

The training and validation accuracy curves show how the model improves during
training.

<div align="center">

<img src="assets/training_accuracy.png" width="800">

</div>

---

## 📉 Training Loss

The loss curve shows the optimization progress of the CNN throughout training.

<div align="center">

<img src="assets/training_loss.png" width="800">

</div>

---

## 🎯 Confusion Matrix

The confusion matrix provides a class-wise view of correct and incorrect
predictions across digits `0–9`.

<div align="center">

<img src="assets/confusion_matrix.png" width="800">

</div>

---

# ✦ Model Metrics

| Metric | Result |
|:---|---:|
| Dataset | MNIST |
| Training Samples | 60,000 |
| Testing Samples | 10,000 |
| Input Shape | `28 × 28 × 1` |
| Number of Classes | 10 |
| Classes | `0 – 9` |
| Model Architecture | CNN |
| Framework | TensorFlow / Keras |
| Optimizer | Adam |
| Loss Function | Sparse Categorical Crossentropy |
| Output Activation | Softmax |
| Training Epochs | `XX` |
| Batch Size | `XX` |
| Test Accuracy | **XX.XX%** |
| Test Loss | **X.XXXX** |
| Model Size | `XX MB` |
| Inference | Real-time |

> Replace `XX` values with the actual values obtained from your training run.

---

# ✦ Recognition Results

The final application performs real-time inference directly from the user's
handwritten input.

<div align="center">

### User Input

<img src="assets/input.png" width="380">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

### AI Prediction

<img src="assets/prediction.png" width="380">

</div>

---

## 📊 Probability Distribution

The model generates a probability score for every digit from `0` to `9`.

<div align="center">

<img src="assets/probability.png" width="800">

</div>

Example:

| Digit | Probability |
|:---:|---:|
| 0 | 0.01% |
| 1 | 0.02% |
| 2 | 0.03% |
| 3 | 0.01% |
| 4 | 0.01% |
| 5 | 0.12% |
| 6 | 0.02% |
| **7** | **98.72%** |
| 8 | 0.71% |
| 9 | 0.37% |

> The probability values above are illustrative. Actual values are generated
> dynamically by the trained model.

---

# ✦ Result Pipeline

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
