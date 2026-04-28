import cv2
import mediapipe as mp
import pickle
import time

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Convert landmarks to model input
def extract_features(landmarks):
    data = []
    for lm in landmarks:
        data.extend([lm.x, lm.y, lm.z])
    return data

# Camera
cap = cv2.VideoCapture(0)

# FULLSCREEN WINDOW
window_name = "Sign Language Phrase Recognition"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

text_output = ""
last_prediction = ""
start_time = time.time()

# NEW: track last time text was updated
last_text_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1920, 1080))

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            features = extract_features(handLms.landmark)

            prediction = model.predict([features])[0]

            # Stabilize prediction
            if prediction == last_prediction:
                if time.time() - start_time > 1.5:
                    text_output += prediction + " "
                    start_time = time.time()

                    # UPDATE last text time
                    last_text_time = time.time()
            else:
                last_prediction = prediction
                start_time = time.time()

            cv2.putText(frame, f"Current: {prediction}", (20, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # NEW: Clear text after 5 seconds of inactivity
    if time.time() - last_text_time > 5:
        text_output = ""

    # Display sentence bar
    cv2.rectangle(frame, (10, 10), (1900, 80), (0, 0, 0), -1)
    cv2.putText(frame, text_output, (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow(window_name, frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC
        break
    elif key == ord('c'):  # Clear manually
        text_output = ""

cap.release()
cv2.destroyAllWindows()
