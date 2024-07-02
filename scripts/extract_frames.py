import cv2
import os

def extract_unique_frames(video_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    unique_frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % 30 == 0:  # Extract every 30th frame as an example
            frame_path = os.path.join(output_dir, f"frame_{unique_frame_count:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            unique_frame_count += 1
    
    cap.release()
    print(f"Extracted {unique_frame_count} unique frames.")

if __name__ == "__main__":
    extract_unique_frames("data/video.mp4", "data/frames")
