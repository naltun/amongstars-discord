FROM python:3
ADD . /
RUN pip3 install discord.py
CMD [ "python", "./bot.py" ]
