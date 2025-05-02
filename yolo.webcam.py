from ultralytics import YOLO
import cv2

# Load model YOLOv5
model = YOLO('yolov5n.pt')

# Buka webcam (0 = default webcam)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi objek
    results = model.predict(source=frame, save=False, conf=0.5, verbose=False)

    # Ambil frame dengan bounding box hasil deteksi
    annotated_frame = results[0].plot()

    # Tampilkan
    cv2.imshow('YOLOv5 Deteksi Webcam', annotated_frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Beres, tutup semua
cap.release()
cv2.destroyAllWindows()
