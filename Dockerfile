FROM python:3.12

#Python related env variables
  
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /home/app
ENV POETRY_HOME="/opt/poetry"
# Set venv to false as the container is already isolated, no need for it
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="/opt/poetry/bin:$PATH"
 
WORKDIR /home/app  
COPY ./pyproject.toml ./poetry.lock* ./  
  
# Install Poetry through Curl instead of using pip

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry install --no-interaction --no-ansi
  
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]