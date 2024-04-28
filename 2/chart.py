import streamlit as st
import pandas as pd

def main():
    st.title("Simple Data Science App")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a .csv file", type=["csv"])

    if uploaded_file is not None:
        # Read CSV file into pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Show DataFrame in a table
        st.write("### DataFrame")
        st.write(df)

        # Sidebar with information about the app
        st.sidebar.title("About")
        st.sidebar.info(
            "This is a simple data science app where you can upload a CSV file, "
            "view its contents in a table, and generate a chart based on the data."
        )

        # Draw a chart
        st.write("### Chart")
        chart_type = st.selectbox("Select chart type", ["Line", "Bar"])
        numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
        selected_x_column = st.selectbox("Select a column for the X axis", df.columns)
        selected_y_column = st.selectbox("Select a column for the Y axis", numerical_columns)
        st.write(f"Selected X axis: {selected_x_column}, Selected Y axis: {selected_y_column}")
        if chart_type == "Line":
            st.line_chart(df.set_index(selected_x_column)[selected_y_column])
        elif chart_type == "Bar":
            st.bar_chart(df.set_index(selected_x_column)[selected_y_column])

if __name__ == "__main__":
    main()
