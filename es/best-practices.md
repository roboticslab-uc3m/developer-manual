# Buenas prácticas

## Haciendo preguntas
* **Siempre, cuando tengas una duda, busca en nuestra **[**wiki**](http://robots.uc3m.es/)**, y busca entre las issues \(tanto abiertas como cerradas\) del repositorio asociado a tu trabajo.** Si no encuentras respuesta, **pon una issue en el repositorio asociado a tu trabajo (o en [QA](https://github.com/roboticslab-uc3m/questions-and-answers) si es extremadamente genérico) o comenta en la pestaña de Discussion de la wiki**. Ventajas:
  * Incrementa la productividad global, porque queda el histórico. Se tiende a evitar el estar repetiendo las mismas preguntas y generando las mismas respuestas.
  * Sirve de herramienta para tratar de mantener lo técnico dentro del contexto técnico, y a centrarse la temática indicada en el asunto de la issue.
  * Da mayor visibilidad a tu duda, te puede contestar gente que no te esperarías. Esto es especialmente interesante cuando hay un desacuerdo entre dos partes: pueden intervenir terceros que aporten nuevas ideas y puntos de vista.
* Tratamos de unificar las etiquetas (labels) para preguntas en GitHub, con [teo-main](https://github.com/roboticslab-uc3m/teo-main/labels) como inspiración.

## Control de versiones
* **Siempre, para cualquier archivo de trabajo, por muy insignificante o borrador que parezca,** utiliza uno de los repositorios compartidos:
  * Software y hardware: [GitHub \(GIT, público\)](https://github.com/roboticslab-uc3m). Utilizamos [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow/) como workflow de git \(excepto para repos de documentación pura, ver [\#6](https://github.com/roboticslab-uc3m/best-practices/issues/6)\) con [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) y [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration). Consulta con tu tutor \(que posiblemente te redirija a [Juan](https://github.com/jgvictores), [David](https://github.com/David-Estevez) o [Raúl](https://github.com/rsantos88)\) si dudas en qué repositorio trabajar. Acomoda tu [.gitignore](https://git-scm.com/docs/gitignore) al tipo de proyecto, para evitar subir ficheros que no se deberían \(binarios, backups, y ficheros residuales varios\).
  * Redacción de publicaciones: consulta con tu tutor \(que posiblemente te redirija a [Juan](https://github.com/jgvictores)\) para la URL exacta, distribuidos a través de [http://robots.uc3m.es/svn/\*](http://robots.uc3m.es/svn/*) \(SVN, privado\).

## Nombrar y documentar en general
* La forma preferida de documentación \(salvo Doxygen para C/C++\) es Markdown.
* La forma preferida para nombrar los archivos en `/doc` es _kebab-case_.

## Programación en general
* Si tienes problemas con la instalación de las dependencias o de algún software adicional, consulta primero nuestro [repositorio dedicado](https://www.gitbook.com/book/roboticslab-uc3m/installation-guides/details).
* Si incorporas una dependencia o algún software adicional, consulta primero nuestro [repositorio dedicado](https://www.gitbook.com/book/roboticslab-uc3m/installation-guides/details). Si no está ahí, considera si buena opción tomando como criterios recomendados (aunque no obligatorios) el que sea ligero, flexible y multiplataforma. Siendo una buena opción, agrégalo ahí, despues enlázalo con tu proyecto ([ejemplo](5182f9f475e229acea4cca1130be57489fd6b0f7)).
* Respeta las sangrías/indentaciones... como si todo fuese Python! ;-\) PD: Existe un programa que autoajusta, que se llama [astyle](http://astyle.sourceforge.net/) \(utilizar con precaución!\).
* NO utilizar NÚMEROS en nombres de ficheros para indicar versiones/intentos/iteraciones... ¡Para eso ya existen los hash y tag de los sistemas de control de versiones!
* NO crear DUPLICADOS de programas. Analizar en profundidad si se puede ampliar la funcionalidad de un programa a través del ajuste o incorporación de parámetros antes de crear un programa nuevo. Una vez detectado que se puede ampliar la funcionalidad de un programa, utilizar los mecanismos convencionales \(issues, o fork y pull request\).
* Todo `toDo`, `fixMe`, etc. en el código debe estar asociado a una _issue abierta_ \(referenciado bidireccionalmente\).
* [Cabeceras, ficheros de configuración y parámetros de CLI](https://github.com/roboticslab-uc3m/asibot-main/blob/develop/doc/asibot-post-install.md#changing-parameters).
* Lee acerca de [Clean code](https://www.google.es/search?q=cleancode).

## Programación CMake
* Convenciones de nombres:
  * *SCREAMING\_SNAKE\_CASE* para el nombre del proyecto y las variables de configuración: `TEO_MAIN`, `TEO_MAIN_LINK_DIRS`.
  * *kebab-case* para los directorios de instalación de contextos de YARP creados por `yarp_configure_external_installation()`: `teo-main`, `asibot-openrave-models`.
  * Utiliza el prefijo `ROBOTICSLAB_` (o `roboticslab-`) siempre que no sea posible garantizar la unicidad del nombre elegido para el proyecto (ten en cuenta que querrás llamar a `find_package()`): `ROBOTICSLAB_YARP_DEVICES`, `ROBOTICSLAB_KINEMATICS_DYNAMICS_INCLUDE_DIRS`, `roboticslab-vision`.

## Programación C/C++
* Para crear un nuevo proyecto C/C++, utiliza [project-generator](https://github.com/roboticslab-uc3m/project-generator).
* Si hay problema con project-generator, [coméntalo en su sección de issues](https://github.com/roboticslab-uc3m/project-generator/issues). Si sigues con motivos en contra, por lo menos no dejes de utilizar [CMake](http://asrob.uc3m.es/index.php/Tutorial_CMake) para cualquier proyecto C/C++.
* Utiliza _UpperCamelCase_ para nombres de librerías y de clases.
* Utiliza _lowerCamelCase_ para nombres de ejecutables.
* Evita el uso de variables globales.
* Preferimos el uso de la clase `std::string` frente a alternativas como `char*` o `yarp::os::ConstString`.
* Crea tus clases dentro de un _namespace_. Nuestra tendencia actual es `roboticslab::` (see https://github.com/roboticslab-uc3m/QA/issues/15).
* Mantén un `main()` minimalista: implementa tu programa como una clase.
  * En C++ solemos hacer que la clase principal herede de [yarp::os::RFModule](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html), con lo cual se dispone de un [configure\(yarp::os::ResourceFinder& rf\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a6c3880961b00b0a7eb527d62214169b7) que recibe un diccionario \([rf](http://www.yarp.it/classyarp_1_1os_1_1ResourceFinder.html)\) pasado desde el `main()`, un [close\(\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a58ce26fc6fdcb6eb4af8e8dc678e095e) que se llama con la señal _CRTL+C_, y una función [updateModule\(\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a37ee5baa17ce243458a1dff209e878b7) llamada periódicamente, con una periodicidad lenta \[segundos\] dada por [getPeriod\(\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#ace2fdadde1a2690f274079fabd6420d2). Si se necesita una función que se llame rápidamente, heredando de [yarp::os::RateThread](http://www.yarp.it/classyarp_1_1os_1_1RateThread.html) se obtiene una función [run\(\)](http://www.yarp.it/classyarp_1_1os_1_1RateThread.html#ac3c97e766733b41a45c799aa0c05598f) que es llamada con una periodicidad  en unidades de milisegundos especificada en el constructor.
* Si tienes un dispositivo, también impleméntalo como una clase, idealmente como un [_YARP device_](http://asrob.uc3m.es/index.php/Tutorial_yarp_devices).
* Crea un test para cada clase, desarrollándolo a la par de la clase. En la actualidad utilizamos **gtest**, como en [kinematics-dynamics/test/testKdlSolver](https://github.com/roboticslab-uc3m/kinematics-dynamics/tree/develop/test/testKdlSolver.cpp) y [yarp-devices/tests/testTechnosoftIpos](https://github.com/roboticslab-uc3m/yarp-devices/tree/develop/tests/testTechnosoftIpos/testTechnosoftIpos.cpp), que está integrado con Travis CI.
* Se recomienda marcar una función como DEPRECATED durante un mes antes de eliminarse de una API. Macros DEPRECATED se pueden generar vía CMake como [aquí](https://github.com/roboticslab-uc3m/kinematics-dynamics/blob/21f2dde2a38f1d0c1c93703d3619e34c14c3bfcd/CMakeLists.txt#L110-L118), y utilizarse en el código como [aquí](https://github.com/roboticslab-uc3m/kinematics-dynamics/blob/21f2dde2a38f1d0c1c93703d3619e34c14c3bfcd/libraries/TeoYarp/ICartesianSolver.h#L29-L33). El procedimiento completo, tal como se describe en [QA #21](https://github.com/roboticslab-uc3m/QA/issues/21), debe ser:
  1. Abre una `issue` allá donde se encuentre la función obsoleta.
  1. Etiquétala (*label*) como `announcement`.
  1. Utiliza la barra de búsqueda para localizar las llamadas a dicha función en roboticslab-uc3m y enumera todos los repositorios afectados.
  1. Si es necesario, traza un plan de acción adecuado y detalla los pasos necesarios para realizar una transición suave hacia la nueva API.
  1. Menciona al *team* correspondiente o a quien pueda necesitar asistencia durante la operación anterior.
  1. Procede gradualmente y, finalmente, elimina la función.

