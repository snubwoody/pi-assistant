create database pibot;

use pibot;

create table alarms(
    id int primary key,
    hours int not null,
    minutes int not null,
    fulfilled bool not null
);
