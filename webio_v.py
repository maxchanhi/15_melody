from pywebio.input import *
from pywebio.output import *
from rate import play_back, play_freq, results1
from pywebio import *

def main():
    ratings = []
    for i in range(len(results1)):
        put_text(f"Melody: {results1[i]}")
        #play_back(play_freq(results1)[i])
        rating = radio("Choose one", options=['Good', 'Bad'])
        ratings.append(rating)
        put_text(f"Your rated: {rating}")
    put_text(f"Result: {ratings},{results1}")
if __name__ == '__main__':
    start_server(main, port=8080)