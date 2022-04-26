# django3-bootstrap5-template

My starter template for django using some 'must have' modules/gadgets for any project.

## Versions

- django (latest)
- bootstrap 5 (crispy-bootstrap5)

## tl;dr

Assuming you have already created a virtual environment(venv) and activated it:

```python
django-admin startproject kamehameha --template https://github.com/devadalberto/django3-bootstrap5-template/archive/refs/heads/main.zip
```

```python
cd kamehameha
```

```python
pip install -r requirements/dev.txt
```

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```

```python
python manage.py runserver
```

And you should see something like this:

![kamehameha_demo_startup](https://user-images.githubusercontent.com/18197046/145336560-087a2249-3ca1-42cd-8b7e-28abe3b790fa.png)

### More Details

This starter comes with an application named 'accounts', I extended the User model as per many readings/recommendations found all over the place.

Also it have some other files and settings that I took from a project called django-cookiecutter.

... more stuff coming soon

### ToDo

- [x] Create an accounts application to expand the user model
- [x] Create README that can actually be used to copy and paste
- [ ] Add a table/list with all the credits (I basically took a bunch of concepts from many pages so I claim NO rights here)
- [ ] Document how to change DB (basically changing from dev to test or prod configs)
- [ ] Make a similar template with different css frameworks (SemanticUI / TailwindCSS)
