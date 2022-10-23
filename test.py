from scrapping.scrapper import scrap_inegi,scrap_maps,scrap_pyme_org
import csv
import codecs 
import pandas as pd
import json


def upload():
    with open('Final_Data_Hackathon_2022.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
        data = {}
        for rows in csv_reader:             
            key = rows['Index']  # Assuming a column named 'Index' to be the primary key
            data[key] = rows  
        
        # file.file.close()
        for datum in data:
            data[datum].update({'Estrato':scrap_inegi(data[datum]['NombComp'][:-10])[0]})
            data[datum].update({'Registro':scrap_pyme_org(data[datum]['NombComp'][:-10], data[datum]['Estado'])})
            # data[datum].update({'Reviews':scrap_maps(data[datum]['Direccion1']+data[datum]['Direccion2']+data[datum]['Direccion3']+data[datum]['Colonia']+data[datum]['CP'])})

        print(data)

        json_object = json.dumps(data, indent=4)
        
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

        df = pd.read_json (r'sample.json')
        df.to_csv (r'new_dataset.csv', index = None)

        return data 

upload()