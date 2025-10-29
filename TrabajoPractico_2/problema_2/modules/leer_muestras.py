# -*- coding: utf-8 -*-
# main.py

from database import Temperaturas_DB
import os

def main():
    print("Initializing Temperature Database...")
    db = Temperaturas_DB()
    
    # Load temperature data from file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'muestras.txt')
    print(f"Loading temperature data from {file_path}...")
    db.cargar_muestras_desde_archivo(file_path)
    print(f"Successfully loaded {db.cantidad_muestras()} temperature records.")
    
    while True:
        print("\nTemperature Database Menu:")
        print("1. Add Temperature")
        print("2. Get Temperature")
        print("3. Get Max Temperature in Range")
        print("4. Get Min Temperature in Range")
        print("5. Get Temperature Extremes in Range")
        print("6. Delete Temperature")
        print("7. List Temperatures in Range")
        print("8. Total Samples")
        print("9. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            fecha = input("Enter date (dd/mm/yyyy): ")
            temperatura = float(input("Enter temperature: "))
            db.guardar_temperatura(temperatura, fecha)
            print("Temperature added.")
        
        elif choice == '2':
            fecha = input("Enter date (dd/mm/yyyy): ")
            temp = db.devolver_temperatura(fecha)
            print(f"Temperature on {fecha}: {temp} ºC" if temp is not None else "No record found.")
        
        elif choice == '3':
            fecha1 = input("Enter start date (dd/mm/yyyy): ")
            fecha2 = input("Enter end date (dd/mm/yyyy): ")
            max_temp = db.max_temp_rango(fecha1, fecha2)
            print(f"Max temperature from {fecha1} to {fecha2}: {max_temp} ºC" if max_temp is not None else "No records found.")
        
        elif choice == '4':
            fecha1 = input("Enter start date (dd/mm/yyyy): ")
            fecha2 = input("Enter end date (dd/mm/yyyy): ")
            min_temp = db.min_temp_rango(fecha1, fecha2)
            print(f"Min temperature from {fecha1} to {fecha2}: {min_temp} ºC" if min_temp is not None else "No records found.")
        
        elif choice == '5':
            fecha1 = input("Enter start date (dd/mm/yyyy): ")
            fecha2 = input("Enter end date (dd/mm/yyyy): ")
            min_temp, max_temp = db.temp_extremos_rango(fecha1, fecha2)
            if min_temp is not None and max_temp is not None:
                print(f"Temperature extremes from {fecha1} to {fecha2}: Min {min_temp} ºC, Max {max_temp} ºC")
            else:
                print("No records found.")
        
        elif choice == '6':
            fecha = input("Enter date (dd/mm/yyyy): ")
            db.borrar_temperatura(fecha)
            print("Temperature record deleted.")
        
        elif choice == '7':
            fecha1 = input("Enter start date (dd/mm/yyyy): ")
            fecha2 = input("Enter end date (dd/mm/yyyy): ")
            records = db.devolver_temperaturas(fecha1, fecha2)
            print("Temperatures in range:")
            for record in records:
                print(record)
        
        elif choice == '8':
            total_samples = db.cantidad_muestras()
            print(f"Total temperature records: {total_samples}")
        
        elif choice == '9':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()