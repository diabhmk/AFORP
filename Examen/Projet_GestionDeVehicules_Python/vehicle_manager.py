from vehicle import Car, Motorcycle, Bus, Metro

class VehicleManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        print("\nAjout d'un véhicule:")
        vehicle_type = input("Type de véhicule (car/motorcycle/bus/metro) : ")
        brand = input("Marque : ")
        model = input("Modèle : ")
        year = input("Année : ")
        color = input("Couleur : ")

        if vehicle_type == 'car':
            num_doors = input("Nombre de portes : ")
            vehicle = Car(brand, model, year, color, num_doors)
        elif vehicle_type == 'motorcycle':
            num_wheels = input("Nombre de roues : ")
            vehicle = Motorcycle(brand, model, year, color, num_wheels)
        elif vehicle_type == 'bus':
            seating_capacity = input("Capacité d'assise : ")
            vehicle = Bus(brand, model, year, color, seating_capacity)
        elif vehicle_type == 'metro':
            num_cars = input("Nombre de voitures : ")
            vehicle = Metro(brand, model, year, color, num_cars)
        else:
            print("Type de véhicule invalide.")
            return

        self.vehicles.append(vehicle)
        print("Le véhicule a été ajouté avec succès.")

    def delete_vehicle(self):
        print("\nSuppression d'un véhicule:")
        vehicle_index = self._get_vehicle_index("Veuillez entrer le numéro d'index du véhicule à supprimer : ")

        if vehicle_index is not None:
            del self.vehicles[vehicle_index]
            print("Le véhicule a été supprimé avec succès.")

    def modify_vehicle(self):
        print("\nModification d'un véhicule:")
        vehicle_index = self._get_vehicle_index("Veuillez entrer le numéro d'index du véhicule à modifier : ")

        if vehicle_index is not None:
            vehicle = self.vehicles[vehicle_index]
            print(f"Modifiez les attributs du véhicule (laissez vide pour conserver la valeur actuelle):")
            brand = input(f"Marque ({vehicle.brand}) : ")
            model = input(f"Modèle ({vehicle.model}) : ")
            year = input(f"Année ({vehicle.year}) : ")
            color = input(f"Couleur ({vehicle.color}) : ")

            if isinstance(vehicle, Car):
                num_doors = input(f"Nombre de portes ({vehicle.num_doors}) : ")
                if num_doors:
                    vehicle.num_doors = num_doors
            elif isinstance(vehicle, Motorcycle):
                num_wheels = input(f"Nombre de roues ({vehicle.num_wheels}) : ")
                if num_wheels:
                    vehicle.num_wheels = num_wheels
            elif isinstance(vehicle, Bus):
                seating_capacity = input(f"Capacité d'assise ({vehicle.seating_capacity}) : ")
                if seating_capacity:
                    vehicle.seating_capacity = seating_capacity
            elif isinstance(vehicle, Metro):
                num_cars = input(f"Nombre de voitures ({vehicle.num_cars}) : ")
                if num_cars:
                    vehicle.num_cars = num_cars

            if brand:
                vehicle.brand = brand
            if model:
                vehicle.model = model
            if year:
                vehicle.year = year
            if color:
                vehicle.color = color

            print("Le véhicule a été modifié avec succès.")

    def display_all_vehicles(self):
        if not self.vehicles:
            print("Aucun véhicule enregistré.")
            return

        print("\nListe des véhicules enregistrés :")
        for index, vehicle in enumerate(self.vehicles):
            print(f"{index+1}. {vehicle.get_details()}")

    def search_vehicle(self):
        print("\nRecherche d'un véhicule:")
        search_term = input("Entrez le terme de recherche (numéro d'immatriculation, marque, etc.) : ")

        results = []
        for vehicle in self.vehicles:
            if search_term.lower() in vehicle.get_details().lower():
                results.append(vehicle)

        if results:
            print("Résultats de la recherche :")
            for index, vehicle in enumerate(results):
                print(f"{index+1}. {vehicle.get_details()}")
        else:
            print("Aucun résultat trouvé.")

    def _get_vehicle_index(self, message):
        if not self.vehicles:
            print("Aucun véhicule enregistré.")
            return None

        self.display_all_vehicles()

        while True:
            index = input(message)

            try:
                index = int(index)
                if 1 <= index <= len(self.vehicles):
                    return index - 1
                else:
                    print("Numéro d'index invalide. Veuillez entrer un numéro d'index valide.")
            except ValueError:
                print("Numéro d'index invalide. Veuillez entrer un numéro d'index valide.")
