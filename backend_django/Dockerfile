# a docker file for a django app on port 8083 based off of python 3.11 on alpine
# the python environment is managed by pipenv
# the app is run by the command hupper -w repair_cafe_item_tracker/ -v -m waitress --port=8083 repair_cafe_item_tracker.wsgi:application

FROM python:3.11-alpine
WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv
RUN pipenv install --system
COPY . .
EXPOSE 8083
CMD hupper -w repair_cafe_item_tracker/ -v -m waitress --port=8083 repair_cafe_item_tracker.wsgi:application
