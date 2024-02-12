FROM python:3.12

#Python related env variables
  
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /home/app
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="/opt/poetry/bin:$PATH"
 
WORKDIR /home/app  
COPY ./pyproject.toml ./poetry.lock* ./  
  
RUN pip install poetry  
RUN poetry install  
  
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]