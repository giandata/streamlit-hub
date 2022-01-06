import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image


with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Text', 'Data', 'Widgets','Structure'],
        icons=['house', 'text-left','clipboard-data','download','building'], menu_icon="menu-app", default_index=1)
    st.markdown("Author: [Giancarlo Di Donato](https://www.linkedin.com/in/giancarlodidonato/)")
   

if selected == "Home":
    st.title ("How To Streamlit App")
    st.subheader("This is a showcase of most useful Streamlit APIs")
    st.markdown('''Read the [docs] (https://docs.streamlit.io/library/api-reference) for a complete reference of all Streamlit widgets and features.''')
    
    st.write('Use the sidebar menu to navigate the groups of widgets.')

    image = Image.open('streamlit-logo-primary-colormark-darktext.png')

    st.image(image)

    st.write("To start using Streamlit’s open-source app framework it’s just a matter of installing it in a dedicated environment:")
    st.code ("pip install streamlit")
    
    st.write("then create a script and execute from the terminal:")
    st.code("streamlit run your_app.py")

    st.write("and it will open locally in a browser tab.")

if selected == "Text":
    st.title ("How to display text")
    st.write("Streamlit provides several ways to display text:")

    with st.echo():
        
        st.title("This is the title")

        st.header("Header")

        st.subheader("And this is sub header")

        st.write("This code will be printed")

        st.markdown("Awesome **Streamlit**!")

        st.caption("Little text")

        code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')

if selected == "Data":
    st.title ("How to display Data")

    df = pd.DataFrame(
    np.random.randn(50, 10),
    columns=('col %d' % i for i in range(10)))

    st.subheader("Show a dataframe:")
    with st.echo():
        
        st.dataframe(df)

    st.subheader("Show some metrics:")
    with st.echo():    
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "20 °C", "1.0 °C")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "66%", "4%")


    st.subheader("Or show charts from multiple libraries:")
    with st.echo():    
        ##native Streamlit library
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        st.line_chart(chart_data)

        df = pd.DataFrame(
            np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

        ## Altair chart
        c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

        st.altair_chart(c, use_container_width=True)

if selected == "Widgets":
    st.title("The widgets enhance the interactivity of the applications.")
    
    st.write("A simple button to execute actions")
    with st.echo():
        ## Button
        clicked = st.button(label="Click me")
        if clicked:
            st.write("Click event")

    st.write("Or a container of widgets ")
    with st.form("Widget form"):
        st.subheader("This is a form")
        st.write("Since the app reruns entirely at every user interaction, it is possible to use a form to control the flow and pass all the input paramenters at once, clicking on the submit button")
        
        with st.echo():
            
            ## Slider
            slider = st.slider("Select number:",1,25)
            
            ## Radio button
            radio = st.radio("Radio Button:",["Fish","Birds","Mammals"])

            ## Selector
            select = st.selectbox("Selectbox:",["Cats","Dogs","Mices"],help =" Information tooltip")

            ## Multiselector
            multiselect = st.multiselect("Teams:",["Barcelona","Naples","Rome","Madrid"],help =" Information tooltip")

            ## Text input
            text = st.text_input("Insert your name")

            ## Number input
            number = st.number_input("Insert your age",step=1)

            ##Date input
            date = st.date_input("Your birthday")

            ## Checkbox    
            agree = st.checkbox('I agree')
                
        submitted = st.form_submit_button("Submit")

if selected == "Structure":
    st.title("How to organize the layout of your app")
