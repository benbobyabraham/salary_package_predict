import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'alcohol':1, 'malic_acid':2, 'ash':3,'alcalinity_of_ash':4,'magnesium':5 ,
'total_phenols':6 ,'flavanoids':7 ,'nonflavanoid_phenols':8 ,'proanthocyanins':9 ,'color_intensity':10,
'hue':11,'od280/od315_of_diluted_wines':12, 'proline':13 })

print(r.json())



  