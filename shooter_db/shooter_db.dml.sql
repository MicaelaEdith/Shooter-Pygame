show databases;
use shooter_db;

insert into aviones (nombre, velocidadMovimiento, velocidadDisparo, potenciaDisparo, salud)
value ('Pampa', 5, 20, 5, 10);

insert into aviones (nombre, velocidadMovimiento, velocidadDisparo, potenciaDisparo, salud)
value ('Tango', 5.5, 18, 4, 8);

insert into aviones (nombre, velocidadMovimiento, velocidadDisparo, potenciaDisparo, salud)
value ('Puma', 5.3, 18.5, 4.5, 9);

insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje) 
value ('Jugador1',1,150,200);

select * from aviones