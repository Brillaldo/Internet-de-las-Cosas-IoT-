# Internet-de-las-Cosas-IoT-

# Monitor de Temperatura con RP2040 y ThingSpeak

Este proyecto permite leer la temperatura interna de un microcontrolador RP2040 y enviarla automáticamente a la plataforma ThingSpeak para su monitoreo en la nube.

## Requisitos

✅ Raspberry Pi Pico W
✅ Sensor de temperatura LM35
✅ ThingSpeak (almacenamiento y visualización de datos)
✅ MathWorks (análisis y procesamiento de datos en ThingSpeak)

## Instalación

### 1. Instalar MicroPython en el RP2040

Si aún no tienes MicroPython instalado, sigue estos pasos:

1. Descarga el firmware de MicroPython desde [aquí](https://micropython.org/download/rp2-pico/).
2. Conecta el RP2040 en modo bootloader (mantén presionado el botón BOOTSEL y conéctalo por USB).
3. Copia el archivo `.uf2` descargado en la unidad que aparece.

### 2. Instalar Thonny

Thonny es un IDE fácil de usar para programar en MicroPython:

1. Descarga e instala Thonny desde [thonny.org](https://thonny.org/).
2. Selecciona el intérprete de MicroPython para el RP2040 en `Herramientas > Opciones > Intérprete`.
3. Conéctate al RP2040 y prueba con un simple `print("Hola, MicroPython!")`.

### 3. Subir el código al RP2040

1. Copia el código en un archivo `main.py`.
2. Modifica las siguientes variables en el código con tus credenciales Wi-Fi y API de ThingSpeak:
   ```python
   SSID = "TU_SSID"
   PASSWORD = "TU_CONTRASEÑA"
   API_KEY = "TU_CLAVE_API_THINGSPEAK"
   ```
3. Guarda y ejecuta el archivo en el RP2040.

## Uso

1. Al iniciar, el RP2040 se conectará a la red Wi-Fi y mostrará su dirección IP.
2. Leerá la temperatura interna del microcontrolador.
3. Enviará la temperatura a ThingSpeak cada 3 minutos.
4. Puedes visualizar los datos en ThingSpeak accediendo a tu canal.




