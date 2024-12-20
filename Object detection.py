import cv2
from ultralytics import YOLO

# Load the pre-trained YOLOv8 model from ultralytics package
model = YOLO('yolov8n.pt')  # You can choose yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt based on your needs
# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)

    # Draw bounding boxes and labels on the frame
    for result in results:
        boxes = result.boxes  # Get the bounding boxes
        for box in boxes:
            # Extract bounding box coordinates, confidence, and class ID
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = box.cls[0]
            label = model.names[int(cls)]
            confidence = f'{conf:.2f}'

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Draw label and confidence
            cv2.putText(frame, f'{label} {confidence}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('YOLOv8 Object Detection', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()