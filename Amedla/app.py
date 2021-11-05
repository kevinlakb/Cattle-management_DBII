from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="admin"
app.config["MYSQL_DB"]="Amedla"
mysql = MySQL(app)

app.secret_key = "mysecretkey"

@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/form/<string:table>")
def form(table):
    if table == "empleado":
        cur = mysql.connection.cursor()
        cur.execute("select codi_ciudad, nombre from ciudades")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codi_finca, nombre from fincas")
        data2 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select cod_empl, concat(nombree1,' ',ifnull(nombree2, '')) from empleados where cod_empl like 'ad%'")
        data3 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select identi_eps, nombre from eps")
        data4 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, ciudades = data1, fincas = data2, jefes = data3, epss = data4)

    if table == "bovino":
        cur = mysql.connection.cursor()
        cur.execute("select identi_bovi, rotacion from bovinos")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codigo_factu, precio_total from facturas")
        data2 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select id, numero from rotaciones")
        data3 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, bovinos = data1, facturas = data2, rotaciones = data3)

    if table == "bovino-jornada":
        cur = mysql.connection.cursor()
        cur.execute("select identi_bovi, rotacion from bovinos")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codi_insem from jornadas_insem")
        data2 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, bovinos = data1, jornadas = data2)

    if table == "finca":
        cur = mysql.connection.cursor()
        cur.execute("select codi_ciudad, nombre from ciudades")
        data1 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, ciudades = data1)

    if table == "tierra":
        cur = mysql.connection.cursor()
        cur.execute("select codi_finca, nombre from fincas")
        data1 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, fincas = data1)

    if table == "cosecha":
        cur = mysql.connection.cursor()
        cur.execute("select codigo_factu, precio_total from facturas")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select identi_planta from plantas_cacao")
        data2 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select id, numero from rotaciones")
        data3 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, facturas = data1, plantas = data2, rotaciones = data3)

    if table == "control-insumo":
        cur = mysql.connection.cursor()
        cur.execute("select codi_insu, nombre from insumos")
        data1 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, insumos = data1)

    if table == "cosecha-cajon":
        cur = mysql.connection.cursor()
        cur.execute("select codigo_cos, peso from cosechas")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codigo_caj, peso_max from cajones")
        data2 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, cosechas = data1, cajones = data2)

    if table == "insumo":
        cur = mysql.connection.cursor()
        cur.execute("select codi_finca, nombre from fincas")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codi_identi, concat(nombrep1,' ', ifnull(nombrep2, '')) from proveedores")
        data2 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, fincas = data1, proveedores = data2)

    if table == "mantenimiento":
        cur = mysql.connection.cursor()
        cur.execute("select matricula, marca from camiones")
        data1 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, camiones = data1)

    if table == "mantenimiento-r":
        cur = mysql.connection.cursor()
        cur.execute("select id, numero from rotaciones")
        data1 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, rotaciones = data1)

    if table == "orden-entrega":
        cur = mysql.connection.cursor()
        cur.execute("select cliente_id, concat(nombrec1,' ', ifnull(nombrec2, '')) from clientes")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codigo_factu, precio_total from facturas")
        data2 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select matricula, marca from camiones")
        data3 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, clientes = data1, facturas = data2, camiones = data3)

    if table == "rotacion":
        cur = mysql.connection.cursor()
        cur.execute("select nombre, tamano from tierras")
        data1 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, tierras = data1)

    if table == "telefono":
        cur = mysql.connection.cursor()
        cur.execute("select cliente_id, concat(nombrec1,' ', ifnull(nombrec2, '')) from clientes")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codi_identi, concat(nombrep1,' ', ifnull(nombrep2, '')) from proveedores")
        data2 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select cod_empl, concat(nombree1,' ',ifnull(nombree2, '')) from empleados")
        data3 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select identi_eps, nombre from eps")
        data4 = cur.fetchall()
        return render_template("Forms/form-{}.html".format(table), tp = table, clientes = data1, proveedores = data2, empleados = data3, epss = data4)

    if table == "cajon" or "camion" or "ciudad" or "cliente" or "eps" or "factura" or "jornada-insem" or "planta-cacao" or "proveedor":
        return render_template("Forms/form-{}.html".format(table), tp = table)

@app.route("/insert/<string:table>", methods=["POST"])
def insert_into(table):
    if table == "empleado":
        if request.method == "POST":
            ide = request.form["codigo"]
            cedula = request.form["dni"]
            puesto = request.form["puesto"]
            nombre1 = request.form["nombre1"]
            nombre2 = request.form["nombre2"]
            apellido1 = request.form["apellido1"]
            apellido2 = request.form["apellido2"]
            salario = request.form["salario"]
            titulo = request.form["titulo"]
            observaciones = request.form["observaciones"]
            licenciacon = request.form["licenciacon"]
            fechacontrato = request.form["fechacontrato"]
            fechanac = request.form["fechanac"]
            ciudad = request.form["ciudad"]
            codigofinca = request.form["codigofinca"]
            jefe = request.form["jefe"]
            eps = request.form["eps"]
            cur = mysql.connection.cursor()
            cur.execute("""insert into empleados
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (ide, cedula, puesto, nombre1, nombre2, apellido1, apellido2, salario, titulo, observaciones, licenciacon, fechacontrato, fechanac, ciudad, codigofinca, jefe, eps))
            mysql.connection.commit()
            flash("Empleado agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "bovino":
        if request.method == "POST":
            idb = request.form["idb"]
            sexo = request.form["sexo"]
            estado = request.form["estado"]
            estadodes = request.form["estadodes"]
            peso = request.form["peso"]
            fechanac = request.form["fechanac"]
            fecharotacion = request.form["fecharotacion"]
            madre = request.form["madre"]
            factura = request.form["factura"]
            rotacion = request.form["rotacion"]
            cur = mysql.connection.cursor()
            cur.execute("insert into bovinos values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (idb, sexo, estado, estadodes, peso, fechanac, fecharotacion, madre, factura, rotacion))
            mysql.connection.commit()
            flash("Bovino agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "bovino-jornada":
        if request.method == "POST":
            idbj = request.form["idbj"]
            codigoins = request.form["codigoins"]
            fecha = request.form["fecha"]
            cur = mysql.connection.cursor()
            cur.execute("insert into bovinos_jornadas values(%s, %s, %s)",
            (idbj, codigoins, fecha))
            mysql.connection.commit()
            flash("Jornada de Bovinos agregada satisfactorimente")
            return redirect("/form/{}".format(table))
    
    if table == "finca":
        if request.method == "POST":
            codigo = request.form["codigo"]
            nombre = request.form["nombre"]
            tamano = request.form["tamano"]
            ciudad = request.form["ciudad"]
            posicion = request.form["posicion"]
            cur = mysql.connection.cursor()
            cur.execute("insert into fincas values(%s, %s, %s, %s, %s)",(codigo, nombre, tamano, ciudad, posicion))
            mysql.connection.commit()
            flash("Finca agregada satisfactorimente")
            return redirect("/form/{}".format(table))

    if table == "tierra":
        if request.method == "POST":
            nombre = request.form["nombre"]
            tamano = request.form["tamano"]
            codigofinca = request.form["codigofinca"]
            cur = mysql.connection.cursor()
            cur.execute("insert into tierras values(%s, %s, %s)",(nombre, tamano, codigofinca))
            mysql.connection.commit()
            flash("Tierra agregada satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "cosecha":
        if request.method == "POST":
            idc = request.form["idc"]
            estado = request.form["estado"]
            peso = request.form["peso"]
            fecha = request.form["fecha"]
            descrip = request.form["descrip"]
            factura = request.form["factura"]
            planta = request.form["planta"]
            rotacion = request.form["rotacion"]
            cur = mysql.connection.cursor()
            cur.execute("insert into cosechas values(%s, %s, %s, %s, %s, %s, %s, %s)",
            (idc, estado, peso, fecha, descrip, factura, planta, rotacion))
            mysql.connection.commit()
            flash("Cosecha agregada satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "camion":
        if request.method == "POST":
            matricula = request.form["matricula"]
            marca = request.form["marca"]
            numchasis = request.form["numchasis"]
            fecha = request.form["fecha"]
            observaciones = request.form["observaciones"]
            cur = mysql.connection.cursor()
            cur.execute("insert into camiones values(%s, %s, %s, %s, %s)",
            (matricula, marca, numchasis, fecha, observaciones))
            mysql.connection.commit()
            flash("Camión agregado satisfactoriamente")
            return redirect("/form/{}".format(table))
    
    if table == "ciudad":
        if request.method == "POST":
            codigo = request.form["codigo"]
            nombre = request.form["nombre"]
            cur = mysql.connection.cursor()
            cur.execute("insert into ciudades values(%s, %s)",(codigo, nombre))
            mysql.connection.commit()
            flash("Ciudad agregada satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "cliente":
        if request.method == "POST":
            idc = request.form["idc"]
            nombre1 = request.form["nombre1"]
            nombre2 = request.form["nombre2"]
            apellido1 = request.form["apellido1"]
            apellido2 = request.form["apellido2"]
            cur = mysql.connection.cursor()
            cur.execute("insert into clientes values(%s, %s, %s, %s, %s)",(idc, nombre1, nombre2, apellido1, apellido2))
            mysql.connection.commit()
            flash("Cliente agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "cajon":
        if request.method == "POST":
            idc = request.form["idc"]
            peso = request.form["peso"]
            observaciones = request.form["observaciones"]
            cur = mysql.connection.cursor()
            cur.execute("insert into cajones values(%s, %s, %s)",(idc, peso, observaciones))
            mysql.connection.commit()
            flash("Cajón agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "control-insumo":
        if request.method == "POST":
            idc = request.form["idc"]
            codigoinsu = request.form["codimsu"]
            cantidaden = request.form["cantidaden"]
            cantidadsa = request.form["cantidadsa"]
            fecha = request.form["fecha"]
            cur = mysql.connection.cursor()
            cur.execute("insert into control_insumos values(%s, %s, %s, %s, %s)",(idc, codigoinsu, cantidaden, cantidadsa, fecha))
            mysql.connection.commit()
            flash("Control de Insumo agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "cosecha-cajon":
        if request.method == "POST":
            codcajon = request.form["codcajon"]
            codcosecha = request.form["codcosecha"]
            fecha = request.form["fecha"]
            cur = mysql.connection.cursor()
            cur.execute("insert into cosechas_cajones values(%s, %s, %s)",(codcosecha, codcajon, fecha))
            mysql.connection.commit()
            flash("Cajón de Cosechas agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "eps":
        if request.method == "POST":
            ide = request.form["ide"]
            nombre = request.form["nombre"]
            pagina = request.form["pagina"]
            cur = mysql.connection.cursor()
            cur.execute("insert into eps values(%s, %s, %s)",(ide, nombre, pagina))
            mysql.connection.commit()
            flash("EPS agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "factura":
        if request.method == "POST":
            idf = request.form["idf"]
            precio = request.form["precio"]
            fecha = request.form["fecha"]
            cur = mysql.connection.cursor()
            cur.execute("insert into facturas values(codigo_factu, precio_total, fecha)",(idf, precio, fecha))
            mysql.connection.commit()
            flash("Factura agregada satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "insumo":
        if request.method == "POST":
            idi = request.form["idi"]
            descripcion = request.form["descripcion"]
            nombre = request.form["nombre"]
            finca = request.form["finca"]
            proveedor = request.form["proveedor"]
            cantidad = request.form["cantidad"]
            cur = mysql.connection.cursor()
            cur.execute("insert into insumos values(%s, %s, %s, %s, %s, %s)",(idi, descripcion, nombre, finca, proveedor, cantidad))
            mysql.connection.commit()
            flash("Isumo agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "jornada-insem":
        if request.method == "POST":
            idj = request.form["idj"]
            observaciones = request.form["observaciones"]
            cur = mysql.connection.cursor()
            cur.execute("insert into jornadas_insem values(%s, %s)",(idj, observaciones))
            mysql.connection.commit()
            flash("Jornada de Inseminación agregada satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "mantenimiento":
        if request.method == "POST":
            idm = request.form["idm"]
            matricula = request.form["matricula"]
            fecha = request.form["fecha"]
            cur = mysql.connection.cursor()
            cur.execute("insert into mantenimientos values(%s, %s, %s)",(idm, matricula, fecha))
            mysql.connection.commit()
            flash("Mantenimiento de Camiones agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "mantenimiento-r":
        if request.method == "POST":
            idm = request.form["idm"]
            descripcion = request.form["descripcion"]
            rotacion = request.form["rotacion"]
            fecha = request.form["fecha"]
            cur = mysql.connection.cursor()
            cur.execute("insert into mantenimientos_r values(%s, %s, %s, %s)",(idm, descripcion, rotacion, fecha))
            mysql.connection.commit()
            flash("Mantenimiento de Rotaciones agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "orden-entrega":
        if request.method == "POST":
            ido = request.form["ido"]
            fecha = request.form["fecha"]
            cliente = request.form["cliente"]
            factura = request.form["factura"]
            camion = request.form["camion"]
            observaciones = request.form["observaciones"]
            cur = mysql.connection.cursor()
            cur.execute("insert into ordenes_entrega values(%s, %s, %s, %s, %s, %s)",(ido, fecha, cliente, factura, camion, observaciones))
            mysql.connection.commit()
            flash("Orden de Entrega agregada satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "planta-cacao":
        if request.method == "POST":
            idp = request.form["idp"]
            estado = request.form["estado"]
            descripcion = request.form["descripcion"]
            cur = mysql.connection.cursor()
            cur.execute("insert into plantas_cacao values(%s, %s, %s)",(idp, estado, descripcion))
            mysql.connection.commit()
            flash("Plantación de Cacao agregada satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "proveedor":
        if request.method == "POST":
            idp = request.form["idp"]
            cedula = request.form["cedula"]
            nombre1 = request.form["nombre1"]
            nombre2 = request.form["nombre2"]
            apellido1 = request.form["apellido1"]
            apellido2 = request.form["apellido2"]
            cur = mysql.connection.cursor()
            cur.execute("insert into proveedores values(%s, %s, %s, %s, %s, %s)",(idp, cedula, nombre1, nombre2, apellido1, apellido2))
            mysql.connection.commit()
            flash("Proveedor agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "rotacion":
        if request.method == "POST":
            idr = request.form["idr"]
            numero = request.form["numero"]
            area = request.form["area"]
            canticacao = request.form["canticacao"]
            cantibovino = request.form["cantibovino"]
            tierra = request.form["tierra"]
            capacidad = request.form["capacidad"]
            cur = mysql.connection.cursor()
            cur.execute("insert into rotaciones values(%s, %s, %s, %s, %s, %s, %s)",(idr, numero, area, canticacao, cantibovino, tierra, capacidad))
            mysql.connection.commit()
            flash("Rotacion agregada satisfactoriamente")
            return redirect("/form/{}".format(table))

    if table == "telefono":
        if request.method == "POST":
            numero = request.form["numero"]
            cliente = request.form["cliente"]
            proveedor = request.form["proveedor"]
            empleado = request.form["empleado"]
            eps = request.form["eps"]
            operador = request.form["operador"]
            cur = mysql.connection.cursor()
            cur.execute("insert into telefonos values(%s, %s, %s, %s, %s, %s)",(numero, cliente, proveedor, empleado, eps, operador))
            mysql.connection.commit()
            flash("Telefono agregado satisfactoriamente")
            return redirect("/form/{}".format(table))

@app.route("/delete2/<string:scheme>/<string:cod>/<string:cod2>")
def delete2(scheme,cod,cod2):
    if scheme == "cosecha-cajon":
        cur = mysql.connection.cursor()
        cur.execute("delete from cosechas_cajones where codigo_cos = '{}' and codigo_caj = '{}'".format(cod,cod2))
        mysql.connection.commit()
        flash("Cajón de Cosecha eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from cosechas_cajones")
        data = cur.fetchall()
        return render_template("/Queries/query-cosecha-cajon.html", cosechas = data)

    if scheme == "bovino-jornada":
        cur = mysql.connection.cursor()
        cur.execute("delete from bovinos_jornadas where identi_bovi = '{}' and codi_insem = '{}'".format(cod,cod2))
        cur.connection.commit()
        flash("Jornada de Bovino eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from bovinos_jornadas")
        data = cur.fetchall()
        return render_template("Queries/query-bovino-jornada.html", jornadas = data)

@app.route("/delete/<string:scheme>/<string:cod>")
def delete(scheme,cod):
    if scheme == "empleado":
        cur = mysql.connection.cursor()
        cur.execute("delete from empleados where cod_empl = '{}'".format(cod))
        cur.connection.commit()
        flash("Empleado eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("""select cod_empl, num_identip, puesto, concat(nombree1,' ', ifnull(nombree2, '')), concat(apellidoe1,' ',apellidoe2), 
        salario, titulo_educa, observaciones, licen_condu, fecha_contrato, fecha_naci, ciudad, finca, jefe, eps
        from empleados""")
        data = cur.fetchall()
        return render_template("/Queries/query-empleado.html", empleados = data)
        
    if scheme == "ciudad":
        cur = mysql.connection.cursor()
        cur.execute("delete from ciudades where codi_ciudad = {}".format(cod))
        cur.connection.commit()
        flash("Ciudad eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from ciudades")
        data = cur.fetchall()
        return render_template("/Queries/query-ciudad.html", ciudades = data)

    if scheme == "rotacion":
        cur = mysql.connection.cursor()
        cur.execute("delete from rotaciones where id = {}".format(cod))
        cur.connection.commit()
        flash("Rotación eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from rotaciones")
        data = cur.fetchall()
        return render_template("/Queries/query-rotacion.html", rotacions = data)

    if scheme == "bovino":
        cur = mysql.connection.cursor()
        cur.execute("delete from bovinos where identi_bovi = '{}'".format(cod))
        cur.connection.commit()
        flash("Bovino eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from bovinos")
        data = cur.fetchall()
        return render_template("/Queries/query-bovino.html", bovinos = data)
        
    if scheme == "planta-cacao":
        cur = mysql.connection.cursor()
        cur.execute("delete from plantas_cacao where identi_planta = '{}'".format(cod))
        cur.connection.commit()
        flash("Planta de Cacao eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from plantas_cacao")
        data = cur.fetchall()
        return render_template("/Queries/query-planta-cacao.html", plantas_cacao = data)

    if scheme == "cajon":
        cur = mysql.connection.cursor()
        cur.execute("delete from cajones where codigo_caj = '{}'".format(cod))
        cur.connection.commit()
        flash("Cajón eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from cajones")
        data = cur.fetchall()
        return render_template("/Queries/query-cajon.html", cajones = data)
    
    if scheme == "camion":
        cur = mysql.connection.cursor()
        cur.execute("delete from camiones where matricula = '{}'".format(cod))
        mysql.connection.commit()
        flash("Camión eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from camiones")
        data = cur.fetchall()
        return render_template("/Queries/query-camion.html", camiones = data)

    if scheme == "cliente":
        cur = mysql.connection.cursor()
        cur.execute("delete from clientes where cliente_id = {}".format(cod))
        mysql.connection.commit()
        flash("Cliente eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select cliente_id, concat(nombrec1,' ', ifnull(nombrec2, '')), concat(apellidoc1,' ', apellidoc2) from clientes")
        data = cur.fetchall()
        return render_template("/Queries/query-cliente.html", clientes = data)

    if scheme == "control-insumo":
        cur = mysql.connection.cursor()
        cur.execute("delete from control_insumos where cod = {}".format(cod))
        mysql.connection.commit()
        flash("Control de Insumos eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from control_insumos")
        data = cur.fetchall()
        return render_template("/Queries/query-control-insumo.html", controles = data)

    if scheme == "cosecha":
        cur = mysql.connection.cursor()
        cur.execute("delete from cosechas where codigo_cos = '{}'".format(cod))
        mysql.connection.commit()
        flash("Cosecha eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from cosechas")
        data = cur.fetchall()
        return render_template("/Queries/query-cosecha.html", cosechas = data)

    if scheme == "eps":
        cur = mysql.connection.cursor()
        cur.execute("delete from eps where identi_eps = '{}'".format(cod))
        mysql.connection.commit()
        flash("EPS eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from eps")
        data = cur.fetchall()
        return render_template("/Queries/query-eps.html", epss = data)

    if scheme == "factura":
        cur = mysql.connection.cursor()
        cur.execute("delete from facturas where codigo_factu = '{}'".format(cod))
        mysql.connection.commit()
        flash("Factura eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from facturas")
        data = cur.fetchall()
        return render_template("/Queries/query-factura.html", facturas = data)

    if scheme == "finca":
        cur = mysql.connection.cursor()
        cur.execute("delete from fincas where codi_finca = '{}'".format(cod))
        mysql.connection.commit()
        flash("Finca eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from fincas")
        data = cur.fetchall()
        return render_template("/Queries/query-finca.html", fincas = data)

    if scheme == "insumo":
        cur = mysql.connection.cursor()
        cur.execute("delete from insumos where codi_insu = '{}'".format(cod))
        mysql.connection.commit()
        flash("Insumo eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from insumos")
        data = cur.fetchall()
        return render_template("/Queries/query-insumo.html", insumos = data)

    if scheme == "jornada-insem":
        cur = mysql.connection.cursor()
        cur.execute("delete from jornadas_insem where codi_insem = '{}'".format(cod))
        mysql.connection.commit()
        flash("Jornada de Inseminación eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from jornadas_insem")
        data = cur.fetchall()
        return render_template("/Queries/query-jornada-insem.html", jornadas = data)

    if scheme == "mantenimiento":
        cur = mysql.connection.cursor()
        cur.execute("delete from mantenimientos where codigo_mante = '{}'".format(cod))
        mysql.connection.commit()
        flash("Mantenimiento de Camión eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from mantenimientos")
        data = cur.fetchall()
        return render_template("/Queries/query-mantenimiento.html", mantenimientos = data)

    if scheme == "mantenimiento-r":
        cur = mysql.connection.cursor()
        cur.execute("delete from mantenimientos_r where codigo_man = '{}'".format(cod))
        mysql.connection.commit()
        flash("Mantenimiento de Rotación eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from mantenimientos_r")
        data = cur.fetchall()
        return render_template("/Queries/query-mantenimiento-r.html", mantenimientos = data)

    if scheme == "orden-entrega":
        cur = mysql.connection.cursor()
        cur.execute("delete from ordenes_entrega where id = '{}'".format(cod))
        mysql.connection.commit()
        flash("Ordenes de Entrega eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from ordenes_entrega")
        data = cur.fetchall()
        return render_template("/Queries/query-orden-entrega.html", ordenes = data)

    if scheme == "proveedor":
        cur = mysql.connection.cursor()
        cur.execute("delete from proveedores where codi_identi = '{}'".format(cod))
        mysql.connection.commit()
        flash("Preveedor eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select codi_identi, concat(nombrep1,' ', ifnull(nombrep2, '')), concat(apellidop1,' ', apellidop2) from proveedores")
        data = cur.fetchall()
        return render_template("/Queries/query-proveedor.html", proveedores = data)

    if scheme == "telefono":
        cur = mysql.connection.cursor()
        cur.execute("delete from telefonos where numero = '{}'".format(cod))
        mysql.connection.commit()
        flash("Telefono eliminado satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from telefonos")
        data = cur.fetchall()
        return render_template("/Queries/query-telefono.html", telefonos = data)

    if scheme == "tierra":
        cur = mysql.connection.cursor()
        cur.execute("delete from Tierras where nombre = '{}'".format(cod))
        mysql.connection.commit()
        flash("Tierra eliminada satisfactoriamente")
        cur = mysql.connection.cursor()
        cur.execute("select * from tierras")
        data = cur.fetchall()
        return render_template("/Queries/query-tierra.html", tierras = data)

@app.route("/edit2/<string:table>/<string:cod>/<string:cod2>")
def edit2(table,cod,cod2):
    if table == "bovino-jornada":
        cur = mysql.connection.cursor()
        cur.execute("select * from bovinos_jornadas where identi_bovi = '{}' and codi_insem = '{}'".format(cod,cod2))
        data = cur.fetchall()
        return render_template("/Edits/edit-bovino-jornada.html", tp = table, jornadas = data[0])

    if table == "cosecha-cajon":
        cur = mysql.connection.cursor()
        cur.execute("select * from cosechas_cajones where codigo_cos = '{}' and codigo_caj = '{}'".format(cod,cod2))
        data = cur.fetchall()
        return render_template("/Edits/edit-cosecha-cajon.html", tp = table, cosechas = data[0])

@app.route("/edit/<string:table>/<string:cod>")
def edit(table,cod):
    if table == "empleado":
        cur = mysql.connection.cursor()
        cur.execute("select * from empleados where cod_empl = '{}'".format(cod))
        data = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codi_ciudad, nombre from ciudades")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codi_finca, nombre from fincas")
        data2 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select cod_empl, concat(nombree1,' ',ifnull(nombree2, '')) from empleados where cod_empl like 'ad%'")
        data3 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select identi_eps, nombre from eps")
        data4 = cur.fetchall()
        return render_template("/Edits/edit-empleado.html", tp = table, empleados = data[0], ciudades = data1, fincas = data2, jefes = data3, epss = data4)
        
    if table == "ciudad":
        cur = mysql.connection.cursor()
        cur.execute("select * from ciudades where codi_ciudad = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-ciudad.html", tp = table, ciudades = data[0])

    if table == "rotacion":
        cur = mysql.connection.cursor()
        cur.execute("select * from rotaciones where id = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-rotacion.html", tp = table, rotaciones = data[0])

    if table == "bovino":
        cur = mysql.connection.cursor()
        cur.execute("select * from bovinos where identi_bovi = '{}'".format(cod))
        data = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select identi_bovi, rotacion from bovinos")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codigo_factu, precio_total from facturas")
        data2 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select id, numero from rotaciones")
        data3 = cur.fetchall()
        return render_template("/Edits/edit-bovino.html", tp = table, bovinos = data[0], madres = data1, facturas = data2, rotaciones = data3)
        
    if table == "planta-cacao":
        cur = mysql.connection.cursor()
        cur.execute("select * from plantas_cacao where identi_planta = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-planta-cacao.html", tp = table, plantas_cacao = data[0])

    if table == "cajon":
        cur = mysql.connection.cursor()
        cur.execute("select * from cajones where codigo_caj = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-cajon.html", tp = table, cajones = data[0])
    
    if table == "camion":
        cur = mysql.connection.cursor()
        cur.execute("select * from camiones where matricula = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-camion.html", tp = table, camiones = data[0])

    if table == "cliente":
        cur = mysql.connection.cursor()
        cur.execute("select * from clientes where cliente_id = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-cliente.html", tp = table, clientes = data[0])

    if table == "control-insumo":
        cur = mysql.connection.cursor()
        cur.execute("select * from control_insumos where cod = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-control-insumo.html", tp = table, controles = data[0])

    if table == "cosecha":
        cur = mysql.connection.cursor()
        cur.execute("select * from cosechas where codigo_cos = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-cosecha.html", tp = table, cosechas = data[0])

    if table == "eps":
        cur = mysql.connection.cursor()
        cur.execute("select * from eps where identi_eps = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-eps.html", tp = table, eps = data[0])

    if table == "factura":
        cur = mysql.connection.cursor()
        cur.execute("select * from facturas where codigo_factu = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-factura.html", tp = table, facturas = data[0])

    if table == "finca":
        cur = mysql.connection.cursor()
        cur.execute("select * from fincas where codi_finca = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-finca.html", tp = table, fincas = data[0])

    if table == "insumo":
        cur = mysql.connection.cursor()
        cur.execute("select * from insumos where codi_insu = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-insumo.html", tp = table, insumos = data[0])

    if table == "jornada-insem":
        cur = mysql.connection.cursor()
        cur.execute("select * from jornadas_insem where codi_insem = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-jornada-insem.html", tp = table, jornadas = data[0])

    if table == "mantenimiento":
        cur = mysql.connection.cursor()
        cur.execute("select * from mantenimientos where codigo_mante = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-mantenimiento.html", tp = table, mantenimientos = data[0])

    if table == "mantenimiento-r":
        cur = mysql.connection.cursor()
        cur.execute("select * from mantenimientos_r where codigo_man = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-mantenimiento-r.html", tp = table, mantenimientos = data[0])

    if table == "orden-entrega":
        cur = mysql.connection.cursor()
        cur.execute("select * from ordenes_entrega where id = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-orden-entrega.html", tp = table, ordenes = data[0])

    if table == "proveedor":
        cur = mysql.connection.cursor()
        cur.execute("select * from proveedores where codigo_identi = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-proveedor.html", tp = table, proveedores = data[0])

    if table == "telefono":
        cur = mysql.connection.cursor()
        cur.execute("select * from telefonos where numero = '{}'".format(cod))
        data = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select cliente_id, concat(nombrec1,' ', ifnull(nombrec2, '')) from clientes")
        data1 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select codi_identi, concat(nombrep1,' ', ifnull(nombrep2, '')) from proveedores")
        data2 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select cod_empl, concat(nombree1,' ',ifnull(nombree2, '')) from empleados")
        data3 = cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("select identi_eps, nombre from eps")
        data4 = cur.fetchall()
        return render_template("/Edits/edit-telefono.html", tp = table, telefonos = data[0], clientes = data1, proveedores = data2, empleados = data3, epss = data4)

    if table == "tierra":
        cur = mysql.connection.cursor()
        cur.execute("select * from tierras where nombre = '{}'".format(cod))
        data = cur.fetchall()
        return render_template("/Edits/edit-tierra.html", tp = table, tierras = data[0])

@app.route("/update/<string:scheme>", methods=["POST"])
def update(scheme):
    if scheme == "bovino":
        if request.method == "POST":
            idb = request.form["idb"]
            sexo = request.form["sexo"]
            estado = request.form["estado"]
            estadodes = request.form["estadodes"]
            peso = request.form["peso"]
            fechanac = request.form["fechanac"]
            fecharotacion = request.form["fecharotacion"]
            madre = request.form["madre"]
            factura = request.form["factura"]
            rotacion = request.form["rotacion"]
            cur = mysql.connection.cursor()
            cur.execute("""update bovinos
            set 
            sexo = %s,
            estado_bovi = %s,
            estado = %s,
            peso = %s,
            fecha_nacim = %s,
            fecha_entrada_rotacion = %s,
            madre = %s,
            factura = %s,
            rotacion = %s
            where identi_bovi = %s
            """,
            (sexo, estado, estadodes, peso, fechanac, fecharotacion, madre, factura, rotacion, idb))
            mysql.connection.commit()
            flash("Bovino modificado satisfactoriamente")
            return redirect("/queries/{}".format(scheme))

    if scheme == "empleado":
        if request.method == "POST":
            ide = request.form["codigo"]
            cedula = request.form["dni"]
            puesto = request.form["puesto"]
            nombre1 = request.form["nombre1"]
            nombre2 = request.form["nombre2"]
            apellido1 = request.form["apellido1"]
            apellido2 = request.form["apellido2"]
            salario = request.form["salario"]
            titulo = request.form["titulo"]
            observaciones = request.form["observaciones"]
            licenciacon = request.form["licenciacon"]
            fechacontrato = request.form["fechacontrato"]
            fechanac = request.form["fechanac"]
            ciudad = request.form["ciudad"]
            codigofinca = request.form["codigofinca"]
            jefe = request.form["jefe"]
            eps = request.form["eps"]
            cur = mysql.connection.cursor()
            cur.execute("""update empleados
            set
            num_identip = %s,
            puesto = %s,
            nombree1 = %s,
            nombree2 = %s,
            apellidoe1 = %s,
            apellidoe2 = %s,
            salario = %s,
            titulo_educa = %s,
            observaciones = %s,
            licen_condu = %s,
            fecha_contrato = %s,
            fecha_naci = %s,
            ciudad = %s,
            finca = %s,
            jefe = %s,
            eps = %s
            where cod_empl = %s
            """,
            (cedula, puesto, nombre1, nombre2, apellido1, apellido2, salario, titulo, observaciones, licenciacon, fechacontrato, fechanac, ciudad, codigofinca, jefe, eps, ide))
            mysql.connection.commit()
            flash("Empleado modificado satisfactoriamente")
            return redirect("/queries/{}".format(scheme))

    if scheme == "camion":
        if request.method == "POST":
            matricula = request.form["matricula"]
            marca = request.form["marca"]
            numchasis = request.form["numchasis"]
            fecha = request.form["fecha"]
            observaciones = request.form["observaciones"]
            cur = mysql.connection.cursor()
            cur.execute("""update camiones
            set
            marca = %s,
            num_chasis = %s,
            fecha_adquisicion = %s,
            observaciones = %s
            where matricula = %s
            """,
            (marca, numchasis, fecha, observaciones, matricula))
            mysql.connection.commit()
            flash("Camión modificado satisfactoriamente")
            return redirect("/queries/{}".format(scheme))

    if scheme == "eps":
        if request.method == "POST":
            ide = request.form["ide"]
            nombre = request.form["nombre"]
            pagina = request.form["pagina"]
            cur = mysql.connection.cursor()
            cur.execute("""update eps
            set
            nombre = %s,
            pagina_web = %s
            where identi_eps = %s
            """,(nombre, pagina, ide))
            mysql.connection.commit()
            flash("EPS modificada satisfactoriamente")
            return redirect("/queries/{}".format(scheme))

    if scheme == "telefono":
        if request.method == "POST":
            numero = request.form["numero"]
            cliente = request.form["cliente"]
            proveedor = request.form["proveedor"]
            empleado = request.form["empleado"]
            eps = request.form["eps"]
            operador = request.form["operador"]
            cur = mysql.connection.cursor()
            cur.execute("""update telefonos
            set
            cliente = %s,
            proveedor = %s,
            empleado = %s,
            eps = %s,
            operador = %s
            where numero = %s
            """,(cliente, proveedor, empleado, eps, operador, numero))
            mysql.connection.commit()
            flash("Telefono modificado satisfactoriamente")
            return redirect("/queries/{}".format(scheme))

    if scheme == "jornada-insem":
        if request.method == "POST":
            idj = request.form["idj"]
            observaciones = request.form["observaciones"]
            cur = mysql.connection.cursor()
            cur.execute("""update jornadas_insem
            set observaciones = %s
            where codi_insem = %s
            """,(observaciones, idj))
            mysql.connection.commit()
            flash("Jornada de Inseminación modificada satisfactoriamente")
            return redirect("/queries/{}".format(scheme))

    if scheme == "bovino-jornada":
        if request.method == "POST":
            idbj = request.form["idbj"]
            codigoins = request.form["codigoins"]
            fecha = request.form["fecha"]
            cur = mysql.connection.cursor()
            cur.execute("""update bovinos_jornadas
            set
            fecha = %s
            where identi_bovi = %s and codi_insem = %s
            """,
            (fecha, idbj, codigoins))
            mysql.connection.commit()
            flash("Jornada de Bovinos modificada satisfactorimente")
            return redirect("/queries/{}".format(scheme))

@app.route("/reports/<string:scheme>")
def report(scheme):

    if scheme == "report-1":
        cur = mysql.connection.cursor()
        cur.execute("""
        Select
        bov.identi_bovi,
        fin.nombre,
        fac.fecha,
        fac.codigo_factu,
        ord.camion,
        ord.cliente,
        ord.fecha_entrega_orden
        From
        ordenes_entrega ord
        inner join facturas fac on (ord.factura = fac.codigo_factu)
        inner join bovinos bov on (bov.factura = fac.codigo_factu)
        inner join rotaciones r on (bov.rotacion = r.id)
        inner join tierras t on (r.tierra = t.nombre)
        inner join fincas fin on (t.codi_finca = fin.codi_finca)
        """)
        data = cur.fetchall() 
        return render_template("/Reports/report-1.html", reports = data)

    if scheme == "report-2":
        cur = mysql.connection.cursor()
        cur.execute("""
        Select
        cos.codigo_cos,
        fin.nombre,
        fac.fecha,
        fac.codigo_factu,
        ord.camion,
        ord.cliente,
        ord.fecha_entrega_orden
        From
        ordenes_entrega ord
        inner join facturas fac on (ord.factura = fac.codigo_factu)
        inner join cosechas cos on (cos.factura = fac.codigo_factu)
        inner join rotaciones rot on (cos.rotacion = rot.id)
        inner join tierras tie on (rot.tierra = tie.nombre)
        inner join fincas fin on (tie.codi_finca = fin.codi_finca)
        """)
        data = cur.fetchall() 
        return render_template("/Reports/report-2.html", reports = data)

    if scheme == "report-3":
        cur = mysql.connection.cursor()
        cur.execute("""
        Select
        bov.identi_bovi,
        bov.estado,
        concat(rot.tierra, ' ', rot.numero),
        timestampdiff(year, bov.fecha_nacim, curdate()),
        fin.nombre
        From
        Bovinos bov
        inner join rotaciones rot on (bov.rotacion = rot.id)
        inner join tierras tie on (rot.tierra = tie.nombre)
        inner join fincas fin on (tie.codi_finca = fin.codi_finca)
        where bov.estado_bovi = "Pr"
        """)
        data = cur.fetchall() 
        return render_template("/Reports/report-3.html", reports = data)

    if scheme == "report-4":
        cur = mysql.connection.cursor()
        cur.execute("""
        Select
        insu.codi_insu,
        insu.nombre,
        insu.descripcion,
        insu.cant_total,
        pro.num_identip,
        concat (pro.nombrep1, ' ', pro.apellidop1),
        tel.numero,
        fin.nombre
        From
        insumos insu
        inner join proveedores pro on (insu.proveedor = pro.codi_identi)
        inner join telefonos tel on (tel.proveedor = pro.codi_identi)
        inner join fincas fin on (insu.finca = fin.codi_finca)
        order by insu.codi_insu
        """)
        data = cur.fetchall() 
        return render_template("/Reports/report-4.html", reports = data)

    if scheme == "report-5":
        cur = mysql.connection.cursor()
        cur.execute("""
        Select
        empl.num_identip as Cedula,
        concat(empl.nombree1, ' ', empl.apellidoe1),
        timestampdiff(year, empl.fecha_naci, curdate()),
        timestampdiff(year, empl.fecha_contrato, curdate()),
        fin.nombre,
        empl.puesto,
        empl.jefe,
        tel.numero
        From
        empleados empl
        inner join fincas fin on (empl.finca = fin.codi_finca)
        inner join telefonos tel on (tel.empleado = empl.cod_empl)
        """)
        data = cur.fetchall() 
        return render_template("/Reports/report-5.html", reports = data)

    if scheme == "report-6":
        cur = mysql.connection.cursor()
        cur.execute("""
        Select
        cos.codigo_cos,
        bovi.identi_bovi,
        cos.peso,
        bovi.peso,
        fin.nombre,
        factu.codigo_factu,
        factu.fecha,
        ord.camion,
        ord.fecha_entrega_orden,
        ord.cliente
        From
        ordenes_entrega ord
        inner join clientes clien on (ord.cliente = clien.cliente_id)
        inner join facturas factu on (ord.factura = factu.codigo_factu)
        inner join bovinos bovi on (bovi.factura = factu.codigo_factu)
        inner join cosechas cos on (cos.factura = factu.codigo_factu)
        inner join rotaciones rot on (bovi.rotacion = rot.id)
        inner join tierras tie on (rot.tierra = tie.nombre)
        inner join fincas fin on (tie.codi_finca = fin.codi_finca)
        """)
        data = cur.fetchall() 
        return render_template("/Reports/report-6.html", reports = data)


@app.route("/queries/<string:scheme>")
def query(scheme):
    if scheme == "empleado":
        cur = mysql.connection.cursor()
        cur.execute("""select cod_empl, num_identip, puesto, concat(nombree1,' ', ifnull(nombree2, '')), concat(apellidoe1,' ',apellidoe2), 
        salario, titulo_educa, observaciones, licen_condu, fecha_contrato, fecha_naci, ciudad, finca, jefe, eps
        from empleados""")
        data = cur.fetchall()
        return render_template("/Queries/query-empleado.html", empleados = data)
        
    if scheme == "ciudad":
        cur = mysql.connection.cursor()
        cur.execute("select * from ciudades")
        data = cur.fetchall()
        return render_template("/Queries/query-ciudad.html", ciudades = data)

    if scheme == "rotacion":
        cur = mysql.connection.cursor()
        cur.execute("select * from rotaciones")
        data = cur.fetchall()
        return render_template("/Queries/query-rotacion.html", rotaciones = data)

    if scheme == "bovino":
        cur = mysql.connection.cursor()
        cur.execute("select * from bovinos")
        data = cur.fetchall()
        return render_template("/Queries/query-bovino.html", bovinos = data)
        
    if scheme == "planta-cacao":
        cur = mysql.connection.cursor()
        cur.execute("select * from plantas_cacao")
        data = cur.fetchall()
        return render_template("/Queries/query-planta-cacao.html", plantas_cacao = data)

    if scheme == "bovino-jornada":
        cur = mysql.connection.cursor()
        cur.execute("select * from bovinos_jornadas")
        data = cur.fetchall()
        return render_template("/Queries/query-bovino-jornada.html", jornadas = data)

    if scheme == "cajon":
        cur = mysql.connection.cursor()
        cur.execute("select * from cajones")
        data = cur.fetchall()
        return render_template("/Queries/query-cajon.html", cajones = data)
    
    if scheme == "camion":
        cur = mysql.connection.cursor()
        cur.execute("select * from camiones")
        data = cur.fetchall()
        return render_template("/Queries/query-camion.html", camiones = data)

    if scheme == "cliente":
        cur = mysql.connection.cursor()
        cur.execute("""select cliente_id, concat(nombrec1,' ', ifnull(nombrec2, '')), concat(apellidoc1,' ', apellidoc2) from clientes""")
        data = cur.fetchall()
        return render_template("/Queries/query-cliente.html", clientes = data)

    if scheme == "control-insumo":
        cur = mysql.connection.cursor()
        cur.execute("select * from control_insumos")
        data = cur.fetchall()
        return render_template("/Queries/query-control-insumo.html", controles = data)

    if scheme == "cosecha":
        cur = mysql.connection.cursor()
        cur.execute("select * from cosechas")
        data = cur.fetchall()
        return render_template("/Queries/query-cosecha.html", cosechas = data)

    if scheme == "cosecha-cajon":
        cur = mysql.connection.cursor()
        cur.execute("select * from cosechas_cajones")
        data = cur.fetchall()
        return render_template("/Queries/query-cosecha-cajon.html", cosechas = data)

    if scheme == "eps":
        cur = mysql.connection.cursor()
        cur.execute("select * from eps")
        data = cur.fetchall()
        return render_template("/Queries/query-eps.html", epss = data)

    if scheme == "factura":
        cur = mysql.connection.cursor()
        cur.execute("select * from facturas")
        data = cur.fetchall()
        return render_template("/Queries/query-factura.html", facturas = data)

    if scheme == "finca":
        cur = mysql.connection.cursor()
        cur.execute("select * from fincas")
        data = cur.fetchall()
        return render_template("/Queries/query-finca.html", fincas = data)

    if scheme == "insumo":
        cur = mysql.connection.cursor()
        cur.execute("select * from insumos")
        data = cur.fetchall()
        return render_template("/Queries/query-insumo.html", insumos = data)

    if scheme == "jornada-insem":
        cur = mysql.connection.cursor()
        cur.execute("select * from jornadas_insem")
        data = cur.fetchall()
        return render_template("/Queries/query-jornada-insem.html", jornadas = data)

    if scheme == "mantenimiento":
        cur = mysql.connection.cursor()
        cur.execute("select * from mantenimientos")
        data = cur.fetchall()
        return render_template("/Queries/query-mantenimiento.html", mantenimientos = data)

    if scheme == "mantenimiento-r":
        cur = mysql.connection.cursor()
        cur.execute("select * from mantenimientos_r")
        data = cur.fetchall()
        return render_template("/Queries/query-mantenimiento-r.html", mantenimientos = data)

    if scheme == "orden-entrega":
        cur = mysql.connection.cursor()
        cur.execute("select * from ordenes_entrega")
        data = cur.fetchall()
        return render_template("/Queries/query-orden-entrega.html", ordenes = data)

    if scheme == "proveedor":
        cur = mysql.connection.cursor()
        cur.execute("select codi_identi, concat(nombrep1,' ', ifnull(nombrep2, '')), concat(apellidop1,' ', apellidop2) from proveedores")
        data = cur.fetchall()
        return render_template("/Queries/query-proveedor.html", proveedores = data)

    if scheme == "telefono":
        cur = mysql.connection.cursor()
        cur.execute("select * from telefonos")
        data = cur.fetchall()
        return render_template("/Queries/query-telefono.html", telefonos = data)

    if scheme == "tierra":
        cur = mysql.connection.cursor()
        cur.execute("select * from tierras")
        data = cur.fetchall()
        return render_template("/Queries/query-tierra.html", tierras = data)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
