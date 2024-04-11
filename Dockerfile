# escape=`
FROM postgres

ENV POSTGRES_PASSWORD docker
ENV postgres_DB user

COPY clothbase.sql /docker-entrypoint-initdb.d/