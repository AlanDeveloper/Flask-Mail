CREATE DATABASE "ds2Mail";

CREATE TABLE "user" (
    "code" serial,
    "email" varchar(100) NOT NULL,
    "password" varchar(1000) NOT NULL
);
CREATE TABLE "public" (
    "code" serial,
    "email" varchar(100) NOT NULL,
    "message" varchar NOT NULL
);
CREATE TABLE "subscribe" (
    "code" serial,
    "email" varchar(100) NOT NULL
);

INSERT INTO "user" (email, password) values ('admin@gmail.com', 'admin');