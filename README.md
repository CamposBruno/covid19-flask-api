## covid19-flask-api | data source: coronadatascraper.com

A React repository consuming the api can be found [here](https://github.com/CamposBruno/covid19-react)

## Run

You can run with docker (recomended) 
````[python]
docker build -t covid19-flask-api .
docker run -p 5000:5000
````
Or you can install dependencies and run in command line with python
````[bash]
pip install Flask flask_cors pandas
python server.py
`````

Pull Requests are welcomed
