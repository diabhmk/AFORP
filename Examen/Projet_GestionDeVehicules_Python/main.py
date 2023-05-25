from vehicle_manager import VehicleManager
from statistics import Statistics

class Application:
    def __init__(self):
        self.vehicle_manager = VehicleManager()
        self.statistics = Statistics()

    def run(self):
        print("Bienvenue dans l'application de gestion de véhicules !")

        while True:
            print("\nMenu:")
            print("1. Ajouter un véhicule")
            print("2. Supprimer un véhicule")
            print("3. Modifier un véhicule")
            print("4. Afficher les statistiques de circulation")
            print("5. Afficher la liste complète des véhicules")
            print("6. Rechercher un véhicule")
            print("7. Quitter")

            choice = input("Choisissez une option : ")

            if choice == '1':
                self.vehicle_manager.add_vehicle()
            elif choice == '2':
                self.vehicle_manager.delete_vehicle()
            elif choice == '3':
                self.vehicle_manager.modify_vehicle()
            elif choice == '4':
                self.statistics.display_traffic_statistics()
            elif choice == '5':
                self.vehicle_manager.display_all_vehicles()
            elif choice == '6':
                self.vehicle_manager.search_vehicle()
            elif choice == '7':
                print("Merci d'avoir utilisé l'application !")
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    app = Application()
    app.run()
