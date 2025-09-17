# -*- coding: utf-8 -*-
'''
Usage: python ffmpeg_pipe_play.py <video_path> [--fps N]
python ffmpeg_pipe_play.py ./week1_hm_1/src/assets/w5.avi [--fps 30]
'''
import sys
import os
import math
import subprocess
import re
import numpy as np
import cv2

def main():
    path = sys.argv[1]
    fps = None
    if len(sys.argv) >= 4 and sys.argv[2] == '--fps':
        try: fps = float(sys.argv[3])
        except: fps = None

    W, H = 320, 180
    if fps is None:
        try:
            out = subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=r_frame_rate',
                                           '-of','default=nokey=1:noprint_wrappers=1', path]).strip()
            num, den = out.split('/')
            fps = float(num) / float(den) if float(den) != 0 else float(num)
        except:
            fps = 30.0

    cmd = [
        'ffmpeg', '-nostdin', '-loglevel', 'error',
        '-i', path,
        '-vf','scale=320:-2',
        '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-', 
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=10**8)

    frame_bytes = W * H * 3
    delay = int(math.floor(1000.0 / fps))
    cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)
    print("Playing via ffmpeg pipe: %s | %dx%d @ %.2f fps | q/ESC quit" % (path, W, H, fps))

    try:
        while True:
            buf = b''
            while len(buf) < frame_bytes:
                chunk = proc.stdout.read(frame_bytes - len(buf))
                if not chunk:
                    # EOF
                    raise EOFError
                buf += chunk
            frame = np.frombuffer(buf, dtype=np.uint8).reshape((H, W, 3))
            cv2.imshow('Video', frame)
            k = cv2.waitKey(delay) & 0xFF
            if k == 27 or k == ord('q'):
                break
    except EOFError:
        pass
    finally:
        proc.terminate()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
