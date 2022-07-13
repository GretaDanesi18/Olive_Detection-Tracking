import os
import shutil

def checking_labels(dir_name):
    path_frame = dir_name
    path_labels ='labels'
    path_image = 'images'


    try:
        if not os.path.exists(path_image):
            os.mkdir(path_image)
        elif os.path.exists(path_image):
            print("La cartella già esiste")
    except OSError:
        print("Errore nella creazione della cartella")
        exit()


    lista_frames = os.listdir(path_frame)
    lista_labels = os.listdir(path_labels)

    for frames in lista_frames:
        print(frames)
        name = frames.split('.')[0]
        print(name)
        file_txt = name+'.txt'
        print(file_txt)

        for labels in lista_labels:
            if labels == file_txt:
                source = path_frame+'/'+frames
                destination = path_image+'/'+frames
                shutil.copyfile(source,destination)

if __name__ == '__main__':  
    checking_labels('frame_video1')


