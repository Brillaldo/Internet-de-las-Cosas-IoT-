import network  # Librería para manejar la conexión Wi-Fi
import urequests  # Librería para realizar solicitudes HTTP
import utime  # Librería para manejar el tiempo y pausas en la ejecución
import machine  # Librería para controlar hardware del microcontrolador

# Configuración Wi-Fi
SSID = "CARMONA"  # Nombre de la red Wi-Fi a la que se conectará
PASSWORD = "AbabL2019"  # Contraseña de la red Wi-Fi

# Configuración de ThingSpeak
API_KEY = "92EGPAWN2LQRDQVZ"  # Clave API de ThingSpeak para enviar datos
THINGSPEAK_URL = "https://api.thingspeak.com/update"  # URL de la API de ThingSpeak

# Función para conectarse a la red Wi-Fi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)  # Se crea un objeto WLAN en modo estación (STA)
    wlan.active(True)  # Se activa la interfaz Wi-Fi
    wlan.connect(SSID, PASSWORD)  # Se intenta conectar a la red con las credenciales
    
    print("Conectando a Wi-Fi...")
    while not wlan.isconnected():  # Se espera hasta que la conexión se establezca
        utime.sleep(1)  # Espera de 1 segundo antes de volver a comprobar
    
    print("Conectado a Wi-Fi:", wlan.ifconfig())  # Se imprime la configuración de la conexión

# Función para leer la temperatura interna del RP2040
def leer_temperatura():
    sensor_temp = machine.ADC(4)  # Se inicializa el ADC en el canal 4 (sensor interno de temperatura)
    conversion_factor = 3.3 / 65535  # Factor de conversión para obtener el voltaje real
    lectura = sensor_temp.read_u16() * conversion_factor  # Se obtiene la lectura en voltios
    temperatura = 27 - (lectura - 0.706) / 0.001721  # Conversión a temperatura en grados Celsius según la fórmula del RP2040
    return round(temperatura, 2)  # Se redondea la temperatura a 2 decimales y se retorna

# Función para enviar los datos de temperatura a ThingSpeak
def enviar_a_thingspeak(temp):
    try:
        # Se envía una solicitud GET a ThingSpeak con la clave API y el valor de temperatura
        respuesta = urequests.get(THINGSPEAK_URL + "?api_key=" + API_KEY + "&field1=" + str(temp))
        print("Enviado a ThingSpeak:", respuesta.text)  # Se imprime la respuesta del servidor
        respuesta.close()  # Se cierra la conexión
    except Exception as e:
        print("Error enviando datos:", e)  # Se captura e imprime cualquier error que ocurra

# Conectar a Wi-Fi antes de empezar a enviar datos
conectar_wifi()

# Bucle principal que lee la temperatura y la envía a ThingSpeak
while True:
    temperatura = leer_temperatura()  # Se lee la temperatura del sensor
    print("Temperatura actual:", temperatura, "°C")  # Se imprime la temperatura en la consola
    enviar_a_thingspeak(temperatura)  # Se envía la temperatura a ThingSpeak
    utime.sleep(180)  # Se espera 180 segundos (3 minutos) antes de repetir el proceso
