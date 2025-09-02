# Star Wars Database
A RESTful API based on SWAPI.

The current project is an async FastAPI API with PostgreSQL as the database.

It uses poetry for dependencies management.

The PostgreSQL is run through a docker container.

The starships entity was left aside as the logic is the same with the other entities (Characters and Films).

Error handling is at a basic level, while unit testing is absent, as the time required to invest was more than my everyday free time.

Documentation is through Swagger, created automatically from FastAPI at /docs endpoint.

The main functionality consists of 3 asynchronous endpoints for each entity:
* fetch all data from SWAPI and store them in out local DB, while associating the entities based on their many-to-many relationships.
* get all data for each entity from the DB
* search by some provided filters. As requested only the name param is set-up, but the code is easily extended.

Unfortunately, the endpoints need some refinement and are not fully functional. 

However, the structure is solid and fully extendable. We use repository pattern, separation of concerns, dependency injection, versioned Pydantic schemas and routes, internal DTOs for decoupling servicers from schemas, and generally adheres closely to SOLID principles.

To run the API you need Docker running and poetry.

First run in terminal `poetry install` to install the dependencies.

Then, with docker running run 
`docker-compose up -d`.

Finally, run `poetry run uvicorn swdb_app.main:app --reload` to run the FastAPI server.

You then can make calls like so `POST http://127.0.0.1:8000/characters/fetch-all` in Postman, or any way you prefer.
