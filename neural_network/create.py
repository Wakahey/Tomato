from ultralytics import YOLO

# Load a model
model = YOLO('yolov8s-cls.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='caltech101', epochs=20, imgsz=640)