use shooter_db;
select * from aviones;
insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje) value ('JugadorZ',2,145,211);
UPDATE historial SET nombre = 'JugadorX' WHERE id=5;
delete from historial where id=9;

select * from historial;