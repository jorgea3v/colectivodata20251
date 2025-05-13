import pandas as pd
from datetime import datetime
dataFrameUsuarios=pd.read_excel("./data/usuarios_sistema_completo.xlsx")

# 🔧 LIMPIEZA GENERAL
dataFrameUsuarios["tipo_usuario"] = dataFrameUsuarios["tipo_usuario"].fillna("").astype(str)
dataFrameUsuarios["direccion"] = dataFrameUsuarios["direccion"].fillna("").astype(str)
dataFrameUsuarios["especialidad"] = dataFrameUsuarios["especialidad"].fillna("").astype(str)
dataFrameUsuarios["fecha_nacimiento"] = pd.to_datetime(dataFrameUsuarios["fecha_nacimiento"], errors="coerce")


# 1. Solo estudiantes
solo_estudiantes = dataFrameUsuarios.query("tipo_usuario == 'estudiante'")
#print(solo_estudiantes)
# 2. Solo profesores (asegúrate de que el valor sea "docente" si ese es el estándar)
profesores = dataFrameUsuarios.query("tipo_usuario == 'docente'")
#print(profesores)
# 3. Todos excepto estudiantes
todos_excepto_estudiantes = dataFrameUsuarios.query("tipo_usuario != 'estudiante'")
#print(todos_excepto_estudiantes)

# 4. Filtrar por especialidad (ejemplo: 'ingenieria de sistemas')
especialidad = dataFrameUsuarios.query("especialidad == 'Ingeniería de Sistemas'")
#print(especialidad)
# 5. Excluir una especialidad
especialidad_excluida = dataFrameUsuarios.query("especialidad != 'Ingeniería Civil'") #FALTA ESTA
#print(especialidad_excluida)
# 6. Excluir administrativos
sin_administrativos = dataFrameUsuarios.query("tipo_usuario != 'administrativo'")
#print(sin_administrativos)

# 7. Direcciones en Medellín
direcciones_medellin = dataFrameUsuarios.query("direccion.str.contains('Medellín', case=False)", engine="python")
#print(direcciones_medellin)

# 8. Direcciones terminadas en sur
direcciones_sur = dataFrameUsuarios.query("direccion.str.endswith('Sur')", engine="python")
#print(direcciones_sur)

# 9. Direcciones que inician con calle
direcciones_calle = dataFrameUsuarios.query("direccion.str.startswith('Calle')", engine="python")
#print(direcciones_calle)

# 10. Especialidades que contienen la palabra datos
especialidades_datos = dataFrameUsuarios.query("especialidad.str.contains('Datos', case=False)", engine="python")
#print(especialidades_datos)

# 11. Instructores en Itagüí
instructores_itagui = dataFrameUsuarios.query("tipo_usuario == 'instructor' and direccion.str.contains('itagui', case=False)", engine="python")
#print(instructores_itagui)

# 12. Nacidos después del año 2000
nacidos_despues_2000 = dataFrameUsuarios.query("fecha_nacimiento > '2000-12-31'")
#print(nacidos_despues_2000)

# 13. Nacidos en los 90
nacidos_en_los_90 = dataFrameUsuarios.query("fecha_nacimiento >= '1990-01-01' and fecha_nacimiento <= '1999-12-31'")
#print(nacidos_en_los_90)

# 14. Direcciones en Envigado
direcciones_envigado = dataFrameUsuarios.query("direccion.str.contains('envigado', case=False)", engine="python")
#print(direcciones_envigado)

# 15. Especialidades que empiezan por I
especialidades_i = dataFrameUsuarios.query("especialidad.str.startswith('I')", engine="python")
#print(especialidades_i)

# 16. Usuarios sin dirección
usuarios_sin_direccion = dataFrameUsuarios.query("direccion == ''")
#print(usuarios_sin_direccion)

# 17. Usuarios sin especialidad
usuarios_sin_especialidad = dataFrameUsuarios.query("especialidad == ''")
#print(usuarios_sin_especialidad)

# 18. Profesores que viven en Sabaneta (asegúrate de que tipo_usuario sea 'docente')
profesores_sabaneta = dataFrameUsuarios.query("tipo_usuario == 'docente' and direccion.str.contains('sabaneta', case=False)", engine="python")
#print(profesores_sabaneta)

# 19. Aprendices que viven en Bello (si usas 'estudiante' como tipo_usuario)
aprendices_bello = dataFrameUsuarios.query("tipo_usuario == 'estudiante' and direccion.str.contains('bello', case=False)", engine="python")
#print(aprendices_bello)

# 20. Nacidos en el nuevo milenio (2000 en adelante)
nacidos_nuevo_milenio = dataFrameUsuarios.query("fecha_nacimiento >= '2000-01-01'")
#print(nacidos_nuevo_milenio)

# Calcular edad
dataFrameUsuarios["edad"] = datetime.now().year - dataFrameUsuarios["fecha_nacimiento"].dt.year

# 1. Total por tipo
totalPorTipo = dataFrameUsuarios.groupby("tipo_usuario").size().reset_index(name="total")
#print(totalPorTipo)

# 2. Total por especialidad
totalPorEspecialidad = dataFrameUsuarios.groupby("especialidad").size().reset_index(name="total")
#print(totalPorEspecialidad)

# 3. Cantidad de especialidades distintas
cantidadEspecialidadesDistintas = dataFrameUsuarios["especialidad"].nunique()
#print(cantidadEspecialidadesDistintas)

# 4. Tipos de usuario por especialidad
tiposPorEspecialidad = dataFrameUsuarios.groupby("especialidad")["tipo_usuario"].unique().reset_index()
#print(tiposPorEspecialidad)

# 5. Usuario más antiguo por tipo
usuariosConFecha = dataFrameUsuarios.dropna(subset=["fecha_nacimiento"])
usuarioMasAntiguoPorTipo = usuariosConFecha.loc[usuariosConFecha.groupby("tipo_usuario")["fecha_nacimiento"].idxmin()]
#print(usuarioMasAntiguoPorTipo)

# 6. Usuario más joven por tipo
usuarioMasJovenPorTipo = usuariosConFecha.loc[usuariosConFecha.groupby("tipo_usuario")["fecha_nacimiento"].idxmax()]
#print(usuarioMasJovenPorTipo)

# 7. Primer registro por tipo (igual al más antiguo)
primerRegistroPorTipo = usuarioMasAntiguoPorTipo.copy()
#print(primerRegistroPorTipo)

# 8. Último registro por tipo (igual al más joven)
ultimoRegistroPorTipo = usuarioMasJovenPorTipo.copy()
#print(ultimoRegistroPorTipo)
# 9. Combinación tipo por especialidad
combinacionTipoEspecialidad = dataFrameUsuarios.groupby(["tipo_usuario", "especialidad"]).size().reset_index(name="total")
#print(combinacionTipoEspecialidad)

# 10. El más viejo por especialidad
usuarioMasViejoPorEspecialidad = usuariosConFecha.loc[
    usuariosConFecha.groupby("especialidad")["fecha_nacimiento"].idxmin()
]
#print(usuarioMasViejoPorEspecialidad)

# 11. Cuántos de cada especialidad por tipo
cantidadEspecialidadPorTipo = combinacionTipoEspecialidad.copy()
#print(cantidadEspecialidadPorTipo)

# 12. Edad promedio por tipo
edadPromedioPorTipo = dataFrameUsuarios.groupby("tipo_usuario")["edad"].mean().reset_index(name="edad_promedio")
#print(edadPromedioPorTipo)

# 13. Años de nacimiento más frecuente por especialidad
dataFrameUsuarios["anio_nacimiento"] = dataFrameUsuarios["fecha_nacimiento"].dt.year
anioMasFrecuentePorEspecialidad = dataFrameUsuarios.groupby("especialidad")["anio_nacimiento"].agg(
    lambda x: x.mode().iloc[0] if not x.mode().empty else None
).reset_index(name="anio_nacimiento_mas_frecuente")
#print(anioMasFrecuentePorEspecialidad)

# 14. Mes de nacimiento más frecuente por tipo
dataFrameUsuarios["mes_nacimiento"] = dataFrameUsuarios["fecha_nacimiento"].dt.month
mesMasFrecuentePorTipo = dataFrameUsuarios.groupby("tipo_usuario")["mes_nacimiento"].agg(
    lambda x: x.mode().iloc[0] if not x.mode().empty else None
).reset_index(name="mes_nacimiento_mas_frecuente")
#print(mesMasFrecuentePorTipo)