import cv2
import pandas as pd

def calculate_pixel_to_cm_ratio(dots_distance_cm, image_path):
    image = cv2.imread(image_path)
    # Assuming the red dots are annotated, calculate their distance in pixels
    # For now, let's assume you have the coordinates of the red dots
    dot1 = (100, 100)
    dot2 = (500, 500)
    distance_px = ((dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2)**0.5
    return dots_distance_cm / distance_px

def estimate_crab_width(detections_csv, ratio, output_csv):
    df = pd.read_csv(detections_csv)
    df['crab_width_cm'] = df['detections'].apply(lambda x: calculate_crab_width_from_detection(x, ratio))
    df.to_csv(output_csv, index=False)
    print(f"Crab widths saved to {output_csv}")

def calculate_crab_width_from_detection(detection, ratio):
    # Assuming detection contains bounding box data
    bbox_width_px = detection['bbox_width']
    return bbox_width_px * ratio

if __name__ == "__main__":
    ratio = calculate_pixel_to_cm_ratio(10, "data/frame_with_dots.jpg")  # Example value
    estimate_crab_width("data/detections.csv", ratio, "data/crab_widths.csv")
