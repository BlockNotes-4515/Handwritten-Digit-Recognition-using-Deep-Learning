
import numpy as np
from PIL import Image, ImageOps

def preprocess_image(image):
    """
    Convert the drawn image into MNIST format.
    """

    # Convert to grayscale
    image = image.convert("L")

    # Resize to 28x28
    image = image.resize((28, 28))

    # Convert to numpy array
    image = np.array(image)

    # Normalize
    image = image.astype("float32") / 255.0

    # Add channel dimension
    image = np.expand_dims(image, axis=-1)

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    return image
