
import os
import cv2

file_path_1 = "../Olive_Detection_Tracking/dataset_video/videos/video1.mp4"
file_path_2 = "../Olive_Detection_Tracking/dataset_video/videos/video2.mp4"


def frame_extraction(video_name):
    file_name = video_name.split('/')[4].split('.')[0]
    path = '../Olive_Detection_Tracking/dataset_video/frame_video/frame_'+file_name
    try:
        if os.path.exists(path):
            print("La cartella già esiste")
            
        elif not os.path.exists(path):
            os.makedirs(path)

    except OSError:
        print("Errore nella creazione della cartella "+path)
        exit()     

    num_frame = 1
    vid = cv2.VideoCapture(video_name)

    while (True):

        success, frame = vid.read()
        print(success)

        if success:
            
            name = path+'/'+'frame_'+str(num_frame).zfill(4)+'.jpg'
            print('Creazione di: '+ name)
            cv2.imwrite(name,frame)
            num_frame += 1
        else:
            break
    vid.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    frame_extraction(file_path_1)
    frame_extraction(file_path_2)



