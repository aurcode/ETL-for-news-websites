FROM continuumio/miniconda3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN conda install -y --file requirements.txt

RUN python -m nltk.downloader stopwords punkt

COPY . .

CMD [ "python", "./pipeline.py" ]
