alter table login
add column apelido varchar(10) after nome;

alter table login
add column marcador varchar(1) default '0' after save_inf;

select * from login;

desc login;

alter table login
modify column senha varchar(8) default '12345678';

alter table login
drop column save_inf;

select apelido from login
where id_user = 'rtieppo';

drop database painel_digital;