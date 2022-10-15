drop database if exists SHOOTER_DB;
create database SHOOTER_DB;
use SHOOTER_DB;

create table HISTORIAL(
	id int primary key AUTO_INCREMENT,
	nombre varchar (25),
	id_avion int,
    historialPuntos int,
    mejorPuntaje int
);

create table AVIONES(
	id int primary key AUTO_INCREMENT,
    nombre varchar (25),
    velocidadMovimiento int,
    velocidadDisparo int,
    potenciaDisparo int,
    salud int
);

alter table HISTORIAL
add foreign key (id_avion)
references aviones (id);

-- show databases