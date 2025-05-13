import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")


#ANTES DE FILTRAR COMO ANALISTAS DE DATOS DEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
#print(dataFrameAsistencia['estado'].unique())
#print(dataFrameAsistencia['estrato'].unique())
#print(dataFrameAsistencia['medio_transporte'].unique())


#FILTROS Y CONDICIONES PARA TRANSOFRMAR DATOS
#1. Reportar todos los estudiantes que asistieron
estudiantesQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')
#print(estudiantesQueAsistieron)
#2. Reportar todos los estudiantes que faltaron
estudiantesQueFaltaron=dataFrameAsistencia.query('estado=="inasistencia"')

#3. Reportar todos los estudiantes que llegaron tarde(Justificado)
estudiantesQueLlegaronTarde=dataFrameAsistencia.query('estado=="justificado"')

#4. Reportar todos los estudiantes de estrato 1
estudiantesEstratoUno=dataFrameAsistencia.query('estrato==1')

#5. Reportar todos los estudiantes de estratos altos
estudiantesEstratosAltos=dataFrameAsistencia.query('estrato>=5')

#6. Reportar todos los estudiantes que llegan en metro
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')

#7. Reportar todos los estudiantes que llegan en bicicleta
estudiantesQueUsanBicicleta=dataFrameAsistencia.query('medio_transporte=="bicicleta"')

#8. Reportar todos los estudiantes que no caminan para llegar a la u
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')

#9. Reportar todos los registros de asistencia del mes de junio
estudiantesJunio=dataFrameAsistencia.query('fecha.str.contains("2023-06")', engine='python') 

#10. Reportar los estudaintes que faltaron y usan bus para llegar a la u
estudiantesQueFaltanUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasistencia"')
#print(estudiantesQueFaltanUsanBus)
#11. Reportar estudiantes que usan bus y son de estratos altos
estudiantesEstratosAltosUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estrato>=5')

#12. Reportar estudiantes que usan bus y son de estratos bajos
estudiantesEstratosBajosUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estrato<=3')

#13. Reportar estudiantes que llegan tarde y son de estrato 3,4,5 o 6
estudiantesQueLleganTardeEstratosMedios=dataFrameAsistencia.query('estado=="justificado" and estrato>=3 and estrato<=6')

#14. Reportar estudiantes que usan transportes ecologicos 
estudiantesTransporteEcologico=dataFrameAsistencia.query('medio_transporte=="bicicleta" or medio_transporte=="a pie"')

#15. Reportar estudiantes que faltan y usan carro para transportarse
estudiantesQueFaltanUsanCarro=dataFrameAsistencia.query('medio_transporte=="carro" and estado=="inasistencia"')

#16. Reportar estudiantes que asisten son estratos altos y caminan
estudiantesEstratosAltosCaminan=dataFrameAsistencia.query('estado=="asistio" and estrato>=5 and medio_transporte=="a pie"')

#17. Reportar estudiantes que son estratos bajos y justifican su iniasistencia
estudiantesEstratosBajosJustifican=dataFrameAsistencia.query('estado=="justificado" and estrato<=3')

#18. Reportar estudiantes que son estratos altos y justifican su iniasistencia
estudiantesEstratosAltosJustifican=dataFrameAsistencia.query('estado=="justificado" and estrato>=5')

#19. Reportar estudiantes que usan carro y justifican su inasistencia
estudiantesQueUsanCarroJustifican=dataFrameAsistencia.query('estado=="justificado" and medio_transporte=="carro"')

#20. Reportar estudiantes que faltan y usan metro y son estratos medios
estudiantesQueFaltanUsanMetroEstratosMedios=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="metro" and estrato>=3 and estrato<=5')





#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. Contar cada registro de asistencia por cada estado
conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()

#2. Numero de registros por estrato
conteoRegistrosPorEstrato=dataFrameAsistencia.groupby('estrato').size()

#3. Cantidad de estudiantes por medio de transporte
conteoRegistrosPorMedioTransporte=dataFrameAsistencia.groupby('medio_transporte').size()

#4. Cantidad de registros por grupo
conteoRegistrosPorGrupo=dataFrameAsistencia.groupby('id_grupo').size()

#5. Cruce entre estado y medio de transporte
cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()


#6. Promedio de estrato por estado de asistencia
promedioEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()


#7. Estrato promedio por medio de transporte
promedioEstratoPorMedioTransporte=dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean()

#8. Maximo estrato por estado de asistencia
maximoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].max()

#9. Minimo estrato por estado de asistencia
minimoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].min()

#10.Conteo de asistencias por grupo y por estado
conteoAsistenciasPorGrupoEstado=dataFrameAsistencia.groupby(['id_grupo','estado']).size()

#11. Transporte usado por cada grupo
transporteUsadoPorGrupo=dataFrameAsistencia.groupby('id_grupo')['medio_transporte'].unique()

#12. cuantos grupos distintos registraron asistencia por fecha
conteoGruposPorFecha=dataFrameAsistencia.groupby('fecha')['id_grupo'].nunique()

#13. Promedio de estrato por fecha
promedioEstratoPorFecha=dataFrameAsistencia.groupby('fecha')['estrato'].mean()

#14. Numero de tipos de estado por transporte
conteoTiposEstadoPorTransporte=dataFrameAsistencia.groupby('medio_transporte')['estado'].nunique()

#15. Primer Registro de cada grupo
primerRegistroPorGrupo=dataFrameAsistencia.groupby('id_grupo').first()

#print(primerRegistroPorGrupo)