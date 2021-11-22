FROM gorialis/discord.py:minimal

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt
COPY . .

CMD ["python", "octo.py"]
