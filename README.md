# Works_Single_View_app

Works_Single_View_app aggregates and reconciles data(musical work) from multiple sources to create a single view of an entity. The app takes metadata.csv as the input files, checks for duplicates as the result is stored in the database.

### Installation and Setup.
Git clone:

 ```
 https://github.com/r-wambui/Works_Single_View_app.git
 ```

Navigate to the root directory:

```
cd  path/to/Works_Single_View_app
```

Install the requirements

```
pip install -r requirements.txt
```

Run the app`(Part 1)`

```
python manage.py migrate
python manage.py music_works
```

Run the api `(Part 2)`

```
python manage.py runserver
```

### Setup on a Docker environment.
Ensure you have `docker` and `docker-compose` installed.

Build the docker images

```
make build
```

Run migrate in the docker container
```
make migrate
```

Run `PART 1` of the project
```
make seed
```

Run the api`(PART 2)`
```
make start
```
Shut down the running container
```
make down
```

Notice we have `make makemigrations` on the `Makefile`, run this incase you made any changes to the models.

For Running part 1: 
Create a `data` directory on the root folder, add the `works_metadata.csv`

### Local Database
Ensure you have postgres installed, create a database `db_name`. Create `.env` file at the root directory
```
export DBNAME='db_name'
export USER='postgres'
export PASSWORD=''
export HOST='localhost' # change this to 'db' when working with docker.
export PORT='5432'
```

### API endpoint
Get music metadata by `iswc`. After running Part 2 above. You can use the endpoint on browser or postman to get the response.

endpoint:
`http://127.0.0.1:8000/api/v1/musicworks/<str:iswc>`

```json
{
    "id": 2,
    "iswc": "T0101974597",
    "title": "Adventure of a Lifetime",
    "contributors": [
        "O Brien Edward John",
        "Yorke Thomas Edward",
        "Greenwood Colin Charles",
        "Selway Philip James"
    ]
}

```


