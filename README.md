# TEST RainFall on Fields

This is just a little technical test to a job interview.



## Getting Started

Backend Python / Django:

Our application allows you to record precipitated rains in a field.
The user of the application can load her fields, and then record all the rains that fall on it.
The required field information is the name, the number of hectares and its coordinates (latitude and longitude).
On the other hand, the rainfall data will be loaded indicating the date and the precipitated millimeters.
To simplify the exercise, the system does not support multiple users. There is only one, and it does not require any type of authentication.



## Preconditions and assumptions

- Each rainfall registration is only for one field
- The coordinates are just info data



## Installing

**1)** clone the repository

**2)** virtualenv -p python3 .venv && source .venv/bin/activate

**3)** pip install -r requirements.txt

**4)** python manage.py makemigrations

**5)** python manage.py migrate

**6)** python manage.py createsuperuser

**7)** python manage.py loaddata kilimo-field.json

**8)** python manage.py loaddata kilimo-register.json

**9)** python manage.py runserver



## User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/field/` | List of Fields
GET | `/api/field/detail/{pk}/` | Field detail
GET | `/api/field/fields-average-rainfall/` | List of fields with their average rainfall millimetres
GET | `/api/field/fields-total-rainfall/` | List of fields with their total rainfall millimetres
GET | `/api/field/fields-rainfall/` | List of rainfall registers by field
POST | `/api/register/create/rainfall` | Create a rainfall register



## Usage and examples

Once you create your superuser, open browser on http://localhost:8000/admin/

- curl -H "Content-Type: application/json" http://localhost:8000/api/field/
- curl -H "Content-Type: application/json" http://localhost:8000/api/field/detail/2/
- curl -X GET -H "Content-Type: application/json" -d '{"days": 7}' http://localhost:8000/api/field/fields-average-rainfall/
- curl -X GET -H "Content-Type: application/json" -d '{"total_millimetres": 373}' http://localhost:8000/api/field/fields-total-rainfall/
- curl -H "Content-Type: application/json" http://localhost:8000/api/field/fields-rainfall/
- curl -H "Content-Type: application/json" -d '{"field": 2, "millimetres": "11.600","date_register": "2018-09-10","time_register": "14:00:00"}' http://localhost:8000/api/register/create/rainfall


## Built With

* [Python - 3.8.2]
* [Django - 3.0]
* [DRF  - 3.11.1]


## Author

* **Gerardo Velazquez (GV)** - *Software Engineer* -

This project is also for personal research.
