FROM python:alpine
WORKDIR /usr/src/multilogin
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add gcc libc-dev g++ libffi-dev libxml2 unixodbc-dev unixodbc mariadb-dev libstdc++6 bash icu-libs krb5-libs libgcc libintl libssl1.1 libstdc++ zlib curl gnupg
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.10.1.1-1_amd64.apk
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.10.1.1-1_amd64.apk
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.10.1.1-1_amd64.sig
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.10.1.1-1_amd64.sig
RUN curl https://packages.microsoft.com/keys/microsoft.asc  | gpg --import -
RUN gpg --verify msodbcsql17_17.10.1.1-1_amd64.sig msodbcsql17_17.10.1.1-1_amd64.apk
RUN gpg --verify mssql-tools_17.10.1.1-1_amd64.sig mssql-tools_17.10.1.1-1_amd64.apk
RUN apk add --allow-untrusted msodbcsql17_17.10.1.1-1_amd64.apk
RUN apk add --allow-untrusted mssql-tools_17.10.1.1-1_amd64.apk
COPY ./requirements.txt /usr/src/multilogin/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/multilogin/