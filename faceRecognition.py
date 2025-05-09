import cv2
import face_recognition
import numpy as np

# Load gambar referensi
def load_reference_images():
    known_face_encodings = []
    known_face_names = []
    
    # Contoh: 2 gambar referensi
    reference_images = [
        ("Syafriyadi", "images/me.png"),
        ("Elon Musk", "images/elon.jpg")
    ]
    
    for name, image_path in reference_images:
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(name)
    
    return known_face_encodings, known_face_names

# Inisialisasi
known_face_encodings, known_face_names = load_reference_images()
video_capture = cv2.VideoCapture(0)  # Gunakan webcam

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]  # Konversi BGR ke RGB
    
    # Deteksi wajah
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Bandingkan dengan wajah yang dikenal
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        # Hitung jarak terdekat
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        # YOLO-style bounding box dan label
        box_color = (0, 255, 0)  # Hijau
        text_color = (255, 255, 255)  # Putih
        thickness = 2
        
        # Gambar bounding box
        cv2.rectangle(frame, (left, top), (right, bottom), box_color, thickness)
        
        # Hitung ukuran teks dan background
        font = cv2.FONT_HERSHEY_DUPLEX
        font_scale = 0.8
        text_size = cv2.getTextSize(name, font, font_scale, 1)[0]
        
        # Background label (di dalam box, kiri atas)
        cv2.rectangle(
            frame,
            (left, top),
            (left + text_size[0] + 10, top - text_size[1] - 10),
            box_color,
            cv2.FILLED  # Background solid
        )
        
        # Teks nama
        cv2.putText(
            frame,
            name,
            (left + 5, top - 5),
            font,
            font_scale,
            text_color,
            1,
            cv2.LINE_AA
        )
    
    # Tampilkan hasil
    cv2.imshow('Face Recognition (YOLO Style)', frame)
    
    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()