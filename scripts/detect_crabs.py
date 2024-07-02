import cv2
import pandas as pd
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

def detect_crabs_in_frames(api_key, endpoint, project_id, model_name, frames_dir, output_csv):
    credentials = ApiKeyCredentials(in_headers={"Prediction-key": api_key})
    predictor = CustomVisionPredictionClient(endpoint, credentials)
    
    results = []
    
    for frame_file in os.listdir(frames_dir):
        frame_path = os.path.join(frames_dir, frame_file)
        with open(frame_path, "rb") as image_data:
            results.append({
                "frame": frame_file,
                "detections": predictor.classify_image(project_id, model_name, image_data).predictions
            })
    
    pd.DataFrame(results).to_csv(output_csv, index=False)
    print(f"Detection results saved to {output_csv}")

if __name__ == "__main__":
    detect_crabs_in_frames("YOUR_API_KEY", "YOUR_ENDPOINT", "YOUR_PROJECT_ID", "YOUR_MODEL_NAME", "data/frames", "data/detections.csv")
