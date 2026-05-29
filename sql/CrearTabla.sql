create table if not exists estudiantes (
  id      serial primary key,
  nombre  varchar(255) not null,
  correo  varchar(255) not null unique,
  carrera varchar(255) not null
);
