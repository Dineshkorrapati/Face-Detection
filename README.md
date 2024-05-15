# Face-Detection

**Dependencies:**

- cv2 (OpenCV): Used for capturing video from the webcam, processing frames, and performing face and eye detection.
- tkinter: Provides the GUI framework for creating the application window and UI elements.
- PIL (Pillow): Utilized for converting OpenCV image frames to a format compatible with Tkinter.

**'**FaceDetectionApp'** Class**
This class represents the main application.

**__init__(self, root): Initializes the application.**

- Sets up the Tkinter window (root).
- Opens the webcam (cv2.VideoCapture) for capturing video.
- Loads Haar cascade classifiers for face and eye detection.
- Creates GUI elements (video label for displaying the webcam feed and buttons for different functionalities).
- update_video(self): Continuously updates the video feed displayed in the Tkinter label (self.video_label) by:


**Reading frames from the webcam.**

- Converting the frame to grayscale for face detection.
- Detecting faces using self.face_cascade.detectMultiScale() and drawing rectangles around detected faces.
- Converting the frame to RGB format compatible with Tkinter and updating the video label.
- detect_faces(self): Switches the cascade classifier to detect faces by updating self.face_cascade to the face detection cascade.

**detect_eyes(self): Switches the cascade classifier to detect eyes by updating self.face_cascade to the eye detection cascade.

**save_image(self): Captures the current frame from the webcam and saves it as an image file (detected_faces_{num_faces}.jpg), where num_faces is the count of detected faces.**

**close_app(self): Releases the webcam resources and closes the application.**

**Main Execution**
The if __name__ == "__main__": block initializes the Tkinter application (root) and creates an instance of FaceDetectionApp. It then starts the main event loop (root.mainloop()) to run the application.

**How to Use**
To use this code:

Ensure you have the required libraries (opencv-python, Pillow, tkinter).
Run the script.
The GUI will display with options to detect faces, eyes, save images, and exit.
