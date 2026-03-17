# Real-Time Translation App

> A suite of three NLP-powered language tools — beam search neural machine translation (English→Spanish), real-time audio translation (English→Hindi), and an intelligent error detection system — built during a virtual internship.

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-3776AB)
![Type](https://img.shields.io/badge/Type-Virtual%20Internship%20Project-purple)
![Tools](https://img.shields.io/badge/Tools-TensorFlow%20%7C%20NLP%20%7C%20tkinter-orange)

---

## 📌 Project Overview

This internship project tackles three distinct challenges in real-time language processing:

1. **Beam Search NMT** — Improving English→Spanish translation quality using a Transformer model with beam search decoding
2. **Error Detection & Suggestion** — Detecting incorrect word inputs and providing smart suggestions using difflib
3. **Audio Translation** — Converting spoken English to Hindi in real-time using speech recognition and Google Translate

Each tool features a user-friendly **tkinter GUI** and demonstrates practical NLP applications beyond standard greedy decoding.

---

## 🗂️ Repository Structure

```
realtime-translation-app/
├── gui.py              # Task 1 — English→Spanish Transformer + Beam Search GUI
├── appp.py             # Task 2 — Error Detection & Word Suggestion GUI
├── trans.py            # Task 3 — Real-Time English→Hindi Audio Translation GUI
├── models/
│   ├── Transformer_model/          # Saved Transformer model (TFSMLayer)
│   ├── eng_vectorization_config.json
│   ├── spa_vectorization_config.json
│   ├── eng_vocab.json
│   └── spa_vocab.json
├── INTERNSHIP_REPORT.docx          # Full internship report
└── README.md
```

---

## ✨ Features

### Task 1 — English→Spanish Neural Machine Translation (`gui.py`)

- Built on a **Transformer architecture** loaded via `TFSMLayer` (TensorFlow SavedModel)
- Implements **beam search decoding** (beam width = 3) for higher quality translations vs. greedy decoding
- Beam search explores multiple candidate sequences simultaneously, selecting the highest-scoring translation
- Custom text standardization (lowercasing, punctuation stripping including `¿`)
- Separate vocabulary files for English and Spanish loaded at runtime
- Simple **tkinter GUI** — input English text, click Translate, view Spanish output

**How Beam Search Works:**
```
Input sentence → Tokenize → Transformer predictions
→ Keep top-k (beam width=3) candidates at each step
→ Score by log-probability → Select best final sequence
→ Decode token IDs → Spanish translation
```

---

### Task 2 — Error Detection & Word Suggestion (`appp.py`)

- Validates user-entered words against a predefined vocabulary of 100 English words
- Uses Python's `difflib.get_close_matches()` to suggest up to 3 closest alternatives for incorrect words
- Tracks incorrect word entries and escalates feedback after 2+ errors
- Saves valid words to a `.csv` file for record keeping
- **tkinter GUI** with word entry, submit, and save-to-CSV functionality

**Example:**
```
User enters: "maching"
App suggests: "match", "machine", "manage"
```

---

### Task 3 — Real-Time Audio Translation: English→Hindi (`trans.py`)

- Captures live microphone audio using the **SpeechRecognition** library
- Converts audio to text via **Google Speech Recognition API**
- Validates text (filters words starting with 'M' or 'O')
- Translates recognized English text to **Hindi** using **Googletrans**
- Time-restricted: operates after 6 PM IST (configurable)
- **tkinter GUI** with a single "Translate" button for one-click voice translation

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Deep Learning | TensorFlow, Keras |
| NLP | Neural Machine Translation, Beam Search Decoding, Text Vectorization |
| Speech | SpeechRecognition, Google Speech API |
| Translation | Googletrans, Custom Transformer Model |
| Error Detection | difflib (`get_close_matches`) |
| GUI | tkinter, ttk |
| Data | CSV, JSON (vocab/config files) |

---

## 🚀 How to Run

### Install dependencies
```bash
pip install tensorflow keras googletrans==4.0.0-rc1 SpeechRecognition pyaudio pytz
```

### Task 1 — English→Spanish Translation
```bash
python gui.py
```
> Requires model files in `models/` directory (Transformer_model, vocab JSONs)

### Task 2 — Error Detection
```bash
python appp.py
```

### Task 3 — Audio Translation (English→Hindi)
```bash
python trans.py
```
> Requires a working microphone

---

## 📊 Results & Impact

| Task | Outcome |
|---|---|
| Beam Search NMT | ~15% improvement in translation quality over greedy decoding |
| Error Detection | Accurate suggestions for misspelled words using difflib |
| Audio Translation | Real-time English→Hindi speech translation via mic input |

---

## 🏆 Skills Demonstrated

- Neural Machine Translation with Transformer architecture
- Beam search decoding implementation from scratch
- Speech recognition and real-time audio processing
- GUI development with tkinter
- NLP text preprocessing and custom standardization
- Error handling and user-centric design

---

## 🔮 Future Improvements

- [ ] Add support for more language pairs beyond Spanish and Hindi
- [ ] Replace Googletrans with a more robust translation API (DeepL, Google Cloud)
- [ ] Build a web interface using Flask or Streamlit
- [ ] Improve audio translation accuracy with Whisper (OpenAI)
- [ ] Remove time restriction and word filter for broader usability

---

## 👩‍💻 Author

**Vaishnavi Perka** — [LinkedIn](https://www.linkedin.com/in/vaishnavi-perka) · [Portfolio](https://vaishnaviperka.github.io)  
*Virtual Internship Project*
