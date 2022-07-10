import os
import cv2
import subprocess
import shutil


filename1 = 'videos/video1.mp4'
filename2 = 'videos/video2.mp4'

try:
    if not os.path.exists('frame_video'):
        os.mkdir('frame_video')
except OSError:
    print('Errore nella creazione della directory frame_video')


def get_frame_types(video_fn):
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    frame_types = out.replace('pict_type=','').split()
    return zip(range(len(frame_types)), frame_types)

def save_i_keyframes(video_fn):
    frame_types = get_frame_types(video_fn)
    name = video_fn.split('/')[1].split('.')[0]
    print(name)
<<<<<<< HEAD
    print('---------------------------------')
=======
    print('-------------------------')
>>>>>>> 38ec0473e94b13f9a659fa25ba0dc0fe0202a13b
    i_frames = [x[0] for x in frame_types if x[1]=='I']
    if i_frames:
        cap = cv2.VideoCapture(video_fn)
        for frame_no in i_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            ret, frame = cap.read()
            outname = 'frame_video/'+str(name)+'_frame_'+str(frame_no)+'.jpg'
            cv2.imwrite(outname, frame)
            print ('Saved: '+outname)
        cap.release()
    else:
        print ('No I-frames in '+video_fn)

if __name__ == '__main__':
    save_i_keyframes(filename1)
    save_i_keyframes(filename2)

