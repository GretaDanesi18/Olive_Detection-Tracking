# <strong> Olive_Detection_Tracking </strong>

L'obiettivo è quello di realizzare una rete neurale in grado di eseguire la detection delle olive attraverso l'utilizzo di pseudo labels ovvero labels generate automaticamente da video, cosi da non dover etichettare manualmente le immagini del dataset.
Infatti uno dei limiti delle rete neurali è la creazione di una dataset per ogni specifico problema e il dispendio temporale che ciò comporta.

L'idea è quella di applicare il sistema discusso nel seguente paper ad un nuovo dataset (le olive).

https://openaccess.thecvf.com/content/CVPR2022W/AgriVision/html/Ciarfuglia_Pseudo-Label_Generation_for_Agricultural_Robotics_Applications_CVPRW_2022_paper.html 

All'intero del paper è descritto un sistema in grado di generare pseudo-labels da utilizzare per la detection e la segmentation di grappoli d'uva.
In particolare, la parte del metodo descritta nel paper, che riguarda la detection, il tracking e la generazione di pseudo-labels è contenuta all'interno del seguente repository :

https://github.com/Lio320/GraphTracking.git

# <strong> Struttura repository </strong>

```
dataset_video
    +---frame_video
        +---frame_video1
            +---frame_0001.jpg

            +---frame_000n.jpg

        +---frame_videon
    +---videos
        +---video1.mp4
        +---videon.mp4
```

La cartella videos contiene i file video da cui vengono estratti i frame su cui costruire il proprio dataset.

I frame vengono estratti con il file frame_extraction.py che si può trovare nella cartella utils e poi inseriti nei rispettivi path di frame_video.


```
source_detector
    +---YOLOv5_SDet.ipynb
    +---source_dataset.yaml
    +---dataset_source
```

YOLOv5_SDet.ipynb è un notebook di colab che contiene il codice per la rete YOLO addestrata tramite il dataset source.
Tutti gli step che riguardano il source detector sono illustrati nel file.

dataset_source è un dataset iniziale le cui labels sono state create manualmente tramite il software LabelImg.

source_dataset.yaml è il file yaml della rete YOLO che contiene il path al dataset di train e validation.

```
target_detector
    +---YOLOv5_TDet.ipynb
    +---target_dataset.yaml
    +---test_dataset
            +---images
            +---labels
```

YOLOv5_TDet.ipynb è un notebook di colab che contiene il codice per la rete YOLO addestrata tramite le pseudo_labels.
Tutti gli step che riguardano il target detector sono illustrati nel file.

test_dataset è stato creato da alcuni frame del video2 e viene usato per testare la rete del target detector.

```
frame_extraction.py

checking_labels.py
```

frame_extraction.py viene utilizzato per estrarre i frame dai video.

checking_labels.py viene utilizzato sui risultati della detection (detect.py) del source detector in modo tale da utilizzare solo le immagini con il corrispondente file txt e riordinare i file.

# <strong> Step principali </strong>

* <strong> Eseguire YOLOv5_SDet.ipynb </strong>

* Al termine dell'esecuzione di YOLOv5_SDet.ipynb avremo delle cartelle zip:
    * source_detection_results.zip
    * source_detection_labels.zip
  le quali contengono le immagini e labels ottenute dalla detection effettuata sui frame di video1.

* Estraimo le labels dalla cartella zip e le salvo in una cartella "detection_labels"
* Eseguiamo checking_lables.py cosi da ottenere il dataset di immagini e labels con cui generare le psuedo-labels, per lanciare checking_labels-py basta eseguire il seguente comando

    ```
    python3 checking_labels.py

    ```
* Dopo aver eseguito checking_labels.py otteniamo una directory strutturata in questo modo:

    ```
    dataset_olive
        +--images
        +--labels
    
    ```
  queste directory costituiscono il path image e il path label del file GraphTracking/config/config_features_labels.yaml contenuta nella repo https://github.com/Lio320/GraphTracking.git




