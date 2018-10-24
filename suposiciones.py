def algoritmo(op,t):

    result = "\n"

    if op[1] == "+":

        if len(op[2]) == 2:

            for e in range(1,t + 1):
                for i in range(1,t + 1):
                    suma = e + i
                    if suma == op[0]:
                        result = result + str(e) + " + " + str(i) + "\n"

        if len(op[2]) == 3:

            for e in range(1,t + 1):
                for i in range(1,t + 1):
                    for j in range(1,t + 1):
                        suma = e + i + j
                        if suma == op[0]:
                            result = result + str(e) + " + " + str(i) +  " + "  + str(j) + "\n"

    if op[1] == "-":

        if len(op[2]) == 2:

            for e in range(1,t + 1):
                for i in range(1,t + 1):
                    resta = abs(e - i)
                    if resta == op[0]:
                        result = result + str(e) + " - "  + str(i) + "\n"

        if len(op[2]) == 3:

            for e in range(1,t + 1):
                for i in range(1,t + 1):
                    for j in range(1,t + 1):
                        resta = abs(e - i - j)
                        if resta == op[0]:
                            result = result + str(e) + " - " + str(i)  +  " - " + str(j) + "\n"

    if op[1] == "x":

        if len(op[2]) == 2:

            for e in range(1,t + 1):
                for i in range(1,t + 1):
                    resta = e * i
                    if resta == op[0]:
                        result = result  + str(e) + " x " + str(i) + "\n"

        if len(op[2]) == 3:

            for e in range(1,t + 1):
                for i in range(1,t + 1):
                    for j in range(1,t + 1):
                        resta = e * i * j
                        if resta == op[0]:
                            result = result + str(e)  + " x " + str(i)  +  " x " + str(j) + "\n"





























                            
