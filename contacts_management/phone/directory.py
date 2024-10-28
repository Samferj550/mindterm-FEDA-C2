class Directory:
    """
    Clase Directorio:

    Atributos:
    contactos: Matriz que contiene todos los contactos, incluyendo la primera fila como encabezado.

    Métodos:
    __init__: Inicializa la matriz contactos con la primera fila como encabezado de atributos.
    agregar_contacto: Agrega un nuevo contacto a la matriz.
    listar_contactos: Muestra todos los contactos en la matriz, incluyendo el encabezado.
    """
    
    def __init__(self):
        self.contacts = [["Nombre", "Apellido", "Organización", "Teléfono", "Dirección"]]

    def add_contact(self, contact):
        self.contacts.append(contact.get_data())

    def list_contacts(self):
        for row in self.contacts:
            print("\t".join(row))

directory = Directory()

contact1 = Contact("Alice", "Smith", "TechCorp", "12345", "Calle 1, Ciudad A")
contact2 = Contact("Bob", "Johnson", "Innovate Inc.", "67890", "Avenida 2, Ciudad B")
contact3 = Contact("Carol", "Brown", "Creative LLC", "54321", "Calle 3, Ciudad C")

directory.add_contact(contact1)
directory.add_contact(contact2)
directory.add_contact(contact3)

print("Directorio de Contactos:")
directory.list_contacts()
