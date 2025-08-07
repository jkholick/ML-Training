import streamlit as st


hide_sidebar_complete = """
    <style>
        /* Hide sidebar nav items */
        [data-testid="stSidebarNav"] {
            display: none;
        }

        /* Hide the entire sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }

        /* Hide the sidebar collapse/expand button */
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_complete, unsafe_allow_html=True)


st.title("Main Page")
st.write("Click a button to go to another page:")

# Generate navigation links (button + query param redirect)
Salary_Prediction_url = "pages/Salary Prediction.py"
Roast_AI_url = "pages/Roast_AI.py"

col1, col2 = st.columns(2)

with col1:
    if st.button("Salary Prediction"):
        st.switch_page(Salary_Prediction_url)

with col2:
    if st.button("Go to Roast AI"):
        st.switch_page(Roast_AI_url)

