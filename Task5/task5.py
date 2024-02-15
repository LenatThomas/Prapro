<<<<<<< HEAD
# Nothing Yet
=======
from downloader import Downloader


pqPath = '../Task4/links.parquet'
savePath = '../Task4/Images'

d = Downloader(pq_file = pqPath , saveFolder = savePath)

index = int(input("Enter the index of the image to be downloaded\t: "))
d[index]
d[5:300]
>>>>>>> 954b75e (Completed task5)
