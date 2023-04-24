import streamlit as st
import numpy as np
from rate import play_freq,generate_interval,results1
from synth import st_play_back
results = results1
ratings = []
def main():
    st.title("Rate Results")
    state = 0
    while state < len(results):
        st.write(f"Melodic_interval: {results[state]}")
        st_play_back(play_freq(results)[state])
        rating = st.radio("Rate this result:", ["Good","-", "Bad"],index=1, key=f"radio{state}")
        if rating == "Good":
            ratings.insert(state, "g")
        elif rating == "Bad":
            ratings.insert(state, "b")
        else:
            ratings.insert(state, "")
        state += 1
    st.success(f"Ratings: {ratings}, {results}")   
    
if __name__ == "__main__":
    main()
    
