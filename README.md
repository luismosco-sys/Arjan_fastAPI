# Arjan_fastAPI
Demo repo for some FastAPI exercises
## Requirements
  - Python 3.13
  - See requirements.txt
## TODO list
  - [ ] Estructurar bien el proyecto. Esto es tener minimamente los endpoints en un lugar (main.py) los modelos de pydantic (como Item) en otro, y los enums (como Category) en otro:
    - main.py (aqui los endpoints), schemas.py (aqui los de pydantic), api_enums.py (aqui los enums)
  - [ ] Para los endpoints de *query_item_by_parameters* y *update* cambiar los parametros por un modelo de pydantic. 
  - [ ] Para todos los endpoints, aplicar response models (solo de respuesta positiva), esto se agrega en el decorador.
  - [ ] Una vez terminado todo lo anterior, implementar el uso de una base de datos SQLite para almacenar el inventario, utilizando SQLAlchemy

