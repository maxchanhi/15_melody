import streamlit as st

from rate import play_freq,generate_interval,results1
from synth import st_play_back
results = results1
ratings = []

def main():
    
    st.title("Rate Results")
    state = 0
    
    while state < len(results):
        st.write(f"Melody: {results[state]}")
        st_play_back(play_freq(results)[state])
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
    
