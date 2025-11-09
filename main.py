from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from ultralytics import YOLO
import threading

class Pokemon(App):
    def build(self):
        self.icon = "32.png"

        # Load the YOLO model (your trained one)
        self.model = YOLO("C:/Users/Emerson/OneDrive/Documents/python/runs/detect/card_yolov8n_run12/weights/best.pt")

        # Main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Add a label and button
        self.status_label = Label(text="Ready to detect Pokémon!", font_size=18)
        layout.add_widget(self.status_label)

        detect_button = Button(text="Start Detection", font_size=20)
        detect_button.bind(on_press=self.start_detection)
        layout.add_widget(detect_button)

        return layout

    def start_detection(self, instance):
        self.status_label.text = "Starting camera detection..."
        
        # Run YOLO in a separate thread to avoid freezing the UI
        threading.Thread(target=self.detect_with_yolo, daemon=True).start()

    def detect_with_yolo(self):
        # Run webcam detection
        results = self.model.predict(source=0, show=True, stream=True)
        for r in results:
            pass  # YOLO handles window display automatically

        self.status_label.text = "Detection stopped."

if __name__ == "__main__":
    Pokemon().run()
