create database painel_digital
default character set utf8mb4
default collate utf8mb4_general_ci;

create table login (
matricula int not null, 
nome varchar (30) not null,
id_user varchar (10) not null,
senha decimal(8) default '12345678',
nivel varchar(5) default 'guest',
primary key (matricula)
) default charset = utf8mb4;

insert into login
(matricula, nome, id_user, nivel)
values
('3927','Ricardo Lucas Tieppo Martins','rtieppo','full');

select * from login;
describe login;