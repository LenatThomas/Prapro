import requests 
import pyarrow.parquet as pq
import numpy as np
import os

table = pq.read_table('links.parquet')
columns = table.column_names

urls = np.array(table['URL']).flatten()
names = np.array(table['TEXT']).flatten()

def downloadImage(url , path) :
    try :
        
        response = requests.get(url)
        
        if response.status_code == 200 :
            
            filename = os.path.basename(url)
            imagePath = os.path.join(path , filename)
            
            with open(imagePath , 'wb') as img :
                img.write(response.content)
            
            print(f"Downloaded : {filename}")



    except Exception as e :
        print(f"Error {e} for {url}")


currentDirectory = os.getcwd()
folder = 'Images'
savePath = os.path.join(currentDirectory , folder)
os.makedirs(folder , exist_ok = True)
print(savePath)

for i in range(10000) :
    downloadImage(urls[i] , savePath)


    