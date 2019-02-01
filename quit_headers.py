import email
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO, BytesIO

def remove_email_headers(data, nombre_archivo_generado="file_withoutheaders.out"):
    # data es lo que resulta de leer el archivo 
    # recibe data , lo transforma a string
    # y busca quitar lo que este arriba de MIME-Version: 1.0
    # si lo parte, genera un archivo con nombre nombre_archivo_generado

    msg = email.message_from_string(data)
    patron = "MIME-Version:"
    partido = False

    if msg.is_multipart():# ya es multipart, osea ya no tiene las cabeceras
        msg = data
    else: ## es un texto en bruto
        texto_total = msg.get_payload()
        lista_partida = texto_total.split(patron, 1)#el split lo debe hacer maximo una vez
        if (len(lista_partida)) > 1:
            lo_buscado = lista_partida[1]
            msg = patron + lo_buscado
            partido = True

    with open(nombre_archivo_generado,'w') as text_file:
        text_file.write(msg)

    return partido, nombre_archivo_generado



if __name__ == "__main__":

    with open('script.out', 'r') as myfile:
        data=myfile.read()

    partido, nombre_file  = remove_email_headers(data)

    print("--------------------------------------------")
    if partido:
        print("tuto benne ...........")
        print(nombre_file)
    else:
        print("ya es multipart.... no hay que quitar cabeceras")

    #print(msg)
