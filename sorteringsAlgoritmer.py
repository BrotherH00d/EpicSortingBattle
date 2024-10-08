import random, tests
# items = items.copy()
def bubble_Sort(arr):
    arr = arr.copy()
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Sample list to be sorted
"""arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)"""
def insertionSort(arr):
    arr = arr.copy()
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return arr # hvis der kun er 1 eller mindre (aka 0) elementer så er listen allerede sorteret og derfor er der e return

    for i in range(1, n):  # starter med at chekke det andet element i listen for at senere kunne sammenligne det med det første
        key = arr[i]  # gemmer det aktuelle element så man kan rykke det
        j = i - 1
        while j >= 0 and key < arr[j]:  # cheaker om det element man har nu er støre end det næste. hvis ja gør nedenstående
            arr[j + 1] = arr[j]  # hvis det element man er ved er støre end det bagved rykker man det aktuelle element en position frem
            j -= 1
        arr[j + 1] = key  # flyt elementet til rigtige plads
    return arr

if __name__ == '__main__':
    ## Skriv navnet på den algoritme, der skal testes
    algorithm = insertionSort

    passedTest = True
    for i in range(10):
        l = list(range(0, 10))
        lb = l.copy()
        random.shuffle(lb)
        ls = lb.copy()
        if not tests.sortsCorrectly(ls, algorithm):
            passedTest = False
            break

    if passedTest:
        print('Succes! Algoritmen sorterer korrekt.')
    else:
        print('Fejl! Algoritmen kan ikke sortere.')

    print('blandet: ', lb)
    print('sorteret:', algorithm(ls))
