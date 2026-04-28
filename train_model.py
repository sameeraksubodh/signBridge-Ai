import os
import cv2
import mediapipe as mp
import pickle
from sklearn.ensemble import RandomForestClassifier

DATA_DIR = r"C:\Users\ASUS\OneDrive\Desktop\vscode\phrases"

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True)

data = []
labels = []

for label in os.listdir(DATA_DIR):
    path = os.path.join(DATA_DIR, label)

    for img_name in os.listdir(path):
        img_path = os.path.join(path, img_name)

        img = cv2.imread(img_path)
        if img is None:
            continue

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                row = []
                for p in handLms.landmark:
                    row.extend([p.x, p.y, p.z])

                data.append(row)
                labels.append(label)

print("Samples collected:", len(data))

# Train model
model = RandomForestClassifier()
model.fit(data, labels)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model saved as model.pkl")
