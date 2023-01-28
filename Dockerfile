FROM python:3.8.3-alpine
# ENV PYTHONUNBUFFERED=1
WORKDIR /intro-app
# COPY requirements.txt requirements.txt
# RUN \
#  apk add --no-cache python3 postgresql-libs && \
#  apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
#  pip install -r requirements.txt && \
#  apk --purge del .build-deps
COPY . .
RUN chmod +x entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]
