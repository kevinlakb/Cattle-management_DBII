create database amedla;
use amedla;
SET SQL_SAFE_UPDATES = 0;
-- -----------------------------------------------------Tablas-----------------------------------------------------------------------

CREATE TABLE ciudades(
codi_ciudad varchar(5) primary key NOT NULL,
nombre character varying(40) NOT NULL
);

CREATE TABLE empleados(
cod_empl varchar(5) primary key NOT NULL,
num_identip varchar(15) NOT NULL,
puesto varchar(15) NOT NULL,
nombree1 varchar(20) NOT NULL,
nombree2 varchar(20),
apellidoe1 varchar(20) NOT NULL,
apellidoe2 varchar(20) NOT NULL,
salario int NOT NULL,
titulo_educa varchar(80) NOT NULL,
observaciones varchar(150),
licen_condu character(2) NOT NULL,
fecha_contrato datetime NOT NULL,
fecha_naci datetime NOT NULL,
    ciudad varchar(5) NOT NULL,
    finca varchar(5) NOT NULL,
    jefe varchar(5),
    eps varchar(6) NOT NULL
);

CREATE TABLE fincas(
codi_finca varchar(5) primary key NOT NULL,
nombre varchar(30) NOT NULL,
tamano float NOT NULL,
    ciudad varchar(5) NOT NULL,
posicion_global varchar(40) NOT NULL
);

CREATE TABLE insumos(
codi_insu varchar(10) primary key NOT NULL,
descripcion varchar(40) NOT NULL,
nombre varchar(40) NOT NULL,
    finca varchar(5) NOT NULL,
    proveedor varchar (5) NOT NULL,
cant_total int NOT NULL
);

CREATE TABLE proveedores(
codi_identi varchar(5) primary key NOT NULL,
num_identip  varchar(15) NOT NULL,
nombrep1 varchar(20) NOT NULL,
nombrep2 varchar(20),
apellidop1 varchar(20) NOT NULL,
apellidop2 varchar(20) NOT NULL
);

CREATE TABLE telefonos(
numero int primary key NOT NULL,
    cliente varchar(5),
    proveedor varchar(5),
    empleado varchar(5),
    eps varchar(6),
    operador varchar(15) not null
);

CREATE TABLE rotaciones(
id int primary key  NOT NULL,
    numero int NOT NULL,
area float NOT NULL,
canti_cacao int,
canti_anim int,
    tierra varchar(30) NOT NULL,
capa_carga float
);

CREATE TABLE tierras (
    nombre varchar(30) primary key NOT NULL,
    tamano float NOT NULL,
    codi_finca varchar(5) NOT NULL
);

CREATE TABLE mantenimientos_r(
codigo_man varchar(5) primary key  NOT NULL,
descrip_man varchar(80) NOT NULL,
    rotacion int NOT NULL,
fecha datetime NOT NULL
);

CREATE TABLE cosechas(
codigo_cos varchar(5) primary key  NOT NULL,
estado character(2) NOT NULL,
peso float NOT NULL,
fecha datetime NOT NULL,
descri_estado varchar(80),
    factura varchar(5),
    planta varchar(5) NOT NULL,
    rotacion int NOT NULL
);

CREATE TABLE plantas_Cacao(
identi_planta varchar(5) primary key  NOT NULL,
estado_planta varchar(15) NOT NULL,
descrip_planta varchar(40)
);

CREATE TABLE bovinos(
identi_bovi varchar(5) primary key  NOT NULL,
sexo varchar(9) NOT NULL,
estado_bovi varchar(15) NOT NULL,
estado varchar(80),
peso int,
fecha_nacim date NOT NULL,
fecha_entrada_rotacion date NOT NULL,
    madre varchar(5),
    factura varchar(5),
    rotacion int
 );

CREATE TABLE facturas(
codigo_factu varchar(5) primary key NOT NULL,
precio_kilobo int default 18000,
precio_kiloca int default 5600,
precio_totalbo int default 0,
precio_totalca int default 0,
precio_total int default 0,
fecha date NOT NULL
);

CREATE TABLE ordenes_entrega(
id varchar(5) primary key NOT NULL,
fecha_entrega_orden date,
    cliente varchar(5) NOT NULL,
    factura varchar(5) NOT NULL,
    camion varchar(7) NOT NULL,
    observaciones varchar(80)
);
 
CREATE TABLE clientes(
cliente_id varchar(5) primary key NOT NULL,
telefono int NOT NULL,
nombrec1 varchar(20) NOT NULL,
nombrec2 varchar(20),
apellidoc1 varchar(20) NOT NULL,
apellidoc2 varchar(20) NOT NULL
);

CREATE TABLE camiones(
matricula varchar(7) primary key NOT NULL,
marca varchar(20) NOT NULL,
    num_chasis varchar(20) NOT NULL,
    fecha_adquisicion date NOT NULL,
    observaciones varchar(80)
);

CREATE TABLE mantenimientos(
codigo_mante varchar(5) primary key NOT NULL,
    matricula varchar(7) NOT NULL,
fecha_mante date NOT NULL
);

CREATE TABLE jornadas_insem(
codi_insem varchar(5) primary key NOT NULL,
    observaciones varchar(80)
);

CREATE TABLE cajones(
codigo_caj varchar(5) primary key NOT NULL,
peso_max float NOT NULL,
observaciones varchar(80)
);

CREATE TABLE bovinos_jornadas(
identi_bovi varchar(5) NOT NULL,
codi_insem varchar(5) NOT NULL,
fecha date NOT NULL,
    primary key(identi_bovi, codi_insem)
);

CREATE TABLE cosechas_cajones(
codigo_cos varchar(5) NOT NULL,
codigo_caj varchar(5) NOT NULL,
fecha date NOT NULL,
    primary key(codigo_cos, codigo_caj)
);
   
CREATE TABLE control_insumos(
cod int primary key auto_increment NOT NULL,
    cod_insumo varchar(10) NOT NULL,
    canti_entra int,
    canti_sali int,
    fecha_actualizacion date NOT NULL
);

CREATE TABLE eps(
identi_eps varchar(6) primary key NOT NULL,
nombre varchar(40) NOT NULL,
pagina_web varchar(40) NOT NULL
);
-- -----------------------------------------------------Alters-----------------------------------------------------------------------

ALTER TABLE empleados
ADD foreign key fk_jefe(jefe) references empleados(cod_empl),
ADD foreign key fk_empleados_fincas(finca) references fincas(codi_finca),
ADD foreign key fk_empleados_ciudades(ciudad) references ciudades(codi_ciudad),
ADD foreign key fk_empleados_eps(eps) references eps(identi_eps);

ALTER TABLE bovinos
ADD foreign key fk_madre(madre) references bovinos(identi_bovi),
ADD foreign key fk_factura(factura) references facturas(codigo_factu),
ADD foreign key fk_rotacion(rotacion) references rotaciones(id);

ALTER TABLE cosechas_cajones
ADD foreign key id_cajones(codigo_caj) references cajones(codigo_caj),
ADD foreign key id_cos(codigo_cos) references cosechas(codigo_cos);

ALTER TABLE cosechas
ADD foreign key fk_factura(factura) references facturas(codigo_factu),
ADD foreign key fk_idplanta(planta) references plantas_cacao(identi_planta),
ADD foreign key fk_rotacion(rotacion) references rotaciones(id);

ALTER TABLE fincas
ADD foreign key fk_ciudad(ciudad) references ciudades(codi_ciudad);

ALTER TABLE insumos
ADD foreign key fk_finca(finca) references fincas(codi_finca),
ADD foreign key fk_proveedor(proveedor) references proveedores(codi_identi);

ALTER TABLE bovinos_jornadas
ADD foreign key fk_bovino(identi_bovi) references bovinos(identi_bovi),
ADD foreign key fk_jornada(codi_insem) references jornadas_insem(codi_insem);

ALTER TABLE mantenimientos
ADD foreign key fk_matricula(matricula) references camiones(matricula);

ALTER TABLE mantenimientos_r
ADD foreign key fk_rotacion(rotacion) references rotaciones(id);

ALTER TABLE ordenes_entrega
ADD foreign key fk_cliente(cliente) references clientes(cliente_id),
ADD foreign key fk_factura(factura) references facturas(codigo_factu),
ADD foreign key fk_camion(camion) references camiones(matricula);

ALTER TABLE rotaciones
ADD foreign key fk_tierra(tierra) references tierras(nombre);

ALTER TABLE telefonos
ADD foreign key fk_cliente(cliente) references clientes(cliente_id),
ADD foreign key fk_proveedor(proveedor) references proveedores(codi_identi),
ADD foreign key fk_eps(eps) references eps(identi_eps),
ADD foreign key fk_empleado(empleado) references empleados(cod_empl);

ALTER TABLE tierras
ADD foreign key fk_finca(codi_finca) references fincas(codi_finca);

ALTER TABLE control_insumos
ADD foreign key fk_insumos(cod_insumo) references insumos(codi_insu);
-- -----------------------------------------------------Inserciones-----------------------------------------------------------------------
INSERT INTO ciudades Values
("68001", "Bucaramanga"),
("68081", "Barrancabermeja"),
("05579", "Puerto Berrío"),
("68655", "Sabana de Torres"),
("68190", "Cimitarra");  
   
INSERT INTO fincas Values
("1", "La Princesa", 650, 68655, "20° 25´ 30.23´´ N"),
("2", "El Ariete", 1022, 68081, "34° 33´ 43.12´´ S"),
("3", "Soplavientos", 845, 68190, "45° 32´ 25.35´´ N");
   
INSERT INTO eps Values
("EPS033", "SALUDVIDA EPS S.A", "https://www.saludvidaeps.com"),
("EPS016", "COOMEVA EPS S.A.", "http://eps.coomeva.com.co/"),
("CCF018", "CAFAM", "https://www.cafam.com.co/"),
("EMP021", "EPS SURA", "https://www.epssura.com/");

INSERT INTO empleados Values
("ad001","1234", "Administrador", "Alejandra", null, "Ventila", "Vacas", 1850000, "Médico Veterinario", "Buena empleada", "A2", "2015-03-22", "1996-03-22", "68001", "1", null, "EMP021"),
("va001", "4563", "Vaquero", "Emilio", "Maria", "Gaitán", "Mancas", 1350000, "Bachiller", "Permiso por incapacidad médica", "NO", "2017-05-14", "1980-05-22", "68190", "1", "ad001", "EPS016"),
("va002", "1485", "Vaquero", "Ernesto", null, "Dávila", "Cámelas", 1350000, "Bachiller", "Sabe arreglar celulares", "A1", "2018-12-12", "1976-11-11", "68081", "1", "ad001", "EPS016"),
("va003", "5846", "Vaquero", "Camilo", "Camile", "Camila", "Camilla", 1350000, "Primaria", "Muy buena gente", "NO", "2017-08-15", "1995-04-21", "68655", "1", "ad001", "EMP021"),
("co001", "5886", "Conductor", "Conducto", "Mariano", "Espinas", "Cabello", 1250000, "Bachiller", "Siempre llega a tiempo", "B3", "2014-06-10", "1980-10-31", "68190", "1", "ad001", "EPS016"),
("of001", "1448", "Oficios Varios", "Isabelo", null, "Portilla", "Naranjo", 1460000, "Bachiller", "Sabe cocinar cebolla frita", "NO", "2017-05-05", "1982-10-15", "68655", "1", "ad001", "EPS033"),
("of002", "1468", 'Oficios Varios', 'Eduardo', null, 'Mantilla', 'Nuñez', 1460000, 'Bachiller', "Le gusta dormir", 'NO', '2018-07-05', '1985-10-25', "68001", '1',  "ad001", "CCF018"),
       
("ad002", "1111", 'Administrador', 'Marcos', 'Juliano', 'Menethil', 'Spartan', 1850000, 'Administrador', "Maestro del origami", 'B2', '2012-05-12', '1987-12-20', "68001", "2", null, "EPS016"),
("va004", "4553", 'Vaquero', 'John', 'Winston', 'Lenon', 'Lenoni', 1350000, 'Bachiller', "Come mucho", 'A2', '2015-05-14', '1980-10-02', "68655", "2", "ad002", "EMP021"),
("va005", "1473", 'Vaquero', 'Wilson', 'Merecumbe', 'Lennin', 'Danonino', 1350000, 'Bachiller', "No le gusta bañarse", 'NO', '2016-11-30', '1978-01-20', "68190", "2", "ad002", "EPS016"),
("va006", "4543", 'Vaquero', 'Matias', null, 'Morris', 'Morrison', 1350000, 'Bachiller', "Hace trucos de magia", 'NO', '2015-10-14', '1982-03-02',  "68001", "2", "ad002", "EMP021"),
("co002", "2586", 'Conductor', 'Naren', 'Fabian', 'Molina', 'Curro', 1250000, 'Bachiller', 'Llamado de atencion por mala conducta', 'B3', '2011-02-20', '1989-07-12', "68001", "2", "ad002", "EMP021"),
("of003", "1418", 'Oficios Varios', 'Martin', null, 'Morro', 'Piede', 1460000, 'Bachiller', "Profesor de gatos", 'NO', '2019-01-05', '1982-02-28', "68655", "2", "ad002", "EPS016"),
("of004", "1328", 'Oficios Varios', 'Elias', null, 'Rico', 'Cuesta', 1460000, 'Bachiller', "No quiere bailar", 'NO', '2016-05-15', '1990-03-13', "68190", "2", "ad002", "CCF018"),
       
("ad003", "22222", 'Administrador', 'Hernan', 'Fruto', 'Del', 'Bosque', 1850000, 'Veterinario', "Cantante nato", 'B2', '2014-09-15', '1986-04-20', "68655", "3", null, "CCF018"),
("va007", "2121", 'Vaquero', 'Martinio', 'Martini', 'Martinez', 'Martha', 1350000, 'Bachiller', "Habla 30 idiomas", 'A2', '2014-05-27', '1980-08-02', "68190", "3", "ad003", "EMP021"),
("va008", "2231", 'Vaquero', 'Que', 'Lindo', 'Nombre', 'Tengo', 1350000, 'Bachiller', "Quiere aprender a bailar salsa", 'NO', '2013-02-01', '1980-09-02', "68655", "3", "ad003", "EPS016"),
("va009", "3131", 'Vaquero', 'Casimiro', null, 'Bayona', 'Rincon', 1350000, 'Bachiller', "Le gusta el chimichurri", 'A2', '2017-03-15', '1980-07-02', "05579", "3", "ad003", "EMP021"),
("co003", "5151", 'Conductor', 'Mago', null, 'Merlin', 'Magia', 1250000, 'Bachiller', "No sabe nadar", 'B3', '2018-05-10', '1992-07-08', "68001", "3", "ad003", "CCF018"),
("of005", "8585", 'Oficios Varios', 'El', 'Rubius', 'OMG', 'Yutúb', 1460000, 'Bachiller', "Juego al tejo", 'NO', '2017-11-15', '1992-08-07', "68190", "3", "ad003", "EMP021"),
("of006", "9090", 'Oficios Varios', 'Vegeta', 'Siete', 'Siete', 'Siete', 1460000, 'Bachiller', "Dice muchas groserias", 'NO', '2016-06-03', '1993-11-22', "68655", "3", "ad003", "CCF018");
   
INSERT INTO proveedores Value
("pr001", "12345", "Cecilia", null, "Martinez", "Galeano"),
("pr002", "85236", "Martha", "Matilde", "Nuñez", "Smith"),
("pr003", "14785", "Policarpo", null, "Triviño", "Avendaño"),
("pr004", "14548", "Ernesto", "Sabe", "Cantar", "Bonito");

INSERT INTO insumos Values
("in001", "Abono completo, bolsa 1kg", "Abono Doña Olga", "1", "pr001", 10),
("in002", "Quimico desinfectante, botella 1lt", "Mekan", "1", "pr002", 15),
("in003", "Correctivo de pH para suelos", "Lopa", "2","pr003", 22),
("in004", "Herbicida", "Bultileno", "2", "pr004", 35),
("in005", "Fungicida", "Maield","2", "pr004", 35),
("in006", "Guantes de Carnasa", "Marthals", "2", "pr002", 35),
("in007", "Botas de caucho", "Moniquetos", "2", "pr004", 51),
("in008", "Alambre dulce", "Cólnicas", "3", "pr001", 32),
("in009", "Vacuna Aftosa", "Buricana", "3", "pr003", 14),
("in010", "Jeringas", "Docto", "3", "pr002", 37);
       
INSERT INTO tierras Values
("Agujero", 89, "1"),
("Champaña", 67, "1"),
("Principe", 63, "1"),
("Carrosas", 22, "2"),
("Muestreos", 15, "2"),
("Mostaza", 89, "2"),
("Hojarasca", 77, "3"),
    ("Malezas", 27, "3"),
    ("Tango", 127, "3");
   
    INSERT INTO rotaciones Values
(1, 1, 50, 34, 0, "Agujero", 0),
    (2, 2, 39, 23, 0, "Agujero", 0),
    (3, 1, 18, 22, 0, "Carrosas", 0),
    (4, 2, 4, 12, 0, "Carrosas", 0),
    (5, 1, 50, 0, 45, "Champaña", 50),
    (6, 2, 17, 0, 23, "Champaña", 28),
    (7, 1, 10, 0, 22, "Malezas", 22),
    (8, 2, 17, 0, 10, "Malezas", 20),
    (9, 1, 40, 0, 34, "Mostaza", 50),
    (10, 2, 33, 0, 34, "Mostaza", 45),
    (11, 3, 16, 0, 15, "Mostaza", 20),
    (12, 1, 7, 43, 0, "Muestreos", 0),
    (13, 2, 8, 12, 0, "Muestreos", 0),
    (14, 1, 30, 77, 0, "Principe", 0),
    (15, 2, 35, 99, 0, "Principe",0),
    (16, 1, 50, 0, 43, "Tango", 60),
    (17, 2, 50, 0, 50, "Tango", 60),
    (18, 3, 27, 0, 22, "Tango", 30);
   
    Insert into mantenimientos_r Values
(1, "Se regaron semillas para pasto", 5, "2018-11-25"),
    (2, "Se cortó la maleza situada al centro del terreno", 10, "2019-01-01"),
    (3, "Se repararon los desagues", 1, "2019-03-04"),
    (4, "Se regaron semillas para pasto", 16, "2019-05-05");
    select * from facturas;
   
    insert into facturas (codigo_factu, fecha) Values
(1, "2018-12-01"),
    (2, "2019-01-01"),
    (3, "2019-02-02"),
    (4, "2019-02-03"),
    (5, "2019-03-04"),
    (6, "2019-04-03"),
    (7, "2019-04-05"),
    (8, "2019-05-07"),
    (9, "2019-07-12"),
    (10, "2019-12-12");
   
     insert into bovinos Values
("01_01", "Femenino", "Ok", "Saludable", 350, "2015-05-06", "2020-02-02", null, null, 5),
    ("01_02", "Femenino", "Ok", "Saludable", 400, "2015-04-08", "2020-02-03", null, null, 5),
    ("01_03", "Femenino", "OK", "Saludable", 250, "2016-12-01", "2020-02-03", "01_01", null, 5),
    ("01_04", "Femenino", "Ok", "Saludable", 200, "2016-08-09", "2020-02-02", "01_02", null, 5),
    ("02_01", "Femenino", "Vendido", "Vendido", 450, "2016-12-01", "2018-12-01", null, 1, null),
    ("02_02", "Femenino", "Vendido", "Vendido", 450, "2016-12-11", "2018-12-01", null, 1, null),
    ("02_03", "Femenino", "Ok", "Se recuperó de torcedura de pata", 258, "2019-12-04", "2020-02-02", "02_01", null, 10),
    ("02_04", "Femenino", "Enferma", "Presenta bajo peso. Bajo observación médica", 102, "2019-12-01", "2020-03-04", "02_02", null, 10),
    ("03_01", "Femenino", "Vendido", "Vendido", 500, "2015-12-31", "2019-02-03", null, 4, null),
    ("03_02", "Femenino", "Vendido", "Vendido", 550, "2016-01-30", "2019-02-03", null, 4, null),
    ("03_03", "Femenino", "Ok", "Saludable", 230, "2019-08-09", "2020-02-03", "03_01", null, 16),
    ("03_04", "Femenino", "Ok", "Saludable", 230, "2019-05-05", "2020-03-15", "03_02", null, 16),
    ("01_05", "Femenino", "Pr", "Correcto desarrollo", 265, "2017-05-05", "2020-03-15", "01_01", null, 5),
    ("02_05", "Femenino", "Pr", "Correcto desarrollo", 423, "2017-05-05", "2020-03-15", "02_01", null, 10),
    ("03_05", "Femenino", "Pr", "Correcto desarrollo", 350, "2017-05-05", "2020-03-15", "03_01", null, 16);
   
    insert into jornadas_insem Values
(1, "Exitosa"),
    (2, "Exitosa"),
    (3, "Exitosa");
   
    insert into plantas_cacao Values
("c1_01", "Ok", "Podada en 2020-03-20"),
    ("c2_01", "Ok", "Correcto"),
    ("c1_02", "Ok", "Tratada por monilia en 2020-02-15"),
    ("c2_02", "Ok", "Correcto"),
    ("c1_03", "OK", "Correto"),
    ("c2_03", "OK", "Correcto");
   
    insert into cosechas Values
("ca1", "Ve", 70, "2018-12-16", "Vendida",  2, "c1_01", 1),
    ("ca2", "Ve", 70, "2019-01-02", "Vendida",  3, "c1_02", 1),
    ("ca3", "In", 65, "2018-07-08", "Fruto en mal estado", null, "c1_03", 1),
    ("ca4", "Ve", 50, "2019-02-06", "Vendida",  5, "c2_01", 13),
("ca5", "Ve", 40, "2019-02-06", "Vendida",  6, "c2_02", 13),
("ca6", "Ve", 56, "2019-05-06", "Vendida",  7, "c2_03", 13),
("ca7", "Ve", 52, "2020-01-15", "Vendida",  8, "c1_02", 15),
("ca8", "Ve", 52, "2020-01-15", "Vendida",  9, "c1_03", 15),
("ca9", "Ve", 52, "2019-08-15", "Vendida",  10, "c2_02", 4);
   
    insert into cajones Values
("1", 50, "Buen Estado"),
("2", 52, "Buen Estado"),
("3", 45, "Buen Estado"),
("4", 52, "Buen Estado"),
("5", 56, "Buen Estado"),
("6", 50, "Buen Estado"),
    ("7", 50, "Buen Estado"),
    ("8", 57, "Buen Estado"),
    ("9", 88, "Buen Estado"),
    ("10", 50, "Buen Estado");
   
    insert into cosechas_cajones Values
("ca1", "1", "2018-12-25"),
    ("ca2", "2", "2019-01-12"),
    ("ca3", "3", "2018-07-18"),
    ("ca4", "4", "2019-02-16"),
    ("ca5", "5", "2019-02-16");
   
    insert into clientes Values
("12345", 1111111, "Juancho", "Ivancho", "Cristancho", "Pancho"),
    ("22345", 2222222, "Gabriel", "Cristobal", "Vaso", "Milk"),
    ("32345", 3333333, "Lucho", "Juan", "Sanguieno", "Dekl"),
    ("42345", 4444444, "Miguel", "Maria", "Cajon", "Mora"),
    ("52345", 5555555, "Ana", "Lorena", "Herrera", "Pina"),
    ("62345", 6666666, "Lorena", "Ana", "Morcilla", "Fucsia"),
    ("72345", 7777777, "Juana", "Moreta", "Catatata", "Capuccino");
   
insert into camiones Values
("abc_123", "Guilo", "15321654865", "2019-05-05", "Genial estado"),
    ("adc_163", "Guilo", "56845621355", "2019-05-05", "Genial estado"),
    ("arc_143", "Guilo", "98756564322", "2019-05-05", "Genial estado");
   
insert into mantenimientos Values
("ma1", "abc_123", "2020-01-01"),
    ("ma2", "adc_163", "2020-01-01"),
    ("ma3", "arc_143", "2020-01-01");
   
    insert into ordenes_entrega Values
("or1", "2018-12-11", "12345", 1, "abc_123", "Entregada"),
    ("or2", "2019-12-18", "42345", 2, "adc_163", "Entregada"),
    ("or3", "2019-02-12", "62345", 3, "arc_143", "Entregada"),
    ("or4", "2019-05-13", "72345", 4, "arc_143", "Entregada");
   
    insert into bovinos_jornadas Values
("01_01", 1, "2016-01-01"),
    ("01_02", 1, "2016-01-01"),
    ("02_01", 2, "2018-01-01"),
    ("02_02", 2, "2018-01-01"),
    ("03_01", 3, "2018-11-01"),
    ("03_02", 3, "2018-11-01");
   
    insert into tierras Values
("Venta1", 0, 1),
("Venta2", 0, 2),
("Venta3", 0, 3);
   
    insert into rotaciones Values
(19, 1, 0, 0, 0, "Venta1", 0),
    (20, 1, 0, 0, 0, "Venta2", 0),
    (21, 1, 0, 0, 0, "Venta3", 0);
   
    ALTER TABLE clientes DROP COLUMN telefono;
   
    insert into telefonos Values
(1111111, "12345", null, null, null, "Movistar"),
    (2222222, "22345", null, null, null, "Movistar"),
    (3333333, "32345", null, null, null, "Movistar"),
    (4444444, "42345", null, null, null, "Movistar"),
    (5555555, "52345", null, null, null, "Movistar"),
    (6666666, "62345", null, null, null, "Movistar"),
    (7777777, "72345", null, null, null, "Movistar"),
    (8888888, null, "pr001", null, null, "Claro"),
    (9999999, null, "pr002", null, null, "Claro"),
    (1010101, null, "pr003", null, null, "Claro"),
    (1100110, null, "pr004", null, null, "Claro"),
    (1111112, null, null, "ad001", null, "Tigo"),
    (1111154, null, null, "ad002", null, "Tigo"),
    (1111113, null, null, "ad003", null, "Tigo"),
    (1111114, null, null, "co001", null, "Tigo"),
    (1111115, null, null, "co002", null, "Tigo"),
    (1111116, null, null, "co003", null, "Tigo"),
    (1111117, null, null, "of001", null, "Tigo"),
    (1111118, null, null, "of002", null, "Tigo"),
    (1111119, null, null, "of003", null, "Tigo"),
    (2222221, null, null, "of004", null, "Tigo"),
    (2222223, null, null, "of005", null, "Tigo"),
    (2222224, null, null, "of006", null, "Tigo"),
    (2222225, null, null, "va001", null, "Tigo"),
    (2222226, null, null, "va002", null, "Tigo"),
    (2222277, null, null, "va003", null, "Tigo"),
    (5555558, null, null, "va004", null, "Tigo"),
    (5555551, null, null, "va005", null, "Tigo"),
    (5555553, null, null, "va006", null, "Tigo"),
    (5555554, null, null, "va007", null, "Tigo"),
    (4444442, null, null, "va008", null, "Tigo"),
    (4444441, null, null, "va009", null, "Tigo"),
    (4444443, null, null, null, "CCF018", "Tigo"),
    (2587412, null, null, null, "EMP021", "Tigo"),
    (6945254, null, null, null, "EPS016", "Tigo"),
    (0123575, null, null, null, "EPS033", "Tigo");
   
    update bovinos set rotacion = 20 where identi_bovi = "02_01";
update bovinos set rotacion = 20 where identi_bovi="02_02";
update bovinos set rotacion = 21 where identi_bovi = "03_01";
    update bovinos set rotacion = 21 where identi_bovi="03_02";

-- -----------------------------------------------------TRIGGERS-----------------------------------------------------------------------

-- Trigger 1, controla la cantidad de insumos disponibles
DELIMITER $$
CREATE TRIGGER canti_insumos after insert on control_insumos for each row
BEGIN
set @cant = (select cant_total from insumos where codi_insu=new.cod_insumo);
if new.canti_entra>0 then
update insumos set cant_total = @cant + new.canti_entra where codi_insu=new.cod_insumo;
elseif new.canti_sali>0 then
if @cant>new.canti_sali then
update insumos set cant_total = @cant-new.canti_sali where codi_insu=new.cod_insumo;
end if;
end if;
end $$
delimiter ;

-- Trigger 2, pasa el estado y la descripcion del estado de los bovinos a "Vendido"
DELIMITER $$
CREATE TRIGGER bovi_vendido before update on bovinos for each row
Begin
if new.factura > 0 then
set new.estado = "Vendido";
    set new.estado_bovi = "Vendido";
end if;
end $$
delimiter

-- Trigger 3, pasa el estado y la descripcion del estado de las cosechas a "Vendido"
DELIMITER $$
CREATE TRIGGER cose_vendido before update on cosechas for each row
Begin
if new.factura > 0 then
set new.estado = "Ve";
    set new.descri_estado = "Vendida";
end if;
end $$
delimiter ;

-- Trigger 4, calcula el precio total bovino por factura
DELIMITER $$
Create trigger factureo after update on bovinos for each row
Begin
if new.factura > 0 then
        update facturas set precio_totalbo = precio_totalbo + (new.peso * precio_kilobo) where codigo_factu = new.factura;
end if;
end $$
delimiter ;

-- Trigger 5, calcula el precio total de cacao por factura
DELIMITER $$
Create trigger factureo2 after update on cosechas for each row
Begin
if new.factura > 0 then
        update facturas set precio_totalca = precio_totalca + (new.peso * precio_kiloca) where codigo_factu = new.factura;
end if;
end $$
delimiter ;

-- Trigger 6, calcula el precio total de factura
DELIMITER $$
Create trigger total_factura before update on facturas for each row
Begin
set new.precio_total = (new.precio_totalbo + new.precio_totalca);
end $$
delimiter ;

-- Consulta 1, muestra los bovinos que han sido vendidos, a la vez que la finca en la que se vendieron, la fecha de su venta, la factura por la que se vendieron, el vehiculo que los transportó hacia el cliente
-- el cliente que realizó la compra y la fecha de la entrega del pedido.
Select
bov.identi_bovi as Animal_vendido,
    fin.nombre as Finca_procedencia,
    fac.fecha as Fecha_venta,
    fac.codigo_factu as Numero_factura,
    ord.camion as Placa_transporte,
    ord.cliente as Cliente,
    ord.fecha_entrega_orden as Fecha_entrega
From
ordenes_entrega ord
inner join facturas fac on (ord.factura = fac.codigo_factu)
inner join bovinos bov on (bov.factura = fac.codigo_factu)
inner join rotaciones r on (bov.rotacion = r.id)
inner join tierras t on (r.tierra = t.nombre)
inner join fincas fin on (t.codi_finca = fin.codi_finca);

-- Consulta 2. Se requiere consultar las cosechas vendidas, la finca en la que se vendieron, la fecha de su venta, el número de factura, el transporte usado para su entrega, el cliente quien realizó la compra
-- y la fecha de entrega.
Select
cos.codigo_cos as Cosecha_vendida,
    fin.nombre as Finca_procedencia,
    fac.fecha as Fecha_venta,
    fac.codigo_factu as Numero_factura,
    ord.camion as Placa_transporte,
    ord.cliente as Cliente,
    ord.fecha_entrega_orden as Fecha_entrega
From
ordenes_entrega ord
inner join facturas fac on (ord.factura = fac.codigo_factu)
inner join cosechas cos on (cos.factura = fac.codigo_factu)
inner join rotaciones rot on (cos.rotacion = rot.id)
inner join tierras tie on (rot.tierra = tie.nombre)
inner join fincas fin on (tie.codi_finca = fin.codi_finca);

-- Consulta 3.Se requiere consultar qué animales se encuentran en estado de preñez, la rotación en la que se encuentran, su edad y la finca en donde se encuentran.
Select
bov.identi_bovi as Bovino,
    bov.estado as Observaciones,
    concat(rot.tierra, ' ', rot.numero) as Rotacion,
    timestampdiff(year, bov.fecha_nacim, curdate()) AS Edad,
    fin.nombre as Finca
From
Bovinos bov
inner join rotaciones rot on (bov.rotacion = rot.id)
inner join tierras tie on (rot.tierra = tie.nombre)
inner join fincas fin on (tie.codi_finca = fin.codi_finca)
where bov.estado_bovi = "Pr";

-- Consulta 4. Se requiere consultar los insumos que han entrado, su código, su descripción, su cantidad, asi como el nombre, cedula y teléfono del vendedor y la finca en la que se encuentran.
Select
insu.nombre as Nombre_insumo,
    insu.codi_insu as Codigo_insumo,
    insu.descripcion as Descripcion_insumo,
    insu.cant_total as Cantidad_insumo,
    concat (pro.nombrep1, ' ', pro.apellidop1) as Proveedor,
    pro.num_identip as Cedula_proveedor,
    tel.numero as Telefono_proveedor,
    fin.nombre as Finca
From
insumos insu
inner join proveedores pro on (insu.proveedor = pro.codi_identi)
inner join telefonos tel on (tel.proveedor = pro.codi_identi)
inner join fincas fin on (insu.finca = fin.codi_finca)
order by insu.codi_insu;

-- Consulta 5. Se requiere consultar el primer nombre y primer apellido de los empleados, su cedula, edad, tiempo trabajando, la finca en la que labora, su puesto, el jefe ante quien responden y su número telefónico.
Select
concat(empl.nombree1, ' ', empl.apellidoe1) as Nombre_empleado,
    empl.num_identip as Cedula,
timestampdiff(year, empl.fecha_naci, curdate()) AS Edad,
timestampdiff(year, empl.fecha_contrato, curdate()) AS Tiempo_trabajando,
    fin.nombre as Finca,
    empl.puesto as Puesto,
    empl.jefe as Jefe,
    tel.numero as Telefono
From
empleados empl
inner join fincas fin on (empl.finca = fin.codi_finca)
inner join telefonos tel on (tel.empleado = empl.cod_empl);

-- Consulta 6. Se requiere conocer la información de factura donde se relacionen los elementos vendidos con sus pesos, los clientes a quienes se le vendieron,
-- el transporte que se uso para su entrega, la fecha de la venta, la finca de la que procede la venta, la factura por la cual se vendieron y la fecha de entrega.
Select
cos.codigo_cos as Cosecha_vendida,
    bovi.identi_bovi as Animal_vendido,
cos.peso as Peso_cosecha,
bovi.peso as Peso_animal,
    fin.nombre as Finca_procedencia,
    factu.codigo_factu as Numero_factura,
    factu.fecha as Fecha_venta,
    ord.camion as Placa_trasnporte,
    ord.fecha_entrega_orden as Fecha_entrega,
    ord.cliente as Cliente
From
ordenes_entrega ord
inner join clientes clien on (ord.cliente = clien.cliente_id)
inner join facturas factu on (ord.factura = factu.codigo_factu)
inner join bovinos bovi on (bovi.factura = factu.codigo_factu)
inner join cosechas cos on (cos.factura = factu.codigo_factu)
inner join rotaciones rot on (bovi.rotacion = rot.id)
inner join tierras tie on (rot.tierra = tie.nombre)
inner join fincas fin on (tie.codi_finca = fin.codi_finca);
