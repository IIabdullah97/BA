
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
        "الشمس لا تغطى بغربال، الاتحاد هو كبير آسيا"
    </div>
    """,
    unsafe_allow_html=True
)


