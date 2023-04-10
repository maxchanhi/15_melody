import streamlit as st
import numpy as np
from rate import results1
results = results1
ratings = []
sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)
f = 100
def main():
    
    st.title("Rate Results")
    state = 0
    
    while state < len(results):
        st.write(f"Melody: {results[state]}")
        st.audio(note_la+f*state, sample_rate=sample_rate)
        #play_freq(results)[state])
        rating = st.text_input("Rate this result good(g)/bad(b): ", key=f"input{state}")
        if rating.lower() in [""]:
            pass
        elif rating.lower() not in ["g","b"]:
            st.warning("Please enter 'g' for good or 'b' for bad.")
        else:
            ratings.insert(state,rating)
        """______________________"""
        state += 1
    st.success(f"Ratings: {ratings}, {results}")   
    
if __name__ == "__main__":
    main()
