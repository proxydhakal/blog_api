## Installation

Setting up the Python environment

```bash
vitrualenv venv
venv\Scripts\activate
```

## Next, install Django and Django REST framework into the virtual environment via requirements.txt:

```
pip install -r requirements.txt
```

## Create Migration File
```
python manage.py migrate
```
## Run the Server
```
python manage.py runserver
```
#Now You Can Test Following Blog Api's

Create Blog: 127.0.0.1:8000/create

List Blog: 127.0.0.1

Detail Blog: 127.0.0.1/<pk>

Update Blog:127.0.0.1/update/<pk>

## License

[MIT](https://choosealicense.com/licenses/mit/)