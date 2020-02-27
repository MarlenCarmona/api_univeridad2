if (data['action']=='buscar'):
    inf={}
    inf['version']="0.01"
    inf['status']="200 ok"
    matricula=str(data['matricula'])
    result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
    with open('static/csv/alumnos.csv','r') as csvfile:
        reader = csv.DictReader(csvfile)
        result = []
        for row in reader:
            if(row['matricula']==matricula):
                resulta={}
                resulta['matricula']=str(row['matricula'])
                resulta['nombre']=str(row['nombre'])
                resulta['primer_apellido']=str(row['primer_apellido'])
                resulta['segundo_apellido']=str(row['segundo_apellido'])
                resulta['carrera']=str(row['carrera'])
                result.append(resulta)
            inf['alumno']=result
        return json.dumps(inf)

