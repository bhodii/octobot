FROM gorialis/discord.py:3.9.2-buster-master-minimal

WORKDIR /app

COPY . .

CMD ["python", "octo.py"]
