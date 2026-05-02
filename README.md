<div align="center">

# 🎧 Joa DJ Hand Control 

### Controlador de música por gestos usando Python, cámara y visión artificial.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-FF6F00?style=for-the-badge)
![Pygame](https://img.shields.io/badge/Pygame-Audio-00A86B?style=for-the-badge)

</div>

---

**DJ Hand Control** es una aplicación en Python que permite controlar música local usando gestos de las manos detectados en tiempo real con la cámara.

El proyecto utiliza visión artificial para reconocer la mano, dibujar sus puntos de seguimiento y ejecutar acciones como reproducir, pausar o cambiar de canción.

---

## Gestos disponibles

| Gesto | Acción |
|---|---|
| Mano abierta | Reproducir música |
| Puño cerrado | Pausar música |
| Dos dedos | Cambiar canción |
| `Q` | Cerrar el programa |

---

## Tecnologías utilizadas

- Python 3.12
- OpenCV
- MediaPipe
- Pygame
- NumPy

---

## Instalación

Clonar el repositorio:

`git clone https://github.com/joagonzalez26/joa-dj-hand-control.git`

Entrar a la carpeta:

`cd joa-dj-hand-control`

Crear entorno virtual:

`python3.12 -m venv .venv`

Activar entorno virtual:

`source .venv/bin/activate`

Instalar dependencias:

`pip install -r requirements.txt`

---

## Uso

Agregá tus canciones dentro de la carpeta `music/`.

Formatos admitidos:

- `.mp3` 🎵
- `.wav` 🎵
- `.ogg` 🎵

Luego ejecutás:

`python main.py`

---

## Importante

Las canciones no están incluidas en el repositorio.  
Cada usuario debe agregar sus propios archivos de música dentro de la carpeta `music/`.

---

## Estado actual

- Cámara funcionando.
- Detección de manos en tiempo real.
- Líneas y puntos de seguimiento sobre la mano.
- Control básico de música por gestos.
- Soporte visual para detectar hasta dos manos.

---

## Próximas mejoras

- Control de volumen con la mano.
- Mejor detección de gestos.
- Funciones distintas para cada mano.
- Interfaz visual más personalizada.
- Documentación técnica del código.

---

## Autor

Desarrollado por **Joaquín González** como proyecto personal de aprendizaje y portfolio.

GitHub: [joagonzalez26](https://github.com/joagonzalez26)

---

<div align="center">

<img width="1080" height="1350" alt="Blue and White Minimal Modern Simple Typography Art Workshop Instagram Story (Post para Instagram (45))" src="https://github.com/user-attachments/assets/0581e4eb-c510-4744-b459-f0d8520f120e" />

</div>
