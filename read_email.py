from quit_headers import remove_email_headers
import email
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO, BytesIO

class Attachement(object):
    def __init__(self):
        self.data = None;
        self.content_type = None;
        self.size = None;
        self.name = None;

    def create_file(self):
        attachment = BytesIO(self.data)
        attachment.content_type = self.content_type
        attachment.size = self.size
        attachment.name = "archivo.pdf"
        return attachment

def email_chunks(data): #receive email as a string starting with MIME-Version: 1.0
    """
    before using email_chunks, its necessary to use remove_email_headers
    remove_email_headers remove unnecessary text before MIME-Version: 1.0
    """

    msg = email.message_from_string(data)
    from_email = msg['from']
    to_email = msg['to']
    attach = Attachement()

    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))
            if ctype == 'application/pdf' and 'attachment' in cdispo:
                attach.data = part.get_payload(decode=True);
                attach.content_type = part.get_content_type();
                attach.size = len(attach.data);
                attach.name = part.get_filename();
          
    else:
        print("NOT MULTIPART ................................................................")
        print(msg.get_payload(decode=True))

    return from_email, to_email,  msg, attach



if __name__ == "__main__":

    ## name or product file
    final_name = "final.pdf"

    # open original email text message 
    with open('email_all.txt', 'r') as myfile:
        data=myfile.read()

    partido, nombre_archivo  = remove_email_headers(data, 'email_all.out')

    with open(nombre_archivo, 'r') as myfile:
        data=myfile.read()

    f, t, msg, archivo = email_chunks(data)
    archivo_resultado = archivo.create_file()  

    with open(final_name,'wb') as out: ## Open temporary file as bytes
        out.write(archivo_resultado.read())


