% verifica que un libro es disponible para su reserva o prestamo

esta_disponible(Libro) :-
not(prestado(Libro)),
not(reservado(Libro)).

prestable(Libro) :-
es_impreso(Libro).

reservable(Libro) :-
es_impreso(Libro).

vendible(Libro) :-
es_digital(Libro).

es_moroso(Lector) :-
tiene(Lector, prestado(Libro, Xdias)),
max_dias_prestamo(Libro, Dias),
Xdias > Dias.

es_multable(Lector) :-
es_moroso(Lector).

puede_prestar(Lector, Libro) :-
prestable(Libro),
esta_disponible(Libro),
tiene(Lector, prestado(Xlibros)),
cant_max_libro_prestable(Lector, Cantidad),
Cantidad > Xlibros,
not(es_moroso(Lector)).

puede_reservar(Lector, Libro) :-
reservable(Libro),
esta_disponible(Libro),
tiene(Lector, reservado(Xlibros)),
cant_max_libro_reservable(Lector, Cantidad),
Cantidad > Xlibros,
not(es_moroso(Lector)).

es_digital(libro1).
es_digital(libro4).
es_impreso(libro2).
es_impreso(libro3).
prestado(libro2).
reservado(libro2).
max_dias_prestamo(_,9).
max_dias_reserva(_, 10).
cant_max_libro_prestable(_, 3).
cant_max_libro_reservable(_, 3).

tiene(lector1, prestado(libro2, 4)).
tiene(lector2, prestado(libro2, 10)).
tiene(lector3, reservado(libro3, 2)).
tiene(lector1, prestado(3)).
tiene(lector2, prestado(2)).
tiene(lector3, prestado(0)).



