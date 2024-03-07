Crear un entorno virtual con virtualenv, activarlo y desactivarlo:

```
python -m virtualenv venv

.\venv\Scripts\activate

.\venv\Scripts\deactivate

```

Instalar los requerimientos del sistema:

```
pip install -r ".\requirements.txt"

```

Inicializar el proyecto:

```
reflex init

```

Inicializar la base de datos:

```
reflex db init
reflex db migrate
```

Correr el proyecto:

```
reflex run

```
