import streamlit as st
import plotly.express as px
from backend import get_data

# Title, text input, slider, select box, and subheader
st.title("Weather Forecast for Next Days")
place = st.text_input('Place: ')
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
    try:
        data = get_data(place, days)

        # if option == "Temperature":
        #     temperatures = [d['main']['temp'] for d in data]
        #     dates = [d['dt_txt'] for d in data]
        #     figure = px.line(x=dates, y=temperatures,line_shape='spline', labels={"x": "Date", "y": "Temperature (C)"})
        #     st.plotly_chart(figure)
        if option == "Sky":
            sky_conditions = [d['weather'][0]['main'] for d in data]
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                      'Snow': 'images/snow.png'}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("That is wrong place, please provider correct place name")
