import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

from src.predict import predict_digit
from src.preprocess import preprocess_image


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Digit AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# DARK THEME
# ============================================================

st.markdown("""
# ✦ Digit AI

### Handwritten Digit Recognition

Draw a digit from **0 to 9** and let the CNN recognize it.
""")

st.divider()


# ============================================================
# MAIN COLUMNS
# ============================================================

input_col, output_col = st.columns(
    2,
    gap="large"
)


# ============================================================
# INPUT
# ============================================================

with input_col:

    st.subheader("INPUT")

    st.write("### Draw your digit")

    canvas = st_canvas(

        fill_color="rgba(0, 0, 0, 0)",

        stroke_width=20,

        stroke_color="#FFFFFF",

        background_color="#000000",

        width=450,

        height=450,

        drawing_mode="freedraw",

        display_toolbar=True,

        key="digit_canvas"

    )

    st.write("")

    clear_col, predict_col = st.columns(2)

    with clear_col:

        clear_button = st.button(
            "Clear",
            use_container_width=True
        )

    with predict_col:

        predict_button = st.button(
            "Recognize Digit",
            type="primary",
            use_container_width=True
        )


# ============================================================
# CLEAR
# ============================================================

if clear_button:

    st.rerun()


# ============================================================
# OUTPUT
# ============================================================

with output_col:

    st.subheader("OUTPUT")

    st.write("### Prediction")


    if predict_button:

        if canvas.image_data is None:

            st.warning(
                "Please draw a digit first."
            )

        else:

            # ------------------------------------------------
            # CANVAS IMAGE
            # ------------------------------------------------

            image = Image.fromarray(
                canvas.image_data.astype("uint8")
            )

            image = image.convert("L")


            # ------------------------------------------------
            # PREPROCESS
            # ------------------------------------------------

            processed_image = preprocess_image(
                image
            )


            # ------------------------------------------------
            # PREDICTION
            # ------------------------------------------------

            digit, confidence, probabilities = (
                predict_digit(
                    processed_image
                )
            )


            # ------------------------------------------------
            # BIG PREDICTION
            # ------------------------------------------------

            st.metric(
                label="Predicted Digit",
                value=str(digit)
            )


            st.metric(
                label="Confidence",
                value=f"{confidence:.2f}%"
            )


            st.success(
                f"The model predicts **{digit}**"
            )


    else:

        st.info(
            "Draw a digit on the left and "
            "click **Recognize Digit**."
        )


# ============================================================
# RESULTS
# ============================================================

if predict_button and canvas.image_data is not None:

    st.divider()


    # ========================================================
    # PROBABILITY
    # ========================================================

    st.subheader("Probability")

    st.caption(
        "Confidence distribution across all 10 digits"
    )


    for i in range(10):

        probability = float(
            probabilities[i]
        )

        percentage = probability * 100


        # Show digit + percentage

        col_digit, col_bar, col_value = st.columns(
            [0.5, 7, 1]
        )


        with col_digit:

            if i == digit:

                st.write(
                    f"**{i}**"
                )

            else:

                st.write(
                    str(i)
                )


        with col_bar:

            st.progress(
                min(probability, 1.0)
            )


        with col_value:

            st.write(
                f"{percentage:.2f}%"
            )


    # ========================================================
    # METRICS
    # ========================================================

    st.divider()

    st.subheader("Model Metrics")


    metric1, metric2, metric3, metric4 = st.columns(4)


    with metric1:

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )


    with metric2:

        st.metric(
            "Prediction",
            str(digit)
        )


    with metric3:

        st.metric(
            "Classes",
            "10"
        )


    with metric4:

        st.metric(
            "Architecture",
            "CNN"
        )


    # ========================================================
    # WHAT MODEL SEES
    # ========================================================

    st.divider()

    st.subheader("Processed Input")

    st.image(
        processed_image[0].squeeze(),
        width=180,
        clamp=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "© dhruvdhayal - 2026 | All Rights Reserved | CNN • TensorFlow • Keras • MNIST"
)