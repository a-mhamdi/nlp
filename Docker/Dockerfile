ARG UV_VERSION=0.4.20
ARG PYTHON_VERSION=3.12

###########################
#= STAGE 1: UV STAGE =#
##########################

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv-stage

###########################
#= STAGE 2: BUILD STAGE =#
##########################

FROM python:${PYTHON_VERSION}-slim AS builder

## Install build dependencies
RUN apt-get update && \
	apt-get install -y --no-install-recommends gcc libffi-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*

## Install `uv` for fast package management
COPY --from=uv-stage /uv /uvx /bin/
RUN uv venv /opt/venv

## Install dependencies
COPY Codes/pyproject.toml .
RUN uv sync
    
############################
#= STAGE 3: RUNTIME STAGE =#
############################

FROM python:${PYTHON_VERSION}-slim AS runtime
COPY --from=builder /.venv /opt/venv

## Metadata
LABEL author="A. Mhamdi <a_mhamdi@outlook.com>"
LABEL version="latest"

ENV PATH="/opt/venv/bin:$PATH"
ENV NLTK_DATA=/data/nltk_data
ENV GENSIM_DATA_DIR=/data/gensim_data

WORKDIR /workspace
COPY Codes/images .
COPY Codes/*.py .

EXPOSE 1357

CMD ["python", "-m", "marimo", "edit", "--host", "0.0.0.0", "--port", "1357", "--headless", "--no-token"]
