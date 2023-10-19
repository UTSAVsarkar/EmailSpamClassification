import pickle
import streamlit as st

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]

def show_predict_page():
    email = st.text_area('**Enter the mail content**', placeholder="Type Here.....")

    ok = st.button(":blue[Predict]")

    if ok:
        if email == "":
            st.error('Please enter the mail content!', icon="🚨")
        else:
            output = model.predict([email])

            if(output[0] == 1):
                st.subheader("Email predicted as spam")
            else:
                st.subheader("Email Predicted as Non-Spam")

            st.write("""### 👈 To know more about the dataset, go to About page""")

