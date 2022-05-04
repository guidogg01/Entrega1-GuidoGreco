# Las funcionalidades están en las pestañas de la página, que son las siguientes:
# - Inicio (que envía al inicio de la página). En esta aparece un h1 con "Mi primera página web con Django".
# - Cursos que además de indicarte con un h1 que "Estos son los cursos!", se muestra un formulario a complear abajo utilizando el "POST" para poder añadir cursos con número y la duración del mismo en la base de datos. Aclaración: Cuando se agrega un Curso en el formulario lleva al usuario automaticamente a la página de incio.
# - Estudiante. En esta pestaña aparece el mensaje (con h2) "Estos son los estudiantes de la camada de CoderHouse.".
# - Entregable. En esta pestaña aparece el mensaje (con h2) "Aquí se ponen las fechas de los entregables."
# - Profesor. En esta pestaña aparece el mensaje (con h1) "Estos son los profesores!!" con un style "Rojo", por eso aparece el mensaje en Rojo.
# - Para poder solicitar datos y utilizar el "GET", se debe entrar a http://127.0.0.1:8000/AppCoder/busquedaCamada/ e ingresar el número de la camada que desea encontrar. Esto se puede encontrar en el código en la sección de views, y en def buscar(request) explica como funciona el mismo con sus propios comentarios.
# - Por último se creo un usuario para el tutor Jonatan Canchi, con la siguiente información:
# Nombre de usuario: Jonatan-Canchi
# Contraseña: CoderHouse1234
# El mismo es SuperUsario y pertenece al staf además de contar con todos los permisos y podes hacer cualquier cosa dentro de la página.
