# Django_test

I've developed this test following [Django Docs](https://docs.djangoproject.com/en/3.2/) for the first part of the test and [Django Rest Framework Docs](https://www.django-rest-framework.org/).

## Intructions

First of all, build and deploy the containers

```bash
docker-compose up --build
```
Then create the database model

```bash
docker-compose -f docker-compose.yml run --rm web python manage.py makemigrations
docker-compose -f docker-compose.yml run --rm web python manage.py migrate
```

To ingest the data from the csv file execute the following command
```bash
docker-compose -f docker-compose.yml run --rm web python manage.py load_work_data --path /works_metadata.csv
```
To run the unit test and see the coverage 
```bash
docker-compose -f docker-compose.yml run --rm web coverage run -m pytest 
docker-compose -f docker-compose.yml run --rm web coverage report -m   
```

You can se all the endpoints going to [API](http://localhost:8000/api/works/) if you want to consult a specific work add the iswc at the end of the url (ej: http://localhost:8000/api/works/T9204649558) if you would like just to get a single field of that work add a query to the end of the url. I added django-restql so you can get a single field in the following way (ej: http://localhost:8000/api/works/T9204649558/?query={contributors})
