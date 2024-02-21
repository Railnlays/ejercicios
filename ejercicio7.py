from dataclasses import dataclass

@dataclass
class Empleado:
    nombre: str
    edad: int
    salario: float

    def subir_salario(self, porcentaje: int) -> None:
        self.salario = self.salario * (1 + porcentaje / 100)

@dataclass
class Departamento:
    nombre: str
    empleados: list[Empleado]
    
    def __get_empleado__(self, nombre_empleado: str) -> Empleado:
        for empleado in self.empleados:
            if empleado.nombre == nombre_empleado:
                return empleado
    
    def agregar_empleado_departamento(self, empleado: Empleado) -> None:
        self.empleados.append(empleado)
    
    def quitar_empleado_departamento(self, nombre_empleado: str) -> None:
        nombre_empleado_a_quitar : Empleado = self.__get_empleado__(nombre_empleado)
        self.empleados.pop(nombre_empleado_a_quitar)

@dataclass
class Empresa:
    nombre: str
    departamentos: list[Departamento]
    empleados: list[Empleado]

    def __get_empleado__(self, nombre_empleado: str) -> Empleado:
        for empleado in self.empleados:
            if empleado.nombre == nombre_empleado:
                return empleado
    
    def __get_departamento__(self, nombre_departamento: str) -> Departamento:
        for departamento in self.departamentos:
            if departamento.nombre == nombre_departamento:
                return departamento
    
    def contratar(self, empleado: Empleado, nombre_departamento: str) -> None:
        self.empleados.append(empleado)
        departamento : Departamento = self.__get_departamento__(nombre_departamento)
        departamento.agregar_empleado_departamento(empleado)

    def despedir(self, nombre_empleado: str) -> None:
        nombre_empleado_a_quitar : Empleado = self.__get_empleado__(nombre_empleado)
        self.empleados.pop(nombre_empleado_a_quitar)
        #quitar de departamento

    def crear_departamento(self, departamento: Departamento) -> None:
        self.departamentos.append(departamento)

    def cerrar_departamento(self, departamento: str) -> None:
        antiguo_departamento: Departamento = self.__get_departamento__(departamento)        
        self.departamentos.pop(antiguo_departamento)

    def cambiar_empleado_de_departamento(self, nombre_empleado: str, nombre_antiguo_departamento: str, nombre_nuevo_departamento: str) -> None:
        antiguo_departamento: Departamento = self.__get_departamento__(nombre_antiguo_departamento)
        nuevo_departamento: Departamento = self.__get_departamento__(nombre_nuevo_departamento)
        empleado: Empleado = antiguo_departamento.quitar_empleado_departamento(nombre_empleado)
        nuevo_departamento.agregar_empleado_departamento(empleado)

repsol = Empresa("Repsol", [], [])
iberdrola = Empresa("Iberdrola", [], [])
santander = Empresa("Santander", [], [])

repsol.crear_departamento("Ventas")
repsol.crear_departamento("Marketing")
repsol.crear_departamento("Direccion")

iberdrola.crear_departamento("Ventas")
iberdrola.crear_departamento("Marketing")
iberdrola.crear_departamento("Direccion")

santander.crear_departamento("Ventas")
santander.crear_departamento("Marketing")
santander.crear_departamento("Direccion")

empleado_1 = Empleado("Juan", 30, 50000)
empleado_2 = Empleado("Ana", 28, 45000)
empleado_3 = Empleado("Maria", 50, 65000)

iberdrola.contratar(empleado_1, "Ventas")
iberdrola.contratar(empleado_2, "Marketing")
iberdrola.contratar(empleado_3, "Direccion")

print(iberdrola.empleados)

print(repsol.departamentos)
