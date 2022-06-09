from DB.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print('''

----------- MENU PRINCIPAL -----------
                    
1- Listar Cursos
2- Registrar Curso
3- Actualizar Curso
4- Eliminar Curso
5- Salir

--------------------------------------

''')
            opcion = input('Seleccione una opcion: ')

            if opcion.isdigit():
                opcion = int(opcion)
                if opcion < 1 or opcion > 5:
                    input('opcion incorrecta, intente nuevamente...')
                elif opcion == 5:
                    continuar = False
                    input('Greacias por usar este sistema...')
                    break
                else:
                    opcionCorrecta = True
                    ejecutarOpcion(opcion)
            else:
                input('opcion incorrecta, intente nuevamente...')

def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            cursos=dao.listarCursos()
            if len(cursos)>0:
                funciones.listarCursos(cursos)
            else:
                print('No se encontraron cursos')
        except:
            print('ocurrio un error')
    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except:
            print('ocurrio un error') 
    elif opcion == 3:
        try:
            cursos=dao.listarCursos()
            if len(cursos)>0:
                curso = funciones.pedirDatosActualizacion(cursos)
                if curso:
                    dao.actualizarCurso(curso)
                else:
                    print('Codigo de curso a actualizar no encontrado...')
            else:
                print('No se encontraron cursos')
        except:
            print('ocurrio un error')
    elif opcion == 4:
        try:
            cursos=dao.listarCursos()
            if len(cursos)>0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar==""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print('Codigo de curso no encontrado...\n') 
            else:
                print('No se encontraron cursos')
        except:
            print('ocurrio un error')
    else:
        print('Opcion no valida...')

menuPrincipal()