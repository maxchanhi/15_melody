import streamlit as st

from rate import generate_interval, play_back, play_freq,results1
results = results1
ratings = []
def main():
    
    st.title("Rate Results")
    state = 0
    while state < len(results):
        st.write(f"Melody: {results[state]}")
        if st.button("Play", key=f"play{state}"):
            play_back(play_freq(results)[state])
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
    