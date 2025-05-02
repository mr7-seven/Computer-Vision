from ultralytics import YOLO
import cv2

# Load model YOLOv5s
model = YOLO('yolov5n.pt')

# Load gambar
img_path = 'images/me.jpg'

# Deteksi objek
results = model.predict(source=img_path, save=False, verbose=False)

# Ambil gambar yang sudah ada bounding box
annotated_img = results[0].plot()

# Tampilkan manual dengan OpenCV
cv2.imshow('Deteksi Gambar', annotated_img)

# Tunggu sampai tekan 'q' baru keluar
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup semua jendela
cv2.destroyAllWindows()
