FROM python:alpine
RUN pip install nltk
WORKDIR /dir
COPY code.py /dir/
COPY random_paragraphs.txt /dir/
CMD python code.py