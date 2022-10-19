show databases;
use shooter_db;

insert into aviones (nombre, velocidadMovimiento, velocidadDisparo, potenciaDisparo, salud)
value ('Pampa', 5, 20, 5, 10);

insert into aviones (nombre, velocidadMovimiento, velocidadDisparo, potenciaDisparo, salud)
value ('Tango', 6, 18, 4, 8);

insert into aviones (nombre, velocidadMovimiento, velocidadDisparo, potenciaDisparo, salud)
value ('Puma', 5.5, 18.5, 4.5, 9);

insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje) 
value ('Jugador1',1,150,200);

insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje)
value ('Jugador2',2,145,211);

insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje)
value ('Jugador3',2,95,120);

insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje)
value ('Jugador4',3,135,180);

select * from historial;
select * from aviones;

select TOP 3 from historial order by mejorPuntaje desc;




