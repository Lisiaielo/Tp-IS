import openai
import readline  # Importamos el módulo readline
import sys

def main():
    try:
        # Configura la clave de la API de OpenAI
        openai.api_key = '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'

        convers_mode = False  # Variable para indicar si estamos en modo conversación
        buffer = []  # Buffer para almacenar las consultas y respuestas

        if "--convers" in sys.argv:
            convers_mode = True

        last_query = ""  # Variable para almacenar la última consulta

        while True:
            try:
                # Solicitar consulta al usuario
                query = input("Ingrese su consulta: ")

                # Si estamos en modo conversación y la consulta no es nula
                if convers_mode and query.strip():
                    buffer.append(query)
                else:
                    last_query = query

            except KeyboardInterrupt:
                print("\nHasta luego.")
                break

            try:
                # Generar respuesta usando OpenAI
                if convers_mode:
                    response = openai.Completion.create(
                        engine="text-davinci",
                        prompt='\n'.join(buffer),  # Utilizamos todas las consultas en el buffer como prompt
                        max_tokens=50
                    )
                    response_text = response.choices[0].text.strip()
                    print("Respuesta:", response_text)

                    # Agregar la respuesta al buffer
                    buffer.append(response_text)
                else:
                    response = openai.Completion.create(
                        engine="text-davinci",
                        prompt=last_query,
                        max_tokens=50
                    )
                    print("Respuesta:", response.choices[0].text.strip())
            except openai.error.InvalidRequestError as e:
                print("Error de solicitud:", e)
            except openai.error.APIConnectionError as e:
                print("Error de conexión a la API:", e)
            except Exception as e:
                print("Error general:", e)

    except Exception as e:
        print("Error general:", e)

if __name__ == "__main__":
    main()
# El programa Pylint tira los siguientes datos.
# Your code has been rated at 2.37/10

# Sugerencias de chatgpt
# He revisado el código y he realizado las siguientes correcciones y mejoras:
# 1)Agregué comentarios explicativos: Comenté el código para explicar cada sección y los cambios realizados.
# 2)Agregué manejo de excepciones Try/Except: Se han agregado bloques Try/Except para manejar posibles errores durante la ejecución del programa.
# 3)Agregué la funcionalidad para conversaciones: Se ha agregado la opción --convers como argumento de línea de comandos para activar el modo de conversación. En este modo, el programa almacenará consultas anteriores y respuestas en un buffer.
# 4)Recuperación de la última consulta con la tecla "cursor Up": Lamentablemente, no es posible implementar la funcionalidad de recuperar la última consulta con la tecla "cursor Up" en este entorno de ejecución de código en línea. 
