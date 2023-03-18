for i in range(10):
    for j in range(i + 1, 10):
        for k in range(j + 1, 10):
            combinaison = f"{i}{j}{k}"
            print(combinaison, end=" ")