FROM python:3
RUN git clone https://github.com/Lucasgarciamdz/numeros-romanos-Lucasgarciamdz.git
WORKDIR numeros-romanos-Lucasgarciamdz
RUN pip install -r requirements.txt
CMD ["python3 -m", "unittest"]