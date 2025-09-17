'''
requirements:
 - python 3.10+
 - numpy-2.2.6 
 - opencv-python-4.12.0.88

 usege: python image_resize_show.py <image_path> [scale]
 example: python image_resize_show.py ./test.jpg 0.5

 python hw_1/image_resize_show.py hw_1/assets/LenaRGB.bmp
 '''

import numpy as np
import cv2
import sys

def main():
    img_path = sys.argv[1]
    try:
        img_original = cv2.imread(img_path, cv2.IMREAD_COLOR) # BGR
    except Exception as e:
        print("Error loading image: {}".format(e))
        return
    # img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB) # convert to RGB
        
    scale = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    h, w = img_original.shape[:2]
    new_width = max(1, int(w * scale))
    new_height = max(1, int(h * scale))
    img_resized = cv2.resize(img_original, (new_width, new_height))

    cv2.imshow(f"Original Image: {h, w}", img_original)
    cv2.imshow(f"Resized Image: {new_height, new_width}", img_resized)

    while True:
        k = cv2.waitKey(20) & 0xFF
        if k in (ord('q'), 27):  # 'q' or Esc
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # python hw_1/image_resize_show.py hw_1/assets/LenaRGB.bmp
    main()

