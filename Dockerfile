# escape=`
FROM postgres


COPY clothbase.sql /docker-entrypoint-initdb.d/