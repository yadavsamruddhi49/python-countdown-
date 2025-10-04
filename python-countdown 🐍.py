## python-countdown 🐍

import time
import streamlit as st

# Title
st.title("⏳ Countdown Timer")

# Input
t = st.number_input("Enter time in seconds:", min_value=1, step=1, value=10)

# Start button
if st.button("Start Countdown"):
    countdown_placeholder = st.empty()

    for remaining in range(t, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        countdown_placeholder.markdown(f"### ⏱️ {timer}")
        time.sleep(1)

    countdown_placeholder.markdown("## 🔥 Fire in the hole!!")
