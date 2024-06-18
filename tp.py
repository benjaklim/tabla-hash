class Pokemon:
    def __init__(self, numero, nombre, tipos, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos
        self.nivel = nivel

    def __repr__(self):
        return f"{self.nombre} (Número: {self.numero}, Tipos: {self.tipos}, Nivel: {self.nivel})"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_tipo(self, tipo):
        return sum(ord(c) for c in tipo) % self.size

    def hash_numero(self, numero):
        return numero % 10

    def hash_nivel(self, nivel):
        return nivel // 10

    def insert(self, key, value, hash_function):
        index = hash_function(key)
        self.table[index].append(value)

    def get_pokemons(self, condition):
        result = []
        for bucket in self.table:
            for pokemon in bucket:
                if condition(pokemon):
                    result.append(pokemon)
        return result

class Pokedex:
    def __init__(self):
        self.hash_tipo = HashTable(20)
        self.hash_numero = HashTable(10) 
        self.hash_nivel = HashTable(10) 

    def agregar_pokemon(self, pokemon):
        for tipo in pokemon.tipos:
            self.hash_tipo.insert(tipo, pokemon, self.hash_tipo.hash_tipo)

        self.hash_numero.insert(pokemon.numero, pokemon, self.hash_numero.hash_numero)

        self.hash_nivel.insert(pokemon.nivel, pokemon, self.hash_nivel.hash_nivel)

    def mostrar_pokemons_terminan_en(self, digitos):
        return self.hash_numero.get_pokemons(lambda p: p.numero % 10 in digitos)

    def mostrar_pokemons_nivel_multiplo_de(self, multiplos):
        return self.hash_nivel.get_pokemons(lambda p: any(p.nivel % m == 0 for m in multiplos))

    def mostrar_pokemons_de_tipo(self, tipos):
        result = []
        for tipo in tipos:
            result.extend(self.hash_tipo.get_pokemons(lambda p: tipo in p.tipos))
        return result


pokedex = Pokedex()

pokedex.agregar_pokemon(Pokemon(1, 'Bulbasaur', ['Planta', 'Veneno'], 5))
pokedex.agregar_pokemon(Pokemon(2, 'Ivysaur', ['Planta', 'Veneno'], 10))
pokedex.agregar_pokemon(Pokemon(4, 'Charmander', ['Fuego'], 15))
pokedex.agregar_pokemon(Pokemon(6, 'Charizard', ['Fuego', 'Volador'], 36))
pokedex.agregar_pokemon(Pokemon(7, 'Squirtle', ['Agua'], 8))
pokedex.agregar_pokemon(Pokemon(25, 'Pikachu', ['Eléctrico'], 12))
pokedex.agregar_pokemon(Pokemon(50, 'Diglett', ['Tierra'], 22))
pokedex.agregar_pokemon(Pokemon(51, 'Dugtrio', ['Tierra'], 31))
pokedex.agregar_pokemon(Pokemon(63, 'Abra', ['Psíquico'], 16))
pokedex.agregar_pokemon(Pokemon(93, 'Haunter', ['Fantasma', 'Veneno'], 25))
pokedex.agregar_pokemon(Pokemon(100, 'Voltorb', ['Eléctrico'], 15))
pokedex.agregar_pokemon(Pokemon(144, 'Articuno', ['Hielo', 'Volador'], 50))
pokedex.agregar_pokemon(Pokemon(157, 'Typhlosion', ['Fuego'], 50))
pokedex.agregar_pokemon(Pokemon(212, 'Scizor', ['Bicho', 'Acero'], 35))

# e
print("Pokémons cuyos números terminan en 3, 7 y 9:")
print(pokedex.mostrar_pokemons_terminan_en([3, 7, 9]))

# f
print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:")
print(pokedex.mostrar_pokemons_nivel_multiplo_de([2, 5, 10]))

# g
print("Pokémons de tipos Acero, Fuego, Eléctrico, Hielo:")
print(pokedex.mostrar_pokemons_de_tipo(['Acero', 'Fuego', 'Eléctrico', 'Hielo']))
