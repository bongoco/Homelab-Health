#use current Python version
FROM python:3.11-slim
#set working directory within container to /app, if doesn't exist
WORKDIR /app
#copy all direcotry contents to /app at the container
COPY . /app
#install dependencies
RUN pip install --no-cache-dir -r requirements.txt
#Expose the port 
EXPOSE 5000
#Define command to run the app when container starts
CMD ["python", "dashboard.py"]




















