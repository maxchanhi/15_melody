from synthesizer import Player, Synthesizer, Waveform
import numpy as np

player = Player()
player.open_stream()

synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

freq = 440.0  # A4
duration = 3.0
volume = 0.2
fade_in = int(0.05 * 44100)  # 50 ms fade in
fade_out = int(0.2 * 44100)  # 200 ms fade out

# Generate the note
t = np.linspace(0, duration, int(duration * 44100), False)
note = volume * np.sin(freq * 2 * np.pi * t)

# Add fade in and fade out
fade_in_curve = np.linspace(0, 1, fade_in)
fade_out_curve = np.linspace(1, 0, fade_out)
note[:fade_in] *= fade_in_curve
note[-fade_out:] *= fade_out_curve

# Play the note
player.play_wave(Synthesizer.generate_constant_wave(note, 3))



