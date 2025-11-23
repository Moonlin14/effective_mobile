FROM python:3.10-alpine

WORKDIR /effective_mobile

RUN apk update && \
apk add --no-cache chromium chromium-chromedriver tzdata

ENV PATH="/usr/bin/chromedriver:${PATH}"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["sh", "-c", "pytest --alluredir=allure-results"]