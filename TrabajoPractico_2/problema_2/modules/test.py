if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()

    # Simulamos fechas como enteros (por ejemplo, YYYYMMDD)
    arbol.agregar(20250101, 30)
    arbol.agregar(20250102, 32)
    arbol.agregar(20250103, 28)
    arbol.agregar(20250104, 35)
    arbol.agregar(20250105, 31)

    print("Recorrido del árbol:")
    arbol.recorrido_inorder()

    print("\nTemperatura máxima entre 20250102 y 20250104:")
    print(arbol.max_in_range(20250102, 20250104))  # Debería devolver 35
