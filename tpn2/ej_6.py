class familia:
    def __init__(self, nom_padre, nom_madre, hijos):
        self.nom_padre = nom_padre
        self.nom_madre = nom_madre
        self.hijos = []

    def __str__(self):
        hijos_str = ", ".join(self.hijos)
        return f"Padre: {self.nom_padre}, Madre: {self.nom_madre}, Hijos: {hijos_str}"


familia_fin=familia()
