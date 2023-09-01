import requests
import csv

csv_file = "data.csv"

requisicao = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=821cf1e1")
movie_data = requisicao.json()

try:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Year", "Rated"])
        writer.writerow([movie_data["Title"], movie_data["Year"], movie_data["Rated"]])
    print("CSV file created successfully!")
except Exception as e:
    print(e)