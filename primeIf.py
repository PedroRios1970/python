password = "ABC1230"


print ("Ejemplo con if/else")
if password == "ABC1234":
    print("La clave es correcta")
else:
    print("La clave es incorrecta")    

    """ Esto es con la sentencia elif """

password_2 ="root"    
usuario = "admin"

print("Ejemplo con if/elif")

if usuario == "admin" and password_2 == "root":
    print("Usuario Correcto | Clave Correcta")
elif usuario =="admin" and password_2 != "root":
    print("Usuario Correcto | Clave incorrecta")    

