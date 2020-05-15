# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:3.7-alpine

# 作業ディレクトリを設定
WORKDIR /usr/src/scraper

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# psycopg2のインストール
RUN apk update \
    && apk add --no-cache jpeg-dev zlib-dev \
    && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev build-base linux-headers\
    && pip install Pillow \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    # && apk add --no-cache build-base mariadb-connector-c-dev \
    # && pip install mysqlclient \
    && apk del build-deps

# Pipenvをインストール
RUN pip install --upgrade pip \
&& pip install pipenv

# ホストのpipfileをコンテナの作業ディレクトリにコピー
COPY ./Pipfile /usr/src/scraper/Pipfile

# pipfileからパッケージをインストールしてDjango環境を構築
RUN pipenv install --skip-lock --system --dev

# entrypoint.shをコピー
COPY ./entrypoint.sh /usr/src/scraper/entrypoint.sh

# ホストのカレントディレクトリ（現在はscraperディレクトリ）を作業ディレクトリにコピー
COPY . /usr/src/scraper/

# entrypoint.shを実行
ENTRYPOINT ["/usr/src/scraper/entrypoint.sh"]