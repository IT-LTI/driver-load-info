import os

DB_HOST = 'driver-load-info-db.clxkywsjsxsy.us-east-2.rds.amazonaws.com'
DB_USER = 'admin'
DB_PASSWORD = os.environ.get("DB_SECRET_CODE")
DB_NAME = 'dli'
