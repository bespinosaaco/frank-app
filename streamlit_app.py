import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Line Plot Viewer", layout="wide")

st.title("Hey! Francis 🦉")
st.caption('Mira que cool!!')

uploaded_file = st.file_uploader("Drag and drop a file here or click to upload", type=["csv", "xlsx"])
col1, col2, col3 = st.columns([1,1,3])
if uploaded_file is not None:
    # Display file details
    with col1:
        st.write("Uploaded File Details:")
        st.write(f"Filename: {uploaded_file.name}")
        st.write(f"File type: {uploaded_file.type}")
        st.write(f"File size: {uploaded_file.size} bytes")

    # Read and display the file content
    if uploaded_file.type == "text/csv":
        data = pd.read_csv(uploaded_file, header=None)
        with col2:
            st.write("File content:")
            st.dataframe(data,use_container_width=True)

if uploaded_file is not None:

    # Ensure the DataFrame has at least two columns
    if len(data.columns) >= 2:
        # Column 0 and Column 1 for line chart
        column_0 = data.iloc[:, 0]  # First column
        column_1 = data.iloc[:, 1]  # Second column

        # Create a DataFrame for plotting
        plot_df = pd.DataFrame({
            "Intensity": column_0,
            "Wavenumber": column_1
        })

        # Generate line chart using Plotly
        fig = px.line(plot_df, x="Intensity", y="Wavenumber", title="Line Chart")
        fig.update_xaxes(range=[4000, 400])
        # Display the Plotly figure in Streamlit
        with col3:
            st.plotly_chart(fig,use_container_width=True)
    else:
        st.error("The uploaded file must have at least two columns.")