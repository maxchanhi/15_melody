import numpy as np
import pyaudio
import time
freq_list=[440,550,660]
def play_back(freq_list):
    duration = 1.0
    volume = 0.2
    overtones = 4
    fade_in = int(0.05 * 44100)  # 50 ms fade in
    fade_out = int(0.2 * 44100)  # 200 ms fade out

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

    for freq in freq_list:
        t = np.linspace(0, duration, int(duration * 44100), False)
        note = volume * np.sin(freq * 2 * np.pi * t)
        # Add overtones
        for overtone in range(1, overtones+1):
            overtone_freq = freq * overtone
            overtone_note = volume * np.sin(overtone_freq * 2 * np.pi * t) / overtone
            note += overtone_note
        # Add fade in and fade out
        fade_in_curve = np.linspace(0, 1, fade_in)
        fade_out_curve = np.linspace(1, 0, fade_out)
        note[:fade_in] *= fade_in_curve
        note[-fade_out:] *= fade_out_curve
        # Play the note
        stream.write(note.astype(np.float32).tobytes())

    fade_out_curve = np.linspace(1, 0, fade_out)
    silence = np.zeros(fade_out)
    silence[-fade_out:] = fade_out_curve * volume
    stream.write(silence.astype(np.float32).tobytes())

    time.sleep(0.1)
    



