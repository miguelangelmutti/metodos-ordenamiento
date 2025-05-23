import time
import random
import pandas as pd # Import pandas



def quick_sort(arr):
    # Inicializamos el contador de intercambios antes de llamar a la función auxiliar
    exchanges = [0]  # Usamos una lista para que el valor sea mutable y pueda ser modificado por quick_sort_helper    
    quick_sort_helper(arr, 0, len(arr) - 1, exchanges)
    # Devolvemos el número de intercambios
    swaps = exchanges[0]
    return swaps
                        
def quick_sort_helper(arr, low, high, exchanges):
    if low < high:
        pivot_index = partition(arr, low, high, exchanges)

        quick_sort_helper(arr, low, pivot_index - 1, exchanges)
        quick_sort_helper(arr, pivot_index + 1, high, exchanges)

def partition(arr, low, high, exchanges):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            exchanges[0] += 1  # Incrementamos el contador de intercambios
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    exchanges[0] += 1  # Incrementamos el contador de intercambios por el intercambio final del pivote
    return i + 1

# ... (your sorting algorithm definitions) ...


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    swaps = 0  # Inicializamos el contador de intercambios

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i

            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                swaps += 1  # Incrementamos el contador por cada movimiento (intercambio implícito)
                j -= gap
            if arr[j] != key: # Solo contamos un "intercambio" si el elemento se movió de su posición original
                arr[j] = key
                swaps += 1
        gap //= 2
    return swaps


def bubble_sort_opt(arr):
    n = len(arr)
    intercambios = 0  # Inicializamos el contador de intercambios        

    for i in range(n):
        # El bucle interno se ejecuta hasta n-i-1 porque los últimos 'i' elementos
        # ya están en su posición correcta.
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambios += 1  # Incrementamos el contador cada vez que hay un intercambio            
    
    return intercambios


def bubble_sort(arr):
    n = len(arr)
    intercambios = 0  # Inicializamos el contador de intercambios
    
    for i in range(n):
        for j in range(0, n-i-1): # Pequeña optimización: el elemento más grande ya estará al final después de cada pasada
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambios += 1  # Incrementamos el contador por cada intercambio    

    return intercambios # Devolvemos el arreglo ordenado, la cantidad de intercambios y el tiempo


def generar_lista_aleatoria(largo):
    return [random.randint(0, largo * 10) for _ in range(largo)]





if __name__ == "__main__":

    #lenghts = [10, 100, 1000, 10000, 100000, 1000000]
    lenghts = [10, 100, 1000, 10000]

    algorithms = {
        "bubble sort optimizado": bubble_sort_opt,
        "quick sort": quick_sort,
        "shell sort": shell_sort,
        "bubblesort": bubble_sort
    }

    all_results = [] # This will store dictionaries, which pandas will convert to a DataFrame


    for largo in lenghts:
        print(f"Testing with list length: {largo}")
        original_list = generar_lista_aleatoria(largo)

        for algo_name, algo_function in algorithms.items():
            list_to_sort = original_list[:]

            start_time = time.time()
            num_swaps = algo_function(list_to_sort)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000

            all_results.append({
                "algoritmo": algo_name,
                "n_elementos": largo,
                "tiempo": round(execution_time, 2),
                "intercambios": num_swaps
            })

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(all_results)

    # Save to CSV
    df.to_csv("sorting_results_pandas.csv", index=False) # index=False prevents writing the DataFrame index as a column

    # Save to Excel (requires openpyxl or xlwt/xlsxwriter installed: pip install openpyxl)
    # df.to_excel("sorting_results_pandas.xlsx", index=False)

    print(f"Results saved to sorting_results_pandas.csv (and optionally .xlsx) using pandas.")