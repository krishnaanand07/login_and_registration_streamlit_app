import streamlit as st

#header.
st.header("Anurag university Student Records Management")
#title of the app

st .title("welcome to student records management system")
#subheader of the app
st.subheader("Mang student efficiently and effectively")

#text method to display information 

st.text("Hii,I am krishna Anand Chauhan ")

#horizontal line

st.markdown("----------------------------")

#write method--allows to write something 

st.write(" hello krishna")
st.write(123456)
st.write(1,2,3,4,5)

# st.write("name""krishna","role":"student")
st.markdown("### this is markdown")
st.markdown("**Bold text**")
st.markdown("*Italic*")
st.markdown("-item 1\n item 2-")

st.markdown("<h3 style=color:red>RED TEXT </h3>",unsafe_allow_html=True)

st.code("""
        def add(a,b):
            return a+b
        
        """,language='python')

#latex
st.latex(r''' a^2 + b^2 = c^2 ''')

#divider
st.divider()

if st.button("click me"):
    st.success("button clicked")
    st.balloons()
    st.snow()
else:
    st.error("button not clicked")

#text input
name=st.text_input("enter your name")
# st.write("your name is:",name)

if name ==" ":
    st.warning("Name cannot be empty")
elif not name.isalpha():
    st.error("Name should contain only alphabets no numbers allowed")
else:
    st.success(f"Welcome {name} to Anurag University")
    
#number input
age=st.number_input("enter your age",min_value=1,max_value=100,step=1)
st.write("your age is:",age)

#mutli line text input
address=st.text_area("enter your address")
st.write("your address is:",address)

st.checkbox("I agree to the terms and conditions")
st.radio("select your gender",("male","female"))
country=st.selectbox("select your country",("india","usa","uk","canada"))
st.write("your country is:",country)
hobbies=st.multiselect("select your hobbies",("reading","traveling","coding","sports")) 
st.write("your hobbies are:",hobbies)
st.slider("select your age :",0,100,25)

uploaded_file=st.file_uploader("choose a file")
if uploaded_file is not None:
    st.success("file uploaded successfully")
    st.write("filename:",uploaded_file.name)




with st.form("my_form"):
    st.text_input("enter your email")
    st.number_input("enter your age",min_value=1,max_value=100,step=1)
    submit=st.form_submit_button("submit")
if submit:
    st.write("name:",name,"age:",age)
    st.success("form submitted successfully")
#form submission
with st.form("login"):
    name=st.text_input("enter your email")
    age= st.number_input("enter your age",min_value=1,max_value=100,step=1)
    login=st.form_submit_button("login")
if login:
    st.write("name:",name,"age:",age)
    st.success("form submitted successfully")
st.divider()
#columns
col1,col2,col3=st.columns(3)
with col1:
    st.header("column 1")
    st.text("this is column 1")
with col2:
    st.header("column 2")
    st.text("this is column 2")
with col3:
    st.header("column 3")
    st.text("this is column 3")

st.divider()
#container
container=st.container()
container.write("this is inside the container")
container.button("click")

data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

st.divider()

#sidebar
st.sidebar.title("sidebar title")
option=st.sidebar.selectbox("select an option",("option 1","option 2","option 3"))
st.sidebar.write("you selected:",option)


@st.cache_data
def laod_data():
    return [1,2,3,4]
data=laod_data()
st.write(data)
