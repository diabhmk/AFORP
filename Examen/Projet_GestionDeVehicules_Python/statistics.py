from vehicle_manager import VehicleManager

class Statistics:
    def __init__(self):
        self.vehicle_manager = VehicleManager()

    def display_traffic_statistics(self):
        print("\nStatistiques de circulation:")
        print("1. Afficher le nombre total de véhicules enregistrés")
        print("2. Afficher le nombre de voitures rouges")
        print("3. Afficher le nombre de motos")
        print("4. Afficher le nombre d'autobus")
        print("5. Afficher le nombre de métros")

        choice = input("Choisissez une option : ")

        if choice == '1':
            self._display_total_vehicles()
        elif choice == '2':
            self._display_red_cars()
        elif choice == '3':
            self._display_motorcycles()
        elif choice == '4':
            self._display_buses()
        elif choice == '5':
            self._display_metros()
        else:
            print("Option invalide. Veuillez choisir une option valide.")

    def _display_total_vehicles(self):
        count = len(self.vehicle_manager.vehicles)
        print(f"Nombre total de véhicules enregistrés : {count}")

    def _display_red_cars(self):
        count = sum(1 for vehicle in self.vehicle_manager.vehicles if isinstance(vehicle, Car) and vehicle.color.lower() == 'rouge')
        print(f"Nombre de voitures rouges : {count}")

    def _display_motorcycles(self):
        count = sum(1 for vehicle in self.vehicle_manager.vehicles if isinstance(vehicle, Motorcycle))
        print(f"Nombre de motos : {count}")

    def _display_buses(self):
        count = sum(1 for vehicle in self.vehicle_manager.vehicles if isinstance(vehicle, Bus))
        print(f"Nombre d'autobus : {count}")

    def _display_metros(self):
        count = sum(1 for vehicle in self.vehicle_manager.vehicles if isinstance(vehicle, Metro))
        print(f"Nombre de métros : {count}")
