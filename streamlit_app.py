import streamlit as st
 
def main():
    st.title("Form Filling App")
 
    # Form inputs
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150)
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    # st.checkbox('yes')
    # st.button('Click')
    # st.radio('Pick your gender',['Male','Female'])
    # st.selectbox('Pick your gender',['Male','Female'])
    # st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
    # st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
    # st.slider('Pick a number', 0,50)
    # # Submit button
    if st.button("Submit"):
        if name and age and email and phone:
            st.success(f"Name: {name}\nAge: {age}\nEmail: {email}\nPhone: {phone}")
        else:
            st.warning("Please fill all the fields")
            
 
if __name__ == "__main__":
    main()
