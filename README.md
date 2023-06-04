# ArquitecturaDeComputadores_Raspberry

La idea de nuestro proyecto es utilizar una Raspberry para poder realizar el control de una huerta  (también podría servir para la playa). Mediante la Raspberry, el usuario puede ver en una página web la imagen en directo de la huerta, ver información de los sensores de temperatura, humedad y humedad en la tierra y ver información del tiempo. Para ello, hemos conectado a la Raspberry diferentes sensores de entrada y salida. 

Por un lado, en los dispositivos de entrada tenemos la cámara,que hemos conectado mediante el puerto USB, para  poder ver la imagen en directo de la huerta. También, hemos conectado dos sensores el DHT11 para obtener información sobre la temperatura y humedad en el aire y un sensor que muestra la humedad con contacto que se podría introducir en la tierra. 

Por otro lado, tenemos dos actuadores LED como salida. Uno de ellos se enciende al poner en marcha la página web y el otro se enciende cuando el usuario está en la pestaña de la cámara. 

La obtención de la información del tiempo lo hemos realizado mediante web scraping de la página web de Euskalmet.  Además, hemos realizado una API para obtener la información de los sensores. 

Por último, para introducir en el proyecto el procesamiento en paralelo mediante hilos hemos pensado añadir hilos a la hora de obtener información mediante los sensores. A continuación, en el siguiente punto se explica con exactitud cómo hemos realizado cada funcionalidad.  


Julen Díez y Asier Olaizola
