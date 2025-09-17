'''
requirements:
 - python 3.10+
 - numpy-2.2.6 
 - opencv-python-4.12.0.88
 '''

import cv2
import numpy as np
import sys

def main():
    video_path = sys.argv[1]

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video")
            break
        cv2.imshow("Video", frame)

        k = cv2.waitKey(30) & 0xFF
        if k in (ord('q'), 27):  # 'q' or Esc
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # python hw_1/video_show.py hw_1/assets/w5.avi
    main()