<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/elopezqu/Lab2_Team3K/blob/main/epis.png" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/elopezqu/Lab2_Team3K/blob/main/abet.png" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>
<div align="center">
 <h3>INFORME DE LABORATORIO</h3>
</div>
<table>
 <theader>
  <tr><th colspan="6" bgcolor="red">INFORMACIÓN BÁSICA</th></tr>
 </theader>
 <tbody>
  <tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
  <tr><td>TÍTULO DE LA PRACTICA:</td><td colspan="5">Python</td></tr>
  <tr><td>NÚMERO DE PRÁCTICA:</td><td>Practica de Laboratorio 04</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td></tr>
  <tr><td>FECHA DE PRESENTACIÓN:</td><td>29/05/2022</td><td>HORA DE PRESENTACIÓN:</td><td colspan="3">11:30 p.m.</td></tr>
  <tr><td>INTEGRANTES:</td><td colspan="3">- Edson Joel López Quispe<br>- Gabriel Steven Machicao Quispe<br>- Fernando Coyla Alvarez</td><td>NOTA:</td><td>...</td></tr>
  <tr><td>DOCENTE:</td><td colspan="5">Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</td></tr>
 </tbody>
</table>
<table>
 <theader>
  <tr><th>SOLUCIÓN Y RESULTADOS</th></tr>
 </theader>
 <tbody>
  <tr><td>I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS:<br>
  # 
      -Funcion verticalMirror, devuelve el espejo vertical de la imagen<br>
      ```sh
        def verticalMirror(self):   
            lista = self.img 
            cadena = ""
            listaV = []
            for i in lista:
                for letra in i:
                    cadena = letra + cadena
            listaV.append(cadena)
            cadena = ""  
            return Picture(listaV)	    	
  ```
  <br>- Para el método Under se utilizaron dos bucles que recorren todo la figura actual tanto en fila como en columnas, luego evalua buscando un espacio vacio y remplazandolo por la nueva figura caracter por caracter. Finalmente retorna la lista modificada<br>
  <pre>
   def under(self, p):
      lista = self.img
      lista2 = p.img
      for x in range(len(lista2)):
        for y in range(len(lista2[x])):
          if lista2[x][y:y+1] != " ":
            linea = list(lista[x])
            linea[y] = lista2[x][y:y+1]
            lista[x] = "".join(linea)
      return Picture(lista)
  </pre>
  - Métodos horizontalRepeat y verticalRepeat en la primera se añadio a cada elemento de la lista(string) la misma cadena las veces que indicaba n, esto se guarda en otro arreglo y se retorna.
  <pre>
   def horizontalRepeat(self, n):
     lista = self.img
     lista2 = []
     cadena = ""
     for i in range(len(lista)):
         for x in range(n+1):
             cadena = cadena+lista[i]
         lista2.append(cadena)
         cadena = ""
     return Picture(lista2)
  </pre> 
  Para el segundo, se añade nuevos elementos(String) al final de la lista
  <pre>
  def verticalRepeat(self, n):
    lista = self.img
    lista2 = []
    for x in range(n+1):
        lista2 = lista2+lista
    return Picture(lista2)
  </pre>
  </td></tr>
  
  <tr><td>II. SOLUCIÓN DEL CUESTIONARIO:<br><strong><em>1. ¿Qué son los archivos *.pyc?</em></strong><br><p>Sirve para almacenar los archivos con extensión .pyc o .pyo; que optimiza la carga de los módulos y permite la ejecución de los programas de forma rápida. Se recomienda no comprometer el control de la fuente y debe coexistir en paz con su código fuente local.</p><strong><em>2. ¿Para qué sirve el directorio pycache?</em></strong><p>Son archivos ejecutables que contiene lineas de código compilados escritos en Python. Esto significa que después de la primera ejecución, el programa Python utilizará el archivo compilado .pyc al importar.</p><strong><em> 3. ¿Cuáles son los usos y lo que representa el subguión en Python?</em></strong><p>Los usos que le dan al caracter "_" , son : la marcación de las cadenas traducibles para la internacionalización (i18n) o localización (l10n); otro uso que se le da es para almacenar el ultimo valor declarado, además de separar los dígitos de un números. Támbien se usa para ignorar valores específicos, pero lo más usado es para nombrar variables o funciones. Lo que representa este caracter en la programación con Python es variada, depende del contexto donde se empleé.</p></td></tr>
  <tr><td>III. CONCLUSIONES:<br>Los ejercicios consistian en completar los métodos de la la clase <em>picture</em> y con ello realizar los ejercicios del a-g, esto implicó indagar acerca del lenguaje python y junto con los conocimientos de la programación orientada a objetos se pudo realizar los ejercicios propuestos, para la implementación de los métodos se usaron bucles, condicionales y metodos de String, en cambio para la realización de los ejercicos se utilizaron objetos junto con los metodos previamente creados.</td></tr>
 </tbody>
</table>

<table>
 <theader>
  <tr><td>RETROALIMENTACIÓN GENERAL</td><tr>
 </theader>
 <tbody>
  <tr><td>Python es un lenguaje orientado a objectos muy usado por la comudad por ser un lenguaje de alto nivel de facil y de fácil legibilidad, esto ultimo nos ayudo bastante ya que al no estar familiarizados con el lenguaje pudimos completar fatisfactoriamente la plactica 4. En los ejercicios presentados, no se tuvo problemas, más que errores comunes de escritura y uno que otro error de lógica. Cabe mencionar que construir el método <em>under</em> representó un reto para el equipo pero al final se pudo culminar.</td></tr>
 </tbody>
</table>

<table>
 <theader>
  <tr><td>REFERENCIAS Y BIBLIOGRAFÍA</td><tr>
 </theader>
 <tbody>
  <tr><td>[1] "The Python Tutorial — Python 3.10.4 documentation". 3.10.4 Documentation. https://docs.python.org/3/tutorial/ (accedido el 28 de mayo de 2022).<br>
     [2] "Python reference". W3Schools Online Web Tutorials. https://www.w3schools.com/python/python_reference.asp (accedido el 28 de mayo de 2022).<br></tr>
 </tbody>
</table>