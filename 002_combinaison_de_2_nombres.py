for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if int(f"{i}{j}") < int(f"{k}{l}"):
                    print(f"{i}{j} {k}{l}", end=", ")
mv 