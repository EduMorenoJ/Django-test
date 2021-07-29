# Django_test

I've developed this test following [Django Docs](https://docs.djangoproject.com/en/3.2/) for the first part of the test and [Django Rest Framework Docs](https://www.django-rest-framework.org/).

It's the first time for me using Django but I've really enjoyed using it and I've found it a really powerful tool that makes really easy the development

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
And that's all! using docker-compose everything becomes easy.

> **Note**: I've not got enough time to develop a really good test suite. But due to this is a test, I think they will be enough to show you my level developing unit tests. Also, I like to use mypy for typing the code, but I didn't do it just to save some time.

## First Part

To test the first part of the test go to your [localhost](http://localhost:8000) and you will see in the index page where the data work cleaned is shown. I've also deployed a simple db client so you can check the data in the postgresql database going to [postgresql]((http://localhost:8080))

> **Note**: I barely know html... so sorry in advance for that ugly design!

Question 1: I've used pandas to clean the code. The strategy that I've followed is grouping by title and iswc, concatenate the contributors and removing the duplicates. As I said before I haven't had enough time to develop a good test suite, and my function is not tested against enough different cases. I know that it works well for the data that you provided my, but I'm not sure what will happen in different scenarios. For example, what would happen if there are two registries with the same title and contributors but different iswc? The answer is always more tests cases!

Question 2: Depend on the way that you receive the data. If the providers left you the data somewhere I would use a microservice to scrap the data from the source. Another option is to tell the clients if they can send the data to a queue, I would implement a microservice to listen that queue and send the data to persist it. If the data is on a database and they give us enough permissions I would consult directly the data from there. Anyway, I would developed a datapipeline using Airflow to configure the data flows. I would get the data depending on the source and I would stored it on a datalake, then I would transform, clean and store it in a datawarehouse and finally I will load all the data on a relational database.

## Second Part

You can se all the endpoints going to [API](http://localhost:8000/api/works/) if you want to consult a specific work add the iswc at the end of the url (ej: http://localhost:8000/api/works/T9204649558) if you would like just to get a single field of that work add a query to the end of the url. If added django-restql so you can get a single field in the following way (ej: http://localhost:8000/api/works/T9204649558/?query={contributors})

Question 1: I think that the response time will increse but I won't be critical. It is not enough amount of data.

Question 2: Setting indexes because them can increase the database performance. Data degfragmentation is another way to increase the database performance or increasing the memory.

