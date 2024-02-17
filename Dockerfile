FROM python:3.9

RUN apt-get update -y && apt-get install -y python3-venv python3-dev build-essential && python -m pip install pip-tools

WORKDIR /airport_checkin

#pip compile from requirements
COPY requirements.txt /airport_checkin/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /airport_checkin/requirements.txt

COPY . /airport_checkin

#if you use HTTPS mode, include this:
#EXPOSE 443
#EXPOSE 80


CMD ["uvicorn", "airport_checkin.main:app","--host", "0.0.0.0", "--port", "80", "--reload"]

# if you use HTTPS mode, comment line above and use this instead:
#CMD ["uvicorn", "airport_checkin.main:app","--ssl-certfile", "./fullchain.pem", "--ssl-keyfile","./privkey.pem", "--host", "0.0.0.0", "--port", "80", "--reload"]
