import cv2
import tkinter as tk
from PIL import Image, ImageTk

class FaceDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Detection App")

        # Initialize webcam
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam.")

        # Load cascade classifiers
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

        # Create label for displaying video feed
        self.video_label = tk.Label(root)
        self.video_label.pack(padx=10, pady=10, anchor=tk.CENTER)  # Center the video label

        # Frame for holding buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Buttons for different functionalities
        self.detect_faces_button = tk.Button(button_frame, text="Detect Faces", command=self.detect_faces, bg="blue", fg="white")
        self.detect_faces_button.pack(side=tk.LEFT, padx=10)

        self.detect_eyes_button = tk.Button(button_frame, text="Detect Eyes", command=self.detect_eyes, bg="green", fg="white")
        self.detect_eyes_button.pack(side=tk.LEFT, padx=10)

        self.save_image_button = tk.Button(button_frame, text="Save Image", command=self.save_image, bg="red", fg="white")
        self.save_image_button.pack(side=tk.LEFT, padx=10)

        self.exit_button = tk.Button(button_frame, text="Exit", command=self.close_app, bg="black", fg="white")
        self.exit_button.pack(side=tk.LEFT, padx=10)

        # Variables for face detection information
        self.num_faces = 0

        # Start video feed update
        self.update_video()

    def update_video(self):
        _, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        self.num_faces = len(faces)

        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

            # Display face count on each detected face
            cv2.putText(frame, f"Face {len(faces)}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Convert frame to RGB for displaying in Tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)

        # Update video feed label
        self.video_label.img = img
        self.video_label.config(image=img)
        self.video_label.after(10, self.update_video)

    def detect_faces(self):
        # Update cascade classifier to face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def detect_eyes(self):
        # Update cascade classifier to eye detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    def save_image(self):
        # Capture the current frame and save it as an image file
        _, frame = self.cap.read()
        filename = f"detected_faces_{self.num_faces}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved as: {filename}")

    def close_app(self):
        # Release resources and close the application
        self.cap.release()
        cv2.destroyAllWindows()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetectionApp(root)
    root.mainloop()
