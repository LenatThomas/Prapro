import requests 
import pyarrow.parquet as pq
import numpy as np
import os


class Downloader :
    
    def __init__(self , pq_file : str , saveFolder : str) -> None:
        self.file = pq_file
        table = pq.read_table(pq_file)
        self.urls = np.array(table['URL']).flatten()
        self.saveFolder = saveFolder


    def downloadImage(self , index) :
        try :
            response = requests.get(self.urls[index])

            if response.status_code == 200 :
                filename = os.path.basename(self.urls[index])
                imagePath = os.path.join(self.saveFolder , filename)
                with open(imagePath , 'wb') as img :
                    img.write(response.content)
                print(f"Downloaded : {filename}")
        except Exception as e :
            print(f"Error {e} for {self.urls[index]}")





    def __getitem__(self , key) :


        if isinstance(key , int) :
            self.downloadImage(key)

        elif isinstance(key , slice) :


            start , stop ,step = key.indices(len(self.urls))

            for i in range(start , stop , step) :

                self.downloadImage(i)

        else :
            raise TypeError('Invalid Index')
        