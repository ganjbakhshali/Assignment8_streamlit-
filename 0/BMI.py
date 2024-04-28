import streamlit as st

def calculate_bmi(height, weight):
    """
    Calculate BMI (Body Mass Index) given height (in meters) and weight (in kilograms).
    """
    bmi = weight / (height ** 2)
    return bmi

def get_body_type(bmi):
    """
    Determine the body type based on BMI.
    """
    if bmi < 18.5:
        return "Underweight", "under.jpg"
    elif bmi < 24.9:
        return "Normal weight", "normal.jpg"
    elif bmi < 29.9:
        return "Overweight", "over.jpg"
    else:
        return "Obese", "obese.jpg"

def main():
    st.title("BMI Calculator")
    height = st.slider("Height (in meters)", min_value=0.5, max_value=2.5, step=0.01, value=1.7)
    weight = st.slider("Weight (in kilograms)", min_value=20, max_value=200, step=1, value=70)
    bmi = calculate_bmi(height, weight)
    body_type, body_image_filename = get_body_type(bmi)
    st.write(f"Your BMI is: {bmi:.2f}")
    st.write(f"You are {body_type}")
    st.image(body_image_filename, caption=body_type, use_column_width=True)

if __name__ == "__main__":
    main()
