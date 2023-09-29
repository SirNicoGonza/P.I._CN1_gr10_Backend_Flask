use mensajeria;
-- Se inserta en la Tabla usuario
INSERT INTO usuarios (nombre_usuario,contraseña, correo_electronico, imagen_perfil)
VALUES ('Batman', 'gotham0001', 'correoelectronico@correo.com', 'imagen_nn_nnnn'),
		('Superman', 'metropolis002', 'correoelectronico@correo.com', 'imagen_nn_nnnn'),
        ('Wonderwoman', 'temisira003', 'correoelectronico@correo.com', 'imagen_nn_nnnn'),
        ('Flash', 'centralcity004', 'correoelectronico@correo.com', 'imagen_nn_nnnn'),
        ('Aquaman', 'atlantis005', 'correoelectronico@correo.com', 'imagen_nn_nnnn');
        
-- Se inserta en la tabla servidores
INSERT INTO servidores (nombre, descripcion)
VALUES ('La baticueva','solo la batifamilia'),
		('La Atalaya', 'heroes de DC'),
        ('Diario El Planeta', 'informacio diaria'),
        ('Super Friends', 'super amigos');

-- Se inserta en la tabla nexo (usuario-servidor)
INSERT INTO nexo (id_usuario, id_servidor)
VALUES (1,1),
		(1,2),
        (1,3),
        (2,2),
        (2,3),
        (2,4),
        (3,2),
        (3,3),
        (3,4),
        (4,2),
        (4,4),
        (5,2),
        (5,4);

-- Se inserta en la tabla canales
INSERT INTO canales (nombre, id_servidor)
VALUES ('Canal 1', 1),
		('Canal 2',1),
        ('Informes 1',2),
        ('Informes 2',2),
        ('Informes 3',2),
        ('Informes 4',2),
        ('Noticias 1',3),
        ('Noticias 2',3),
        ('Noticias 3',3),
        ('Chat 1',4),
        ('Chat 2',4),
		('Chat 3',4);

-- Se inserta en la tabla mensajes
INSERT INTO mensajes (contenido, id_canal, id_usuario)
values ('Hola',1,1),
		('hola',1,1),
        ('informe N° 1000',3,1),
        ('informe N° 1001',4,1),
        ('Que tal?',10,2),
        ('Bien',10, 3);
        
