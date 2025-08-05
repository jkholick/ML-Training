import streamlit as st
import joblib 
import numpy as np
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Salary Estimation App",layout="wide")
st.title("Salary estimation")
st.markdown("Predict salary based on company experience!")


page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://fortune.com/img-assets/wp-content/uploads/2022/02/GettyImages-1354585791-e1644460734266.jpg?resize=1200,600");
  background-size: cover;
  background-color: rgba(0,0,0,0.6);
  background-blend-mode: darken;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)

#st.image(r"https://fortune.com/img-assets/wp-content/uploads/2022/02/GettyImages-1354585791-e1644460734266.jpg?resize=1200,600")

st.divider()

col1,col2,col3 = st.columns(3)

with col1:
    years_at_company = st.number_input("Years at company",min_value=0,max_value=20,value=3)

with col2:
    satisfaction_level = st.number_input("Satisfaction Level",min_value=0.0,max_value=1.0,value = 0.7)

with col3:
    avg_monthly_hrs = st.number_input("Average monthly hours",min_value=120,max_value=310,step=1)

x = [years_at_company,satisfaction_level,avg_monthly_hrs]

scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

predict_button = st.button("Predict Salary")

st.divider()

if predict_button:
    st.balloons()

    x_array = scaler.transform([np.array(x)])
    prediction = model.predict(x_array)

    st.success(f"Predicted Salary: Rs.{prediction[0]:,.2f}")

    df_input = pd.DataFrame({
        "Feature":["Years at Company","Satisfcation Level","Average Monthly Hours"],
        "Value": x
    })
    fig = px.bar(df_input,x="Feature",y="Value",color="Feature",title="Your Input Profile",text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Enter details and click 'Predict Salary'.")
