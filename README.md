# realtime-translation-app
Real-time English↔Spanish/Hindi translation using NLP and beam search
# Real-Time Translation App

> A real-time NLP translation application for English↔Spanish and English↔Hindi using beam search decoding — improving translation quality by ~15%.

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20NLP%20%7C%20Beam%20Search-orange)

---

## 📌 Project Overview

Developed during a virtual internship, this application provides real-time bidirectional translation between English–Spanish and English–Hindi. The system uses NLP techniques with beam search decoding to improve translation fluency, along with built-in error detection and suggestion logic to enhance accuracy.

---

## 🎯 Objectives

- Build a **real-time translation system** for two language pairs
- Implement **beam search decoding** to improve translation quality over greedy approaches
- Develop **error detection and suggestion logic** to catch and correct mistranslations
- Achieve measurable improvement in translation quality (~15% over baseline)

---

## 🧠 Technical Approach

### Why Beam Search?
Unlike greedy decoding (which picks the single best token at each step), beam search maintains multiple candidate sequences simultaneously. This leads to more fluent, contextually accurate translations — especially for longer or more complex sentences.

### Error Detection Logic
- Detects out-of-vocabulary tokens and proposes closest matches
- Flags low-confidence translations for user review
- Suggests alternative phrasings when ambiguity is detected

---

## 📊 Results

| Metric | Baseline | With Beam Search |
|---|---|---|
| Translation Quality | — | ~15% improvement |
| Language Pairs | English↔Spanish, English↔Hindi | ✅ |
| Error Detection | None | ✅ Implemented |

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| NLP | Tokenization, sequence modeling |
| Decoding | Beam search algorithm |
| Error Handling | Custom suggestion logic |
| Environment | Jupyter Notebook |

---

## 📁 Repository Structure

```
realtime-translation-app/
├── src/
│   ├── translator.py             # Core translation engine
│   ├── beam_search.py            # Beam search decoder
│   ├── error_detector.py         # Error detection & suggestions
│   └── app.py                    # Main application entry point
├── models/
│   └── model_weights/            # Pre-trained model weights
├── notebooks/
│   └── translation_demo.ipynb    # Demo notebook
├── tests/
│   └── test_translations.py      # Sample test cases
└── README.md
```

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/VaishnaviPerka/realtime-translation-app.git
cd realtime-translation-app

# Install dependencies
pip install -r requirements.txt

# Run the app
python src/app.py
```

---

## 🔮 Future Improvements

- [ ] Add support for additional language pairs
- [ ] Build a web interface with Flask or Streamlit
- [ ] Integrate with a pre-trained transformer model (e.g., Helsinki-NLP)
- [ ] Add pronunciation guide for translated output

---

## 👩‍💻 Author

**Vaishnavi Perka** — [LinkedIn](https://www.linkedin.com/in/vaishnavi-perka) · [Portfolio](https://vaishnaviperka.github.io)
