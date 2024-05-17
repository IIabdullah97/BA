
import streamlit as st


st.title("Welcome")

st.image("https://pbs.twimg.com/media/BFvJWkSCcAEbRRe.jpg", caption="Your Image Caption", use_column_width=True)

# Display the message with custom styles
st.markdown(
    """
    <style>
    .custom-text {
        color: blue;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    <div class="custom-text">
        Hi Bader, it is easy to develop a web but hard to deploy/publish our local host interface
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .custom-text {
        color: blue;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    <div class="custom-text">
        Hi Bader, it is easy to develop a web but hard to deploy/publish our local host interface
    </div>
    """,
    unsafe_allow_html=True
)

