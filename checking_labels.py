

from asyncore import write
import os
import cv2

#modificare i path in base alle proprie directory

def checking_labels(dir_name):
    path_frame = dir_name
    path_labels ='labels'
    path_image = 'dataset_olive_70/images'
    path_new_labels = 'dataset_olive_70/labels' 


    try:
        if not os.path.exists(path_image):
            os.makedirs(path_image)
    except OSError:
        print("Errore nella creazione della cartella")
        exit()

    try:
        if not os.path.exists(path_new_labels):
            os.makedirs(path_new_labels)
    except OSError:
        print("Errore nella creazione della cartella")
        exit()


    lista_frames = sorted(os.listdir(path_frame))
    #print(lista_frames)
    lista_labels = sorted(os.listdir(path_labels))
    #print(lista_labels)
    num= 1


    for labels in lista_labels:
        #print(labels)
        name = labels.split('.')[0]
        #print(name)
        file_jpg = name+'.jpg'
        #print(file_jpg)

        for frames in lista_frames:
            #print(frames)
            if frames == file_jpg:

                source_txt = path_labels+'/'+labels
                #print(source_txt)
                file_read= open(source_txt, "r").read()
                print(file_read)
                num_righe= len(open(source_txt, "r").readlines())

                destination_txt = path_new_labels+'/'+'frame_'+str(num).zfill(4)+'.txt'
                print(destination_txt)
                file_write = open(destination_txt, 'w')
                file_write.write(file_read)
                print('Label '+str(num).zfill(4)+' copiata')

                source_img = path_frame+'/'+frames
                #print(source_img)
                img = cv2.imread(source_img)
                #print(img)
                destination_img = path_image+'/'+'frame_'+str(num).zfill(4)+'.jpg'
                #print(destination_img)
                cv2.imwrite(destination_img,img)
                print('Immagine '+str(num).zfill(4)+' copiata')
            
            
                num +=1
                

if __name__ == '__main__':  
    checking_labels('frame_video1')
