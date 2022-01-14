import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Text', 'Data', 'Widgets','Structure',"State management"],
        icons=['house','text-left','clipboard-data','download','building','clock'], menu_icon="menu-app", default_index=0)
    st.markdown("Author: [Giancarlo Di Donato](https://www.linkedin.com/in/giancarlodidonato/)")
   
if selected == "Home":
    st.title ("How To Streamlit ")
    st.subheader("This app is a showcase of most useful Streamlit APIs")
    st.markdown('''Read the [docs] (https://docs.streamlit.io/library/api-reference) for a complete reference of all Streamlit widgets and features.''')
    
    

    image = Image.open('streamlit-logo-primary-colormark-darktext.png')

    st.image(image)

    st.subheader("Get started")
    st.write("To start using Streamlit’s open-source app framework it’s just a matter of installing it in a dedicated environment:")
    st.code ("pip install streamlit")
    
    st.write("then create a script and execute from the terminal:")
    st.code("streamlit run your_app.py")

    st.write("and it will open locally in a browser tab.")

    st.info('Use the sidebar menu to navigate the app through the sections. (Click on left top arrow to open it)')


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

    st.subheader("Displays notifications with variants:")

    with st.echo():
        st.info("Info message")
        st.success("Success message")
        st.warning("warning message")
        st.error("Error message")

if selected == "Data":
    st.title ("How to display Data")

    st.subheader("Streamlit is a lightning fast framework great for Data Science: it allows to load, process, visualize and export data ")

    df = pd.DataFrame(
        np.random.randn(50, 10),
        columns=('col %d' % i for i in range(10)))

    st.subheader("Show a dataframe:")
    with st.echo():
        
        st.dataframe(df)

    st.subheader("Show visual metrics:")
    with st.echo():    
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "20 °C", "1.0 °C")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "66%", "4%")


    st.subheader("Or show charts from multiple libraries:")
    with st.echo():    
        ##native Streamlit chart library
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
    
    st.subheader("A simple button to execute actions")
    with st.echo():
        ## Button
        clicked = st.button(label="Click me")
        if clicked:
            st.write("Click event")

    st.write("Since the app reruns entirely at every user interaction, it is possible to use a form to control the flow and pass all the input paramenters at once, clicking on the submit button")

    with st.form("Widget form"):
        st.subheader("This is a form")
        
        with st.echo():
            
            ## Slider
            slider = st.slider("Select number:",1,25)
            
            ## Radio button
            radio = st.radio("Radio Button:",["Fish","Birds","Mammals"])

            ## Selector
            select = st.selectbox("Selectbox:",["Cats","Dogs","Mices"],help ="Select only one element")

            ## Multiselector
            multiselect = st.multiselect("Teams:",["Barcelona","Naples","Rome","Madrid"],help ="Select multiple elements")

            ## Text input
            text = st.text_input("Insert your name")

            ## Number input
            number = st.number_input("Insert your age",step=1)

            ##Date input
            date = st.date_input("Your birthday")

            ## Checkbox    
            agree = st.checkbox('I agree')
                
        submitted = st.form_submit_button("Submit")

    st.subheader("There are also widgets to upload or download data:")

    with st.echo():
        input = st.file_uploader("Load file")

        data = "Some data"
        output = st.download_button("Download file", data)

if selected == "Structure":
    st.title("How to organize the layout of your app")
    st.subheader("Streamlit provides several options for controlling different elements are laid out on the screen. The most useful are the columns, the expanders and the sidebar.")
    with st.container():
        with st.echo():

            col1,col2 = st.columns(2)

            with col1:
                st.header("Column 1")
                widget= st.radio("How you find Streamlit?",["Awesome","Cool","Fantastic"])
            
            with col2:
                st.header("Column 2")
                widget2 = st.radio("Will you use Streamlit?",["Maybe","For sure","Can't wait!"])

    st.write("This is outside the container. It is possible to stack up multiple containers:")
    
    with st.container():
        col1,col2 = st.columns(2)

        with st.echo():
            with col1:
                with st.expander("Expander 1"):
                    st.write("Some text")

            with col2:
                with st.expander("Expander 2"):
                    st.write("Other text")

if selected == "State management":
    st.title("How to manage the session state (WIP)")     
    st.subheader("Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state.")       

    with st.echo():


        ## Every widget with a key is automatically added to Session State:
        input = st.radio("Assign a value",["1","2","3","4"])
        if input:
            st.session_state.key = input
        
        st.write(f'The key of the widget is now {st.session_state.key}')
        
        delete = st.button("Delete value")
        if delete:
            del st.session_state.key
            st.write("value:" ,st.session_state)

    
