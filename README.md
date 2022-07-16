# <strong> Olive_Detection_Tracking <strong>

L'obiettivo è quello di realizzare una rete neurale in grado di eseguire la detection delle olive attraverso l'utilizzo di pseudo labels ovvero labels generate automaticamente da video, cosi da non dover etichettare manualmente le immagini del dataset.
Infatti uno dei limiti delle rete neurali è la creazione di una dataset per ogni specifico problema e il dispendio temporale che ciò comporta.

L'idea è quella di applicare il sistema discusso nel seguente paper ad un nuovo dataset.
https://openaccess.thecvf.com/content/CVPR2022W/AgriVision/html/Ciarfuglia_Pseudo-Label_Generation_for_Agricultural_Robotics_Applications_CVPRW_2022_paper.html 

All'intero del paper è descritto un sistema in grado di generare-pseudo labels da utilizzare per la detection e la segmentation di grappoli d'uva.
In particolare, la parte del metodo descritta nel paper, che riguarda la detection, il tracking e la generazione di pseudo-labels è contenuta all'interno del seguente repository : 
https://github.com/Lio320/GraphTracking.git

Questo repository contiene il codice necessario alla detection delle olive e le directory contenenti vari dataset.

