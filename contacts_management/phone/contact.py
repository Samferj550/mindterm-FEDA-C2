class Contact:
      """
    Atributos:
    datos: Lista que contiene los valores de los atributos del contacto (nombre, apellido, organización, teléfono, dirección).
    
    Métodos:
    __init__: Inicializa el contacto con los atributos necesarios y los almacena en una lista.
    obtener_datos: Retorna la lista con los datos del contacto.

    """
    
    def __init__(self, first_name, last_name, organization, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.organization = organization
        self.phone = phone
        self.address = address

    def get_data(self):
        return [self.first_name, self.last_name, self.organization, self.phone, self.address]
