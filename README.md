# Motores-de-b-squeda
Para ejecutar este solver es necesario clonar el repositorio, se sugiere aun cuando no es obligación utilizar un entorno virtual de python.
```
    cmd
    git clone https://github.com/gtello79/Motores-de-b-squeda.git
    cd Motores-de-b-squeda
    python main.py
```
De esta forma, el algoritmo lanzará un mensaje por consola pidiendo ingresar una frase para predecir, por ejemplo 'Hello Hello'
```
  CADENA A PREDECIR
  Hello hello
```
Como consecuencia de esto, el algoritmo entregará la predicción de este cadena, a la misma vez que aprende de ella, en efecto:
```
  CADENA A PREDECIR
  Hello hello
  HELP HELLO
```
Donde HELP es la prediccion para el primer 'Hello' y a consecuencia de esto, aprendió de ella y cuando se le pregunta nuevamente por esta palabra, retorna la prediccion en si.
