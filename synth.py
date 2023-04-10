import numpy as np

import time
freq_list=[440,550,660]

import streamlit as st
freq_list=[440,550,660]
def st_play_back(freq_list):
    duration = 1.0
    volume = 0.2
    overtones = 4
    fade_in = int(0.05 * 44100)  # 50 ms fade in
    fade_out = int(0.2 * 44100)  # 200 ms fade out

    # Create empty array to store the final audio clip
    clip = np.zeros(int(duration * 44100 * len(freq_list)))

    # Iterate over frequencies and concatenate notes
    for i, freq in enumerate(freq_list):
        t = np.linspace(0, duration, int(duration * 44100), False)
        note = volume * np.sin(freq * 2 * np.pi * t)
        # Add overtones
        for overtone in range(1, overtones+1):
            overtone_freq = freq * overtone
            overtone_note = volume * np.sin(overtone_freq * 2 * np.pi * t) / overtone
            note += overtone_note
        # Add fade in and fade out
        fade_in_curve = np.linspace(0, 1, fade_in)
        fade_out_curve = np.linspace(1, 0, len(note) - len(fade_in_curve))
        fade_out_curve = np.concatenate((np.ones(fade_in), fade_out_curve))
        note *= fade_out_curve
        # Concatenate note to clip
        start_index = int(i * duration * 44100)
        end_index = int((i + 1) * duration * 44100)
        clip[start_index:end_index] = note

    # Play the clip using Streamlit
    st.audio(clip.astype(np.float32), sample_rate=44100, format='audio/wav')
