# Notification Database Design

## Create Database Container
```
docker run -d --name riverFort_no -e POSTGRESQL_POSTGRES_PASSWORD=password123 -e POSTGRESQL_USERNAME=river -e POSTGRESQL_PASSWORD=fort -e POSTGRESQL_DATABASE=riverFort_no -p 5432:5432 bitnami/postgresql:11.4.0
```

## Access Database
```
psql -U river -h localhost riverFort_no
```
