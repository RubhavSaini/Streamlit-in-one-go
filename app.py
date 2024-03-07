import streamlit as st
st.title("TITLE")
st.header("Header")
st.subheader("subheader")
st.text("text sdfasdf")

st.markdown("# markdown")
st.markdown("## markdown")
st.markdown("### markdown")
st.markdown("markdown")

st.success("success")
st.warning("warning")
st.info("info")
st.error("error")
st.exception(ZeroDivisionError("not possible"))

st.help(ZeroDivisionError)

st.write(1+2+3)
st.write("1+2+3")
st.write("range(1,10)")
st.write(range(1,10))

st.code("x=10\n"
        "for i in range(10)\n"
            "   print(i)")

st.checkbox("Male")
if(st.checkbox("Adult")):
    st.write("you are a Adult")

# st.radio('Select :',('Male','Female'))   
radiobtn= st.radio('Select :',('Male','Female'))   
if(radiobtn=='Male'):
    st.write("You are male")
else:     
    st.write("You are female")


st.subheader('Select Box')                              
selectBox =  st.selectbox("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
st.write("You've selected : ", selectBox)


st.subheader('MultiSelect Box')                       
multiSelBox = st.multiselect("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                    'Deep Learning','Natural Language Processing',
                                                    'Computer Vision','Image Processing'])
# st.write("You've selected : ", len(multiSelBox) , multiSelBox)
st.write("You've selected : ", len(multiSelBox) , 'courses')


st.subheader("Button")                                  # Button
if(st.button('Click me')):
    st.write('Thanks for clicking me')


st.subheader("Slider")                                  # Slider
vol = st.slider('Select the volume',0,100,step = 1)
st.write('Volume is : ',vol)


st.subheader("Text Input")                              # Text-Input
username = st.text_input('Username : ')
if(username):
   st.write('hello :',username)
password = st.text_input('Password : ', type = 'password')


st.subheader("Text Area")                              # Text-Area
st.text_area('Write something interesting about yourself')

st.subheader("Input Number")                           # Input-Number
st.number_input('Select your age',18,110)

st.subheader("Input Date")                              # Input-Date
st.date_input('Date')

st.subheader("Input Time")                              # Input-Time
st.time_input('Time')