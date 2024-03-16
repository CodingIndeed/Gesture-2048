import cv2
import mediapipe as mp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Mediapipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize the Chrome driver with options if needed
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open the 2048 game
driver.get("https://play2048.co/")
time.sleep(10)
body = driver.find_element(By.TAG_NAME, "body")
time.sleep(5)

# Initialize the video capture object
cap = cv2.VideoCapture(0)
prev_tip_position = None

def calculate_direction(prev_tip_position, current_tip_position):
    if prev_tip_position is None or current_tip_position is None:
        return
    dx = current_tip_position[0] - prev_tip_position[0]
    dy = current_tip_position[1] - prev_tip_position[1]
    if abs(dx) > abs(dy):
        if dx > 60:
            body.send_keys(Keys.LEFT)
            print("Swipe Left")
            print(dx)
        elif dx < -60:
            body.send_keys(Keys.RIGHT)
            print("Swipe Right")
            print(dx)
    else:
        if dy > 60:
            body.send_keys(Keys.DOWN)
            print("Swipe Down")
            print(dy)
        elif dy < -60:
            body.send_keys(Keys.UP)
            print("Swipe Up")
            print(dy)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand detection
    results = hands.process(frame_rgb)

    # Check if the 'multi_hand_landmarks' attribute exists in 'results'
    if hasattr(results, 'multi_hand_landmarks') and results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Focus on the tip of the index finger, landmark 8
            tip_of_index = hand_landmarks.landmark[8]
            current_tip_position = (int(tip_of_index.x * frame.shape[1]), int(tip_of_index.y * frame.shape[0]))

            if prev_tip_position is not None and current_tip_position is not None:
                calculate_direction(prev_tip_position, current_tip_position)

            prev_tip_position = current_tip_position

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
driver.quit()
