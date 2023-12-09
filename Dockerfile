# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY api/requirements.txt requirements.txt
COPY app/requirements.txt app-requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r app-requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set environment variables
ENV FLASK_APP=api/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV STREAMLIT_APP=app/app.py

# Expose ports
EXPOSE 5000 8501

# Run app.py when the container launches
CMD ["flask", "run", "--port", "5000", "&", "streamlit", "run", "--server.port", "8501", "app.py"]