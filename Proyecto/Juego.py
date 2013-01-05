print "Bienvenidos a Dark Quest"
print "Seleccione una opcion del menu:"
print "1. Juego nuevo"
print "2. Salir del juego"
#Coger valor de 1 o 2 y ejecutar accion correspondiente

#Musica introductoria y voces

print "Hace tiempo atras atras, en el pacifico reino de Belavir ocurrio una catastrofe."
print "Un tesoro de la realeza fue robado por un demonio."
print "Este tesoro tenia un valor inimaginable, ya que dentro de si,"
print "contenia los poderes de un antiguo rey demonio que fue sellado hace mucho tiempo."
print "Debido a esto, Faris, un joven heroe ha decidido ir en busca del tesoro al calabozo del demonio..."

#Dialogo de entrada a la cueva

print "Frente a ti se encuentran 3 caminos, el de la izquierda está iluminado por antorchas y se observa un brillo al final del tunel."
print "El del medio está totalmente oscuro, y el de la derecha tiene algunas antorchas, pero tiene un olor nauseabundo."
print "¿Cual escogeras?"
print "1. Izquierda"
print "2. Medio"
print "3. Derecha"

Opcion1 = int(raw_input())

#Coger valor de 1, 2 o 3 y ejectuar accion

if Opcion1 == 1: 
    #Para Opcion 1:
    print "Has procedido por el camino de la izquierda."
    print "Luego de caminar por unos momentos, has encontrado un cofre con una pocion."


#Para Opcion 2:
if Opcion1 == 2:
    print "Has escogido el camino del centro."
    print "Luego de caminar por un tiempo, te encuentras en una emboscada puesta por un orco."
    print "Lo logras derrotar, pero has perdido 5 puntos de vida."

#Para Opcion 3:
if Opcion1 == 3:
    print " Has escogido el camino de la derecha."
    print "Luego de caminar por un tiempo no encuentras nada mas que el camino hacia la siguiente zona."

print "Has llegado a otro punto donde el camino se divide en 3."
print "El camino de la izquierda comienza a ser de piedra luego de unos metros."
print "El camino del medio luego de cierta distancia comienza a descender."
print "El camino de la derecha sigue siendo de tierra hasta donde se puede observar."
print "¿Que camino escogeras?"
print "1. Izquierda"
print "2. Medio"
print "3. Derecha"
Opcion2 = int(raw_input())


#Coger el valor de 1 2 o 3
if Opcion2 == 1: 
    #Opcion 1
    print " Has escogido el camino de piedra."
    print "Sigues por este camino sin ningun contratiempo y eventualmente llegas a la zona final del calabozo."

if Opcion2 == 2: 
    #Opcion 2 
    print "Has escogido el camino del centro."
    print "Despues de avanzar un poco caes en una trampa y pierdes 5 puntos de vida."
    print "Eventualmente llegas a la zona final del calabozo."

if Opcion2 == 3:

    #Opcion 3
    print "Has escogido el camino de la derecha."
    print "En el camino encuentras una pocion y eventualmente llegas a la zona final del calabozo."

print "Has llegado a la zona final."
print "Frente a ti hay 3 puertas."
print "A la izquierda hay una puerta de piedra con calaveras talladas en ella."
print "En el medio hay una puerta hecha de huesos de humanos."
print "A la derecha hay una puerta de madera casi desarmada con manchas de sangre."

print "¿Cual puerta escogeras?"
print "1. Puerta de piedra"
print "2. Puerta de huesos"
print "3. Puerta de madera"
Opcion3 = int(raw_input())

if Opcion3 == 1:
    print "Has seleccionado la puerta de piedra."
    print "El camino esta totalmente oscuro, pero decides seguir adelante."
    print "Eventualmente caes en una trampa fatal y tu aventura se termina..."
    print "GAME OVER"

if Opcion3 == 2:
    print "Has seleccionado la puerta de huesos."
    print "Esta te conduce directamente hacia el jefe del calabozo, Catastrofe"

if Opcion3 == 3:
    print "Has seleccionado la puerta de huesos."
    print "Esta te conduce directamente hacia el jefe del calabozo, Catastrofe"

