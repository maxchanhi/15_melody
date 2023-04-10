
from synth import play_back
def append_note(accend_decend, pitch_class):
    append = accend_decend + str(pitch_class)
    return append
def generate_interval():
    import random
    pitch_class = [x for x in range(0,16)]
    accend_decend = ["+","-"]
    results = []
    while len(results) < 10:
        melody = []
        for loop in range(5):
            acc_dec = random.choice(accend_decend)
            pitch = random.choice(pitch_class)
            note = append_note(acc_dec, pitch)
            melody.append(note)
            melody_sum = sum((eval(x) for x in melody))
            if melody_sum > 23 or melody_sum < -23:
                melody = []
                break
            else:
                pass
        if len(melody) == 5:
            results.append(melody)
        else:
            pass
    return results
def get_frequencies(start_freq, num_octaves):
    half_step_ratio = 2 ** (1/15)
    frequencies = [start_freq]
    for i in range(num_octaves):
        for j in range(15):
            next_freq = frequencies[-1] * half_step_ratio
            frequencies.append(next_freq)
    return frequencies
def rate_results(results):
    ratings = []
    for i in range(len(results)):
        print(f"Result: {results[i]}")
        play_back(play_freq(results)[i])
        rating = input("Rate this result good(g)/bad(b): ")
        while rating not in ["g", "b"]:
            rating = input("Invalid input. Please rate this result as g/b: ")
        ratings.append(rating)
    return ratings,results
def play_freq(results):
    list=[]
    for result in results:
        pointer = int(15*3/2)
        play_freqs = [freqs[pointer]]
        for x in result:
            pointer+=eval(x)
            play_freqs.append(freqs[pointer]) 
        list.append(play_freqs)
    return list
def select_melodies(rate,melody):
    list = []
    for x in range(len(rate)):
        if rate[x]=="g":
            list.append(melody[x])
        else:
            pass
    return list


freqs = get_frequencies(110, 3)
#rate_results(generate_interval())

list = [generate_interval() for x in range(10)]
import json
with open('melodies.json', 'w') as f:
    # Loop through the list and add each element to the file
    f.write("[")
    for item in list:
        json.dump(item, f)
        f.write(',')
        f.write('\n')
    f.write("]")
results1 = generate_interval()