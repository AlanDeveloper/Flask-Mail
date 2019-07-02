CREATE DATABASE "ds2Mail";

CREATE TABLE "user" (
    "code" serial,
    "email" varchar(100) NOT NULL,
    "password" varchar(1000) NOT NULL,
    CONSTRAINT "userPK" PRIMARY KEY ("code")
);
CREATE TABLE "public" (
    "code" serial,
    "email" varchar(100) NOT NULL,
    "message" varchar NOT NULL,
    CONSTRAINT "publicPK" PRIMARY KEY ("code")
);
CREATE TABLE "subscribe" (
    "code" serial,
    "email" varchar(100) NOT NULL,
    CONSTRAINT "subsPK" PRIMARY KEY ("code")
);

INSERT INTO "user" (email, password) values ('admin@gmail.com', 'admin');
