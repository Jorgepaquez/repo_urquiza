```mermaid
classDiagram
    class Pelicula {
        +String titulo
        +String director
        +String imdbId
        +boolean estaDisponible()
    }

    class Genero {
        +String nombre
        +String idGenero
        +asignarPelicula(Pelicula pelicula)
        +eliminarPelicula(Pelicula pelicula)
    }

    class Duracion {
        +String tiempo
        +List peliculas
        +List generos
        +agregarGenero(Genero genero)
    }

    Pelicula --> Genero : "asociado con"
    Pelicula --> Duracion : "dura"
