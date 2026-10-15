import smtplib
import time

from email.message import EmailMessage


# ==========================================
# CONFIGURACIÓN
# ==========================================

CANTIDAD_CORREOS = int(
    input("¿Cuántos correos deseas enviar?: ")
)

EMAIL_REMITENTE = input(
    "Email remitente: "
)

EMAIL_PASSWORD = input(
    "Contraseña de aplicación: "
)

EMAIL_DESTINO = input(
    "Email de destino: "
)

while True:
    TIPO_CORREO = input(
        "Tipo de correo (texto/imagen): "
    ).strip().lower()

    if TIPO_CORREO in ("texto", "imagen"):
        break

    print("Opción no válida. Escribe 'texto' o 'imagen'.")


# ==========================================
# ARCHIVOS
# ==========================================

IMAGEN = "image.jfif"


# ==========================================
# CREAR CORREO
# ==========================================

def crear_correo(tipo, numero):

    mensaje = EmailMessage()

    mensaje["From"] = EMAIL_REMITENTE
    mensaje["To"] = EMAIL_DESTINO

    mensaje["Subject"] = (
        f"PRUEBA APP #{numero} - {tipo}"
    )

    # -----------------------------
    # SOLO TEXTO
    # -----------------------------

    if tipo == "texto":

        mensaje.set_content(
            f"""
Este es el correo de prueba número {numero}.

Tipo: SOLO TEXTO

Este correo sirve para comprobar que la aplicación
puede recibir y procesar correctamente mensajes de texto.
"""
        )

    # -----------------------------
    # TEXTO + IMAGEN
    # -----------------------------

    elif tipo == "imagen":

        mensaje.set_content(
            f"""
Este es el correo de prueba número {numero}.

Tipo: TEXTO + IMAGEN

Este correo contiene texto y una imagen.
"""
        )

        with open(IMAGEN, "rb") as archivo:

            datos = archivo.read()

            mensaje.add_attachment(
                datos,
                maintype="image",
                subtype="jpeg",
                filename="imagen_prueba.jpg"
            )

    return mensaje


# ==========================================
# ENVIAR CORREOS
# ==========================================

def enviar_correos():

    print()
    print("Conectando al servidor de Gmail...")

    servidor = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    servidor.starttls()

    servidor.login(
        EMAIL_REMITENTE,
        EMAIL_PASSWORD
    )

    print("Conectado correctamente.")
    print()

    # ======================================
    # ENVÍO
    # ======================================

    for numero in range(
        1,
        CANTIDAD_CORREOS + 1
    ):

        try:

            mensaje = crear_correo(
                TIPO_CORREO,
                numero
            )

            servidor.send_message(
                mensaje
            )

            print(
                f"[OK] Correo "
                f"{numero}/{CANTIDAD_CORREOS} "
                f"→ {TIPO_CORREO}"
            )

        except Exception as error:

            print(
                f"[ERROR] Correo "
                f"{numero}: {error}"
            )

        time.sleep(1)

    servidor.quit()

    print()
    print("================================")
    print("PRUEBA TERMINADA")
    print("================================")


# ==========================================
# INICIO
# ==========================================

if __name__ == "__main__":

    enviar_correos()