
# Hand Gesture Controlled 2048 Game

## Introduction
This Python program allows the user to play the popular sliding block puzzle game, 2048, using hand gestures. By leveraging OpenCV for video capture and processing, and MediaPipe for hand landmark detection, users can control the game by moving their index finger in the desired direction of the tiles' movement.

## Prerequisites
Before you start, ensure you have the following installed on your system:
- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the Repository**
   
   First, clone this repository to your local machine using Git.

   ```sh
   git clone <repository-url>
   ```

2. **Install Required Libraries**

   Navigate to the cloned repository's directory and install the required Python libraries using pip.

   ```sh
   pip install opencv-python mediapipe selenium webdriver-manager
   ```

3. **ChromeDriver**

   The Selenium WebDriver requires ChromeDriver to interact with the Chrome browser. The script automatically manages ChromeDriver installations using `webdriver-manager`, so there's no need for manual setup.

## How to Run

1. **Open Terminal**

   Open a terminal and navigate to the project's directory.

2. **Run the Script**

   Execute the Python script to start the game.

   ```sh
   python main.py
   ```

## Usage

- **Starting the Game**: Once the script is running, it will automatically open the game in a new Chrome browser window and start the webcam feed in a separate window.
  
- **Playing the Game**: Move your index finger within the webcam's field of view to control the game. The direction of your finger's movement will dictate the tiles' movement in the game:
  - Move your finger to the **left** to swipe left.
  - Move your finger to the **right** to swipe right.
  - Move your finger **up** to swipe up.
  - Move your finger **down** to swipe down.

- **Quitting the Game**: To quit, press 'q' in the webcam feed window. This will close the webcam feed and the Chrome browser window, ending the game session.

## Note

This project is for educational purposes and demonstrates the use of computer vision and web automation technologies to interact with web-based applications in a novel way.

## Contributions

Contributions to this project are welcome! If you have improvements or bug fixes, please feel free to fork the repository and submit a pull request. Your contributions can help make this project even better.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more information.

