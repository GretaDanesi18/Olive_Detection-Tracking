## <strong> Olive_Detection_Tracking </strong>

L'obiettivo è quello di realizzare una rete neurale in grado di eseguire la detection delle olive attraverso l'utilizzo di pseudo labels ovvero labels generate automaticamente da video, cosi da non dover etichettare manualmente le immagini del dataset.
Infatti uno dei limiti delle rete neurali è la creazione di una dataset per ogni specifico problema e il dispendio temporale che ciò comporta.

L'idea è quella di applicare il sistema discusso nel seguente paper ad un nuovo dataset (le olive).

https://openaccess.thecvf.com/content/CVPR2022W/AgriVision/html/Ciarfuglia_Pseudo-Label_Generation_for_Agricultural_Robotics_Applications_CVPRW_2022_paper.html 

All'intero del paper è descritto un sistema in grado di generare pseudo-labels da utilizzare per la detection e la segmentation di grappoli d'uva.
In particolare, la parte del metodo descritta nel paper, che riguarda la detection, il tracking e la generazione di pseudo-labels è contenuta all'interno del seguente repository :
https://github.com/Lio320/GraphTracking.git

## <strong> Struttura repository </strong>

```
olive_tracking
    +---ModelText
        +---points3D.txt
        +---images.txt
        +---cameras.txt

    +---olive_tracking_YOLO
        +---images
            +---image1.jpg
            +---image2.jpg
            +---imagen.jpg
        +---labels
            +---label1.txt
            +---label2.txt
            +---labeln.txt
        
    +---olive_tracking_MOT
        +---images
            +---image1.jpg
            +---image2.jpg
            +---imagen.jpg
        +---labels
            +---gt.txt
            +---labels.txt

```
La cartella olive_tracking contiene il materiale necessario ad eseguire il tracking tramite il file <strong> Bboxes_Tracker.py </strong> contenuto all'interno della repo https://github.com/Lio320/GraphTracking.git

In particolare, in ModelText ci sono i file txt generati tramite COLMAP mentre in olive_tracking_YOLO ci sono le labels e le immagini etichettate tramite CVAT per il tracker.


```
dataset_video
    +---frame_video
        +---frame_video1
            +---frame_0001.jpg
            +---frame_0002.jpg
            +---frame_000n.jpg

        +---frame_videon
        
    +---videos
        +---video1.mp4
        +---video2.mp4
```

La cartella videos contiene i file video da cui vengono estratti i frame su cui costruire il proprio dataset.

I frame vengono estratti con il file frame_extraction.py che li inserisce nei rispettivi path di frame_video.

```
source_detector
    +---YOLOv5_SDet.ipynb
    +---source_dataset.yaml
    +---dataset_source
        +---images
            +---image1.jpg
            +---image2.jpg
            +---imagen.jpg
        +---labels
            +---label1.txt
            +---label2.txt
            +---labeln.txt
```

YOLOv5_SDet.ipynb è un notebook di google colab che contiene il codice per la rete YOLOv5 addestrata tramite il dataset source.

Tutti gli step che riguardano il source detector sono illustrati nel file.

dataset_source è un dataset iniziale le cui labels sono state create manualmente tramite il software LabelImg.

source_dataset.yaml è il file yaml della rete YOLO che contiene il path al dataset di train e validation.

```
target_detector
    +---YOLOv5_TDet.ipynb
    +---target_detector_features.yaml
    +---target_detector_Sfm.yaml
    +---pseudo_labels_dataset
        +---images
        +---feature_labels
            +---results_2
                +---labels
            +---results_5
                +---labels
        +---SfmLabels
            +---results_2
                +---labels
            +---results_5
                +---labels

```

YOLOv5_TDet.ipynb è un notebook di colab che contiene il codice per la rete YOLOv5 addestrata tramite le pseudo-labels.

Tutti gli step che riguardano il target detector sono illustrati nel file.

pseudo_labels_dataset contiene i risultati generati dai seguenti file : <strong> Generate_Feature_Labels.py </strong> e <strong> Generate_Sfm_Labels.py </strong>

Il path delle directory di pseudo_labels_dataset costituisce il path result del file GraphTracking/config/config_features_labels.yaml e del file GraphTracking/config/config_sfm_labels.yaml contenuti nella repo https://github.com/Lio320/GraphTracking.git.

```
    +---test_dataset
            +---images
            +---labels
            
```
test_dataset è un dataset composto da alcuni frame del video2 le cui labels sono state create manualmente tramite software LabelImg.

Questo dataset viene usato per testare le due reti di detection.

```
frame_extraction.py
checking_labels.py
```

frame_extraction.py viene utilizzato per estrarre i frame dai video.

checking_labels.py viene utilizzato sui risultati della detection (detect.py) del source detector in modo tale da utilizzare solo le immagini con il corrispondente file txt e riordinare i file.

## <strong> Step principali Detection </strong>

* Eseguire <strong> YOLOv5_SDet.ipynb </strong> 

* Al termine dell'esecuzione di YOLOv5_SDet.ipynb avremo delle cartelle zip:
    * source_detection_results.zip
    * source_detection_labels.zip
  le quali contengono le immagini e labels ottenute dalla detection effettuata sui frame di video1.

* Estraimo le labels dalla cartella zip e le salvo in una cartella "detection_labels"
* Eseguiamo <strong> checking_labels.py </strong> cosi da ottenere il dataset di immagini e labels con cui generare le pseudo-labels, per lanciare checking_labels.py basta eseguire il seguente comando

    ```
    python3 checking_labels.py
    ```
* Dopo aver eseguito checking_labels.py otteniamo una directory strutturata in questo modo:

    ```
    dataset_detection
        +--images
        +--labels
    ```
  queste directory costituiscono il path image e il path label del file GraphTracking/Config/config_features_labels.yaml e del file GraphTracking/config/config_sfm_labels.yaml contenuti nella repo https://github.com/Lio320/GraphTracking.git.

* Eseguiamo <strong> Generate_Feature_Labels.py </strong> per generare pseudo-labels con l'algoritmo di SURF
* Eseguiamo <strong> Generate_Sfm_Labels.py </strong> per generare pseudo-labels con Structure from Motion (SfM)
 
    Per maggiori informazioni sulle creazione di pseudo-labels fare riferimento al README.md della repo https://github.com/Lio320/GraphTracking.git.

* Al termine dell'esecuzione di questi due file otteniamo la cartella pseudo_labels_dataset con cui addestriamo il target detector.
* Eseguiamo <strong> YOLOv5_TDet.ipynb </strong>
* Dopo aver eseguito il target detector possiamo esportare/visualizzare i risultati e trarre le relative conclusioni. 

## <strong> Step principali Tracking </strong>

* Configurare il file GraphTracking/Config/config_track.yaml con i path della directory olive_tracking
* Eseguire il file <strong> Bboxes_Tracking.py </strong> 
* Al termine dell'esecuzione otteniamo le immagini con i bounding box ognuno con il proprio ID. 


N.B Prima di eseguire i file controllare che i path all' interno dei codice corrispondano ai path della propria directory , in caso contrario modificarli.






