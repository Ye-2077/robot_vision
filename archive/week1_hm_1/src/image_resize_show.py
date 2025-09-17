# Python 2.7 / OpenCV 2.4.11
'''
usage: python image_resize_show.py <image_path> [scale]")
example: python image_resize_show.py ./test.jpg 0.5")

python week1_hm_1/src/image_resize_show.py week1_hm_1/src/assets/LenaRGB.bmp
'''
import cv2
import sys
import numpy as np

def main():
    img_path = sys.argv[1]
    scale = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5

    img = cv2.imread(img_path, 1) #rgb
    if img is None:
        print("load fail: {}".format(img_path))
        return

    h, w = img.shape[:2]
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA if scale < 1.0 else cv2.INTER_LINEAR)

    # add titles
    pad = 6
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.6
    thickness = 1

    orig_title = "Original (%dx%d)" % (w, h)
    resz_title = "Resized (%dx%d)" % (new_w, new_h)

    (_, text_h1), _ = cv2.getTextSize(orig_title, font, font_scale, thickness)
    (_, text_h2), _ = cv2.getTextSize(resz_title, font, font_scale, thickness)
    title_h = max(text_h1, text_h2) + pad * 2
    
    H = max(h, new_h)
    canvas = np.zeros((H + title_h, w + new_w, 3), dtype=img.dtype)
    canvas[0:title_h, :, :] = (220, 220, 220) # light gray background
    canvas[title_h:title_h + h, :w] = img
    canvas[title_h:title_h + new_h, w:w + new_w] = resized

    orig_text_org = (8, pad + text_h1)
    resz_text_org = (w + 8, pad + text_h2)

    LINE_AA = getattr(cv2, 'LINE_AA', getattr(cv2, 'CV_AA', 8))
    cv2.putText(canvas, orig_title, orig_text_org, font, font_scale, (0, 0, 0), thickness + 2, LINE_AA)
    cv2.putText(canvas, orig_title, orig_text_org, font, font_scale, (255, 255, 255), thickness, LINE_AA)
    cv2.putText(canvas, resz_title, resz_text_org, font, font_scale, (0, 0, 0), thickness + 2, LINE_AA)
    cv2.putText(canvas, resz_title, resz_text_org, font, font_scale, (255, 255, 255), thickness, LINE_AA)

    # cv2.imwrite("resized_compare_with_titles.png", canvas)
    cv2.imshow("Compare (Left: Original, Right: Resized)", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE)
    # cv2.namedWindow("Resized", cv2.WINDOW_AUTOSIZE)
    
    # cv2.moveWindow("Original", 50, 50)
    # cv2.moveWindow("Resized",  60 + img.shape[1], 50)

    # cv2.imshow("Original", img)
    # cv2.imshow("Resized", resized)
    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
