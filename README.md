# Sign Language Phrase Recognition (MVP) 🤟

A real-time sign language recognition system developed for the **2024 Solution Challenge**. This project uses computer vision and machine learning to bridge the communication gap for the deaf and hard-of-hearing community.

## 🚀 Overview
This prototype detects hand gestures via webcam, translates them into text keywords, and stabilizes them into phrases. It is designed to eventually integrate with **Google Gemini** for natural language smoothing.

## 🛠️ Tech Stack
*   **Language:** Python 3.9+
*   **Computer Vision:** MediaPipe, OpenCV
*   **Machine Learning:** Scikit-learn (Random Forest/SVM)
*   **Planned:** Google Gemini Pro API, Google Cloud Run

## ⚙️ Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe scikit-learn
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## 🎮 How to Use
*   **Sign Detection:** Hold a sign steady for **1.5 seconds** to add it to the sentence.
*   **Clear Text:** Press the **'C'** key to clear the current phrase.
*   **Exit:** Press **'ESC'** to close the application.

## 🔮 Future Roadmap
*   **Gemini Integration:** Passing raw keywords to Gemini Pro for grammatical sentence construction.
*   **Cloud Deployment:** Migrating the local engine to **Google Cloud Run** for web access.
*   **TTS:** Adding Text-to-Speech for audible communication.

## 🤖 Google AI Integration (Planned Phase)
An AI layer using Google Gemini Pro is prepared to connect "Signed Keywords" and natural human speech.

*   **File:** `future_ai_layer.py`
*   **Purpose:** This module is designed to use Gemini’s Large Language Model (LLM) capabilities to generate fluent sentences (e.g., *"I would like something to eat."*) from the raw, stabilized text from the CV engine (e.g., *"FOOD WANT ME"*).
*   **Status:** The logic is mapped out in the repository and will be fully integrated using the **Google Generative AI SDK** in the production build.
