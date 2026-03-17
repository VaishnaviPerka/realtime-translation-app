import tkinter as tk
from tkinter import ttk
from keras.layers import TextVectorization
from tensorflow import keras
import re
import tensorflow.strings as tf_strings
import json
import string
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from keras.utils import pad_sequences
import numpy as np
import tensorflow as tf

# English to Spanish translation
strip_chars = string.punctuation + "¿"
strip_chars = strip_chars.replace("[", "")
strip_chars = strip_chars.replace("]", "")

def custom_standardization(input_string):
    lowercase = tf_strings.lower(input_string)
    return tf_strings.regex_replace(lowercase, f"[{re.escape(strip_chars)}]", "")

# Load the English vectorization layer configuration
with open(r'eng_vectorization_config.json') as json_file:
    eng_vectorization_config = json.load(json_file)

# Recreate the English vectorization layer with basic configuration
eng_vectorization = TextVectorization(
    max_tokens=eng_vectorization_config['max_tokens'],
    output_mode=eng_vectorization_config['output_mode'],
    output_sequence_length=eng_vectorization_config['output_sequence_length']
)

# Apply the custom standardization function
eng_vectorization.standardize = custom_standardization

# Load the Spanish vectorization layer configuration
with open(r'spa_vectorization_config.json') as json_file:
    spa_vectorization_config = json.load(json_file)

# Recreate the Spanish vectorization layer with basic configuration
spa_vectorization = TextVectorization(
    max_tokens=spa_vectorization_config['max_tokens'],
    output_mode=spa_vectorization_config['output_mode'],
    output_sequence_length=spa_vectorization_config['output_sequence_length'],
    standardize=custom_standardization
)

# Load and set the English vocabulary
with open(r'eng_vocab.json') as json_file:
    eng_vocab = json.load(json_file)
    eng_vectorization.set_vocabulary(eng_vocab)

# Load and set the Spanish vocabulary
with open(r'spa_vocab.json') as json_file:
    spa_vocab = json.load(json_file)
    spa_vectorization.set_vocabulary(spa_vocab)

# Load the Spanish model
transformer = keras.layers.TFSMLayer('Transformer_model')


spa_index_lookup = dict(zip(range(len(spa_vocab)), spa_vocab))
max_decoded_sentence_length = 20

def beam_search_decode(input_sentence, beam_width=3, max_len=50):
    tokenized_input_sentence = eng_vectorization([input_sentence])
    start_token_index = spa_vocab.index('[start]')
    end_token_index = spa_vocab.index('[end]')
    
    # Initialize the beam with the start token
    beams = [([start_token_index], 0.0)]  # List of tuples (sequence, score)
    for _ in range(max_len):
        all_candidates = []
        for seq, score in beams:
            tokenized_target_sentence = tf.expand_dims(seq, axis=0)
            predictions = transformer([tokenized_input_sentence, tokenized_target_sentence])
            top_k_indices = tf.math.top_k(predictions[0, -1, :], k=beam_width).indices.numpy()
            top_k_probs = tf.math.top_k(predictions[0, -1, :], k=beam_width).values.numpy()
            for idx, prob in zip(top_k_indices, top_k_probs):
                candidate = (seq + [idx], score - np.log(prob))
                all_candidates.append(candidate)
        # Select the top k sequences with the highest scores
        ordered = sorted(all_candidates, key=lambda tup: tup[1])
        beams = ordered[:beam_width]
        # Check if any beam sequence has ended with the end token
        if any(seq[-1] == end_token_index for seq, _ in beams):
            break
    
    # Select the sequence with the highest score
    best_seq = beams[0][0]
    decoded_sentence = " ".join([spa_index_lookup[idx] for idx in best_seq if idx != start_token_index])
    return decoded_sentence

def translate_to_spanish(english_sentence):
    spanish_sentenceb = beam_search_decode(english_sentence)
    return spanish_sentenceb.replace("[start]", "").replace("[end]", "")

# Function to handle translation request based on selected language
def handle_translate():
    english_sentence = text_input.get("1.0", "end-1c")
    translation = translate_to_spanish(english_sentence)
    
    translation_output.delete("1.0", "end")
    translation_output.insert("end", f"Spanish translation: {translation}")

# Setting up the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("550x600")

# Font configuration
font_style = "Times New Roman"
font_size = 14

# Frame for input
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Heading for input
input_heading = tk.Label(input_frame, text="Enter the text to be translated", font=(font_style, font_size, 'bold'))
input_heading.pack()

# Text input for English sentence
text_input = tk.Text(input_frame, height=5, width=50, font=(font_style, font_size))
text_input.pack()

# Submit button
submit_button = ttk.Button(root, text="Translate", command=handle_translate)
submit_button.pack(pady=10)

# Frame for output
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

# Heading for output
output_heading = tk.Label(output_frame, text="Translation: ", font=(font_style, font_size, 'bold'))
output_heading.pack()

# Text output for translations
translation_output = tk.Text(output_frame, height=10, width=50, font=(font_style, font_size))
translation_output.pack()

# Running the application
root.mainloop()
