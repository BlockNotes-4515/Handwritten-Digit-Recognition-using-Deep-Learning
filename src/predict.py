
import numpy as np
import tensorflow as tf

MODEL_PATH = "model/digit_recognition_cnn.keras"

model = tf.keras.models.load_model(MODEL_PATH)


def predict_digit(image):
    """
    Predict handwritten digit.
    """

    prediction = model.predict(
        image,
        verbose=0
    )

    predicted_digit = int(
        np.argmax(prediction)
    )

    confidence = float(
        np.max(prediction) * 100
    )

    probabilities = prediction[0]

    return (
        predicted_digit,
        confidence,
        probabilities
    )
