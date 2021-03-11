# define base, label, and working path
FROM python
LABEL maintainer="code@tythos.net"
WORKDIR /application

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy and run application
COPY . .
ENTRYPOINT ["python", "service.py"]
