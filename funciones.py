



def listarCursos(cursos):
    print('\n Cursos: \n')
    contador=1
    for cur in cursos:
        datos='{0}. Codigo: {1} | Nombre: {2} ({3} creditos)'
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador+=1
    print(' ')

def pedirDatosRegistro():
    codigoCorrecto=False
    while(not codigoCorrecto):
        codigo=input('Ingrese Codigo: ')
        if len(codigo) == 6:
            if codigo.isdigit():
                codigo = int(codigo)
                codigoCorrecto = True
            else:
                input('opcion incorrecta, intente nuevamente...')
        else:
            input('Codigo Incorrecto, debe tener 6 digitos')
    nombre=input('Ingrese Nombre: ')
    creditosCorrecto=False
    while(not creditosCorrecto):
        creditos=input('Ingrese Creditos: ')
        if creditos.isdigit():
            if int(creditos) >0:
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                input('Los creditos deben ser mayor a 0')
        else:
            input('creditos incorrectos, debe ser un numero...')

    curso=(codigo, nombre, creditos)
    return curso

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigoEditar=input('Ingrese el codigo del curso a editar: ')
        if codigoEditar.isdigit():
            codigoCorrecto = True
            codigoEditar = int(codigoEditar)
            for cur in cursos:
                if cur[0] == codigoEditar:
                    existeCodigo = True
                    break

            if existeCodigo:
                nombre=input('Ingrese Nombre a modificar: ')
                creditosCorrecto=False
                while(not creditosCorrecto):
                    creditos=input('Ingrese Creditos a modificar: ')
                    if creditos.isdigit():
                        if int(creditos) >0:
                            creditosCorrecto = True
                            creditos = int(creditos)
                        else:
                            input('Los creditos deben ser mayor a 0')
                    else:
                        input('creditos incorrectos, debe ser un numero...')
                curso = (codigoEditar, nombre, creditos)
            else:
                curso=None

            return curso
        else:
            print('Ingrese un numero...')

def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoCorrecto=False
    while(not codigoCorrecto):
        codigoEliminar=input('Ingrese el codigo del curso a eliminar: ')
        if codigoEliminar.isdigit():
            codigoCorrecto = True
            codigoEliminar = int(codigoEliminar)
            for cur in cursos:
                if cur[0] == codigoEliminar:
                    existeCodigo = True
                    break

            if not existeCodigo:
                codigoEliminar = ""

            return codigoEliminar
        else:
            print('Ingrese un numero...')