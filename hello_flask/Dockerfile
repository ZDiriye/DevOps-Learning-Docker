# use a lightweight python base image
FROM python:3.8-slim

# sets the working directory in the container
WORKDIR /app

# copies the application code into container
COPY . .

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

# installs flask and redis
RUN pip install flask redis

# tells docker which port the app will use in the container
EXPOSE 5002

# run the application
CMD ["python", "app.py"]