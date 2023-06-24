from persona import persona

paciente=persona("cc",1023025723,"julieth","rodriguez",45,1.60,25,"femenino")

paciente.pedirDatos()
paciente.mostrarPersona()

print("el peso ideal es",paciente.calcularImc())

paciente.mayorEdad()
