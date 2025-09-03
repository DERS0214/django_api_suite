
# 🚀 Django API Suite

## 📌 Resumen del Proyecto
**Django API Suite** es un conjunto de APIs desarrolladas con **Django** que ofrece servicios completos para la **gestión de datos** e integración con plataformas en la nube.  
Incluye APIs de demostración, funcionalidades reales de producción y un portal administrativo centralizado.

---

## 🔥 Características Principales

### 🏠 Portal Web Administrativo
- Página de inicio elegante como punto de acceso a todas las APIs.  
- Interfaz moderna construida con **Tailwind CSS**.

### 🔧 Demo REST API
- API de prueba con **CRUD completo** (Create, Read, Update, Delete).  
- Almacenamiento en memoria para pruebas rápidas.  
- Gestión de usuarios con nombre, email y estado activo.  
- **Eliminación lógica** y soporte para operaciones `PUT` y `PATCH`.

### 🌐 Landing API con Firebase
- API para gestión de reseñas con **Firebase Realtime Database**.  
- Almacenamiento en la nube con timestamps personalizados.  
- Operaciones `GET` y `POST` optimizadas.

---

## 🛠️ Tecnologías Utilizadas
- **Framework principal:** Django 5.2.4  
- **API Framework:** Django REST Framework 3.16.0  
- **Base de datos en la nube:** Firebase Admin SDK 7.0.0  
- **Base de datos local:** SQLite3  
- **Frontend:** Tailwind CSS  

---

## 📂 Estructura del Proyecto
```

django\_api\_suite/
├── backend\_data\_server/     # Configuración principal de Django
├── demo\_rest\_api/           # API de demostración con CRUD
├── landing\_api/             # API con Firebase
├── homepage/                # Portal web administrativo
├── templates/               # Plantillas HTML
└── requirements.txt         # Dependencias del proyecto
```


---

## 🌍 Despliegue
Este proyecto está configurado para su despliegue en **PythonAnywhere**:  
🔗 `https://katesfv.pythonanywhere.com`

---

## 🔗 Rutas de API

### Demo REST API
| Método      | Endpoint                              | Descripción                               |
|-------------|--------------------------------------|-------------------------------------------|
| `GET/POST`  | `/demo/rest/api/index/`               | Gestión de recursos                       |
| `PUT/PATCH/DELETE` | `/demo/rest/api/<item_id>/`    | Operaciones sobre elementos específicos   |

### Landing API
| Método      | Endpoint                              | Descripción                               |
|-------------|--------------------------------------|-------------------------------------------|
| `GET/POST`  | `/landing/api/index/`                | Gestión de reseñas en Firebase            |

### Portal Web
| Ruta        | Descripción                           |
|-------------|--------------------------------------|
| `/`         | Página principal del portal admin     |

---

## ☁️ Integración con Firebase
Se utiliza **Firebase Realtime Database** para almacenamiento persistente, con configuración para el proyecto `casa-food`.

---

## 💡 Notas
Django API Suite combina:
- **Demo REST API:** ideal para aprendizaje y pruebas de operaciones CRUD.  
- **Landing API:** integración real con servicios en la nube.  
- **Portal Web:** interfaz unificada para gestionar los servicios.  

