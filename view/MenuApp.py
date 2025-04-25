from application.EmployeeInput import EmployeeInput
from application.ServiceInput import ServiceInput
from domain.model.Guest import Guest
from application.GuestService import GuestService
from application.Guestinput import GuestInput
from application.ReservationInput import ReservationInput
from application.RoomInput import RoomInput
from repository.connection.MysqlDataHandler import Conexion
from domain.model.Room import Room
from repository.persistence.EmployeeRepository import EmployeeRepository
from repository.persistence.RoomRepository import RoomRepository
from domain.model.Employee import Employee
from domain.model.Services import Services
from repository.persistence.ServiceRepository import ServiceRepository


class MenuApp:
    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel')
        self.db.connection()
        self.guest = Guest(None, None, None, None, None, None, None, None, None)
        self.guest_service = GuestService()
        self.guest_input = GuestInput()
        self.room_input = RoomInput()
        self.room = Room(None, None)
        self.room_repository = RoomRepository
        self.employee = Employee(None, None, None, None, None, None, None)
        self.employee_input = EmployeeInput()
        self.employee_repository = EmployeeRepository
        self.service = Services(None, None, None)
        self.service_input = ServiceInput()
        self.service_repository = ServiceRepository


    def display_header(self, title):
        print("\n" + "=" * 40)
        print(f"{title:^40}")
        print("=" * 40)

    def init_app(self):
        print("\n¡Bienvenido al Sistema de Gestión de Hotel!")
        init = int(input("\nPresione 1 para inicializar, 0 para salir: "))

        while init != 0:
            self.display_header("MENÚ PRINCIPAL")
            print(" 1. Login")
            print(" 2. Registro de Huésped")
            print(" 3. Gestión de Reservas")
            print(" 4. Gestión de Habitaciones")
            print(" 5. Gestión de Empleados")
            print(" 6. Gestión de Servicios")
            print(" 0. Salir")

            option = input("\nSeleccione una opción: ")

            try:
                option = int(option)

                if option == 0:
                    print("\n¡Gracias por usar el sistema! Hasta pronto.")
                    init = 0
                elif option == 1:
                    self.login_menu()
                elif option == 2:
                    self.display_header("REGISTRO DE HUÉSPED")
                    self.guest_input.register(self.guest, self.db)
                elif option == 3:
                    self.reservation_menu()
                elif option == 4:
                    self.room_menu()
                elif option == 5:
                    self.employee_menu()
                elif option == 6:
                    self.service_menu()
                else:
                    print("\n⚠️ Opción no válida. Intente nuevamente.")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.")

    def login_menu(self):
        self.display_header("LOGIN")
        print("Funcionalidad de login en desarrollo...")
        input("\nPresione Enter para continuar...")

    def reservation_menu(self):

        while True:
            self.display_header("GESTIÓN DE RESERVAS")
            print(" 1. Consultar reserva")
            print(" 2. Realizar nueva reserva")
            print(" 0. Volver al menú principal")

            option = input("\nSeleccione una opción: ")

            try:
                option = int(option)

                if option == 0:
                    break
                elif option == 1:
                    print("\n✅ Has consultado exitosamente")
                    input("\nPresione Enter para continuar...")
                elif option == 2:
                    print("\nIniciando proceso de reserva...")
                    self.room_menu()
                else:
                    print("\n⚠️ Opción no válida. Intente nuevamente.")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.")

    def room_menu(self):
        while True:
            self.display_header("GESTIÓN DE HABITACIONES")
            print(" 1. Listar todas las habitaciones")
            print(" 2. Buscar habitación por número")
            print(" 3. Registrar nueva habitación")
            print(" 4. Mostrar habitaciones disponibles")
            print(" 5. Actualizar disponibilidad")
            print(" 6. Eliminar habitación")
            print(" 0. Volver al menú principal")

            option = input("\nSeleccione una opción: ")

            try:
                option = int(option)

                if option == 0:
                    break
                elif option == 1:
                    print("\nListando habitaciones...")
                    rooms = self.room_input.room_repository.find_all(self.db)
                    print(rooms)
                    input("\nPresione Enter para continuar...")
                elif option == 2:
                    number = input("Ingrese el número de habitación")
                    room_id = self.room_input.room_repository.find_by_room_numer(number, self.db)
                    print(room_id)
                    print("\n✅ Encontraste la habitación")
                    input("\nPresione Enter para continuar...")
                elif option == 3:
                    self.room_input.register(self.room, self.db)
                    input("\nPresione Enter para continuar...")
                elif option == 4:
                    print("\nListando habitaciones disponibles...")
                    reponse = self.room_input.room_repository.find_available(self.room, self.db)
                    print(reponse)
                    input("\nPresione Enter para continuar...")
                elif option == 5:
                    print("\nActualizar disponibilidad de habitación...")
                    number = input("\nIngrese el número de habitación...")
                    room = input("\nIngrese el estado de la habitación...")
                    updated = self.room_input.room_repository.update_availability(number, room, self.db)
                    print(updated)
                elif option == 6:
                    print("\nFuncionalidad de eliminación en desarrollo...")
                    number = input("\nPresione número de habitación a eliminar...")
                    delete = self.room_input.room_repository.delete(number, self.db)
                    print(delete)
                else:
                    print("\n⚠️ Opción no válida. Intente nuevamente.")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.")

    def employee_menu(self):
        while True:
            self.display_header("GESTIÓN DE EMPLEADOS")
            print(" 1. Listar todos los empleados")
            print(" 2. Registrar nuevo empleado")
            print(" 3. Actualizar empleado")
            print(" 4. Eliminar empleado")
            print(" 0. Volver al menú principal")

            option = input("\nSeleccione una opción: ")

            try:
                option = int(option)

                if option == 0:
                    break
                elif option == 1:
                    self.employee_input.print_data()
                    input("\nPresione Enter para continuar...")
                elif option == 2:
                    self.employee_input.register(self.employee, self.db)
                    input("\nPresione Enter para continuar...")
                elif option == 3:
                    id_employee = input("Ingrese el número del empleado a actualizar: ")
                    name = input("Nombre del empleado: ")
                    last_name = input("Apellido del empleado: ")
                    email = input("Email del empleado: ")
                    password = input("Contraseña nueva: ")
                    status = input("Estado: ")
                    salary = input("salario: ")
                    result = self.employee_input.employee_repository.update(name,last_name, email, password, status, salary, id_employee, self.db)
                    print(result)
                    input("\nPresione Enter para continuar...")
                elif option == 4:
                    number = input("Ingrese el número de identificación del empleado que quiere eliminar")
                    result = self.employee_input.employee_repository.delete(number, self.db)
                    print(result)
                    input("\nPresione Enter para continuar...")
                else:
                    print("\n⚠️ Opción no válida. Intente nuevamente.")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.")

    def service_menu(self):
        while True:
            self.display_header("GESTIÓN DE SERVICIOS")
            print(" 1. Listar todos los servicios")
            print(" 2. Registrar nuevo servicio")
            print(" 3. Actualizar servicio")
            print(" 4. Eliminar servicio")
            print(" 0. Volver al menú principal")

            option = input("\nSeleccione una opción: ")

            try:
                option = int(option)

                if option == 0:
                    break
                elif option == 1:
                    self.service_input.services_service.print_all_services(self.db)
                    input("\nPresione Enter para continuar...")
                elif option == 2:
                    id_service = input("Ingrese el id del servicio que desea registrar: ")
                    description = input("Ingrese la descripción del servicio: ")
                    price = input("Ingrese el costo del servicio: ")
                    response = self.service_input.service_repository.create_service_repository(id_service, description, price, self.db)
                    print(response)
                    input("\nPresione Enter para continuar...")
                elif option == 3:
                    id_service = input("Ingrese el id del servicio que desea actualizar: ")
                    description = input("Ingrese la descripción del servicio: ")
                    price = input("Ingrese el costo del servicio: ")
                    update = self.service_input.service_repository.update_service(id_service, description, price, self.db)
                    print(update)
                    input("\nPresione Enter para continuar...")
                elif option == 4:
                    id_service = input("Ingrese el id del servicio que desea eliminar: ")
                    delete = self.service_input.service_repository.delete_service(id_service, self.db)
                    print(delete)
                    input("\nPresione Enter para continuar...")
                else:
                    print("\n⚠️ Opción no válida. Intente nuevamente.")
            except ValueError:
                print("\n⚠️ Por favor, ingrese un número válido.")




#
# class MenuApp:
#
#     def __init__(self):
#         self.db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel')
#         self.db.connection()
#         self.guest= Guest(None, None,None,None,None,None,None,None,None)
#         self.guest_service= GuestService()
#         self.guest_input= GuestInput()
#         self.room_input = RoomInput()
#         self.room = Room(None, None)
#         self.room_repository = RoomRepository
#
#     def init_app(self):
#         init = (int(input("Presione 1 para inicializar ")))
#
#         while init != 0:
#
#             option = int(input(" 1. Login \n 2. Registro \n 3. Gestión de Reservar \n 4. Salir \n"))
#
#             match option:
#                 case 1:
#                     print("login")
#                 case 2:
#                     print("Registro")
#                     self.guest_input.register(self.guest, self.db)
#                 case 3:
#                     self.reservation_menu()
#                 case 4:
#                     init = 0
#
#
#     def reservation_menu(self):
#         option = int(input(" 1. Consultar reserva \n 2. Reservar \n 3. Salir \n"))
#
#         match option:
#             case 1:
#                 print("haz consultado exitosamente")
#             case 2:
#                 print("Proceso de reserva")
#                 self.room_menu()
#             case 3:
#                 init = 0
#                 return init
#
#     def room_menu(self):
#         option = int(input(" 1.Listar habitaciones \n 2.Buscar por número \n 3.Registrar nueva habitación \n 4.Actualizar disponibilidad \n 5.Eliminar habitación \n"))
#
#         match option:
#             case 1:
#                 print("Listar habitaciones")
#                 nau = self.room_input.room_repository.find_all(self.db)
#                 print(nau)
#             case 2:
#                 print("Encontraste la habitación")
#             case 3:
#                 self.room_input.register(self.room, self.db)


