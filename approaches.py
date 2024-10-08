import random
import help

class Approaches() :
    def __init__(self) :
        self.helper = help.Helper()

    def find_indices(self, input_list, element):
            return [i for i, x in enumerate(input_list) if x == element]

    def completely_random(self, n, occupyAll=False) :
        print('ABORDAGEM COMPLETAMENTE ALEATORIA:')

        facility = [0] * n
        index_list = [i for i in range(0,n)]
        steps = 0
        discomfort = 0
        disc_list = []

        while (index_list) :
            if (occupyAll) :
                idx = random.choice(index_list)
                facility[idx] = 1
                index_list.remove(idx)
                steps += 1
            elif (self.helper.find_sublist_start_index([1,1], facility) == -1) :
                idx = random.choice(index_list)
                facility[idx] = 1
                index_list.remove(idx)
                steps += 1
            else :
                break
            discomfort = self.helper.count_discomfort(facility)
            disc_list.append(discomfort)

            print(f'Indice escolhido: {idx}')
            print(f'Instalacao: {facility}')
            print(f'Coef. incomodo global: {discomfort}')

        print()
        return steps, discomfort, disc_list

    def individualist(self, n, occupyAll=False) :
        print('ABORDAGEM INDIVIDUALISTA: ')

        facility = [0] * n
        index_list = [i for i in range(0,n)]
        steps = 0
        discomfort = 0
        disc_list = []

        while (index_list) :
            idx = random.choice(index_list)
            facility[idx] = 1
            index_list.remove(idx)

            if (not occupyAll) :
                if idx > 0 and idx-1 in index_list :
                    index_list.remove(idx-1)
                if idx < n-1 and idx+1 in index_list :
                    index_list.remove(idx+1)

            steps += 1

            discomfort = self.helper.count_discomfort(facility)
            disc_list.append(discomfort)

            print(f'Indice escolhido: {idx}')
            print(f'Instalacao: {facility}')
            print(f'Coef. incomodo global: {discomfort}')

        print()
        return steps, discomfort, disc_list

    def altruistic(self, n, occupyAll=False) :
        print('ABORDAGEM ALTRUÍSTICA: ')

        facility = [0] * n
        index_list = []
        steps = 0
        discomfort = 0
        disc_list = []

        if (not occupyAll) :
            if (n % 2 == 0) :
                coin = random.randint(0,1)
                index_list = [i for i in range(coin,n,2)]
            else :
                index_list = [i for i in range(0,n,2)]
        else :
            index_list = [i for i in range(0,n)]

        while (index_list) :
            idx = random.choice(index_list)
            facility[idx] = 1
            index_list.remove(idx)

            steps += 1

            discomfort = self.helper.count_discomfort(facility)
            disc_list.append(discomfort)

            print(f'Indice escolhido: {idx}')
            print(f'Instalacao: {facility}')
            print(f'Coef. incomodo global: {discomfort}')

        print()
        return steps, discomfort, disc_list

    def individualist_altruistic(self, n, occupyAll=False) :
        print('ABORDAGEM INDIVIDUALISTA-ALTRUÍSTICA: ')

        facility = [0] * n
        index_list = [i for i in range(n)]
        steps = 0
        discomfort = 0
        disc_list = []

        # print(f'Lista de indices: {index_list}')

        if (n == 1) :
            idx = random.choice(index_list)
            facility[idx] = 1
            index_list.remove(idx)
            steps += 1
            discomfort = self.helper.count_discomfort(facility)
            disc_list.append(discomfort)

            print(f'Indice escolhido: {idx}')
            print(f'Instalacao: {facility}')
            print(f'Coef. incomodo global: {discomfort}')


        else :
            coin = random.randint(0, 1)

            if (coin) :
                seq = [n-1]
                if (n > 2 or occupyAll) :
                    seq.append(0) # para n=2, pegar so o inicio de seq, so pode popular tudo se permitido
            else :
                seq = [0]
                if (n > 2 or occupyAll) :
                    seq.append(n-1) # para n=2, pegar so o inicio de seq, so pode popular tudo se permitido

            while (seq):
                # print(steps, n)
                idx = seq.pop(0)
                facility[idx] = 1
                if (idx == 0) :
                    if (facility[idx+1] == 0) :
                        facility[idx+1] = 'X'
                if (idx == n-1) :
                    if (facility[idx-1] == 0) :
                        facility[idx-1] = 'X'
                index_list.remove(idx)
                discomfort = self.helper.count_discomfort(facility)
                disc_list.append(discomfort)

                print(f'Indice escolhido: {idx}')
                print(f'Instalacao: {facility}')
                print(f'Coef. incomodo global: {discomfort}')

                # print(f'Instalacao: {facility}')
                # print(f'Lista de indices: {index_list}')
                steps += 1

            while (index_list) :
                # print(steps, n)

                if (self.helper.find_sublist_start_index([0], facility) != -1) :
                    coin = random.randint(0, 1)
                    if (coin) :
                        pos = self.helper.find_sublist_start_index([0, 'X'], facility)
                        if (pos != -1) :
                            idx = pos
                            facility[idx] = 1
                            if (facility[idx-1] == 0) :
                                facility[idx-1] = 'X'
                            index_list.remove(idx)
                            # print(index_list)
                            # print(f'Lista de indices: {index_list}')
                    else :
                        pos = self.helper.find_sublist_start_index(['X', 0], facility)
                        if (pos != -1) :
                            idx = pos + 1
                            facility[idx] = 1
                            if (facility[idx+1] == 0) :
                                facility[idx+1] = 'X'
                            index_list.remove(idx)
                            # print(index_list)
                            # print(f'Lista de indices: {index_list}')

                else :
                    pos = self.helper.find_sublist_start_index(['X', 'X'], facility)
                    if (occupyAll) :
                        if (pos != -1) :
                            coin = random.randint(0, 1)
                            idx = pos + coin
                        else :
                            idx = random.choice(index_list)
                        facility[idx] = 1
                        index_list.remove(idx)
                        # print(index_list)
                        # print(f'Lista de indices: {index_list}')
                    else :
                        break

                steps += 1
                # print(f'Instalacao: {facility}')

                discomfort = self.helper.count_discomfort(facility)
                disc_list.append(discomfort)

                print(f'Indice escolhido: {idx}')
                print(f'Instalacao: {facility}')
                print(f'Coef. incomodo global: {discomfort}')

        print()
        return steps, discomfort, disc_list #, facility

    def cleaner(self, n) :
        print('ABORDAGEM DO FAXINEIRO: ')

        facility = [0] * n
        index_list = []
        steps = 0
        discomfort = 0

        if (n % 2 == 0) :
            coin = random.randint(0,1)
            index_list = [i for i in range(coin,n,2)]
        else :
            if (n == 1) :
                index_list = [i for i in range(0,n,2)]
            else :
                index_list = [i for i in range(1,n,2)]

        while (index_list) :
            idx = random.choice(index_list)
            facility[idx] = 1
            index_list.remove(idx)

            steps += 1

            print(f'Indice escolhido: {idx}')
            print(f'Instalacao: {facility}')

        discomfort = self.helper.count_discomfort(facility)

        print(f'Coef. incomodo global: {discomfort}')

        print()
        return steps, discomfort

    def discomfort_minimization(self, n, users) :
        print('ABORDAGEM DE MINIMIZACAO DO INCOMODO: ')

        if (users > n) :
            raise ValueError("Erro: número de usuários maior do que a capacidade da instalação!\n")

        facility = [0] * n
        index_list = [i for i in range(0,n)]
        neighborhood = [1] + [2] * (n-2) + [1]
        steps = 0
        disc_list = []

        while (users) :
            coin = random.randint(0,1)

            if (coin == 0) :
                # testa se o recurso mais à esquerda está disponível
                if (not facility[0]) :
                    facility[0] = 1
                    index_list.remove(0)
                    neighborhood[1] -= 1
                    print(f'Indice escolhido: {0}')
                    print(f'Instalacao: {facility}')
                    print(f'Mapa de adjacencias: {neighborhood}')
                    
                elif (not facility[n-1]) :
                    facility[n-1] = 1
                    index_list.remove(n-1)
                    neighborhood[n-2] -= 1
                    print(f'Indice escolhido: {n-1}')
                    print(f'Instalacao: {facility}')
                    print(f'Mapa de adjacencias: {neighborhood}')
                
                else :
                    two_neighbors_indices = self.find_indices(neighborhood, 2)
                    one_neighbor_indices = self.find_indices(neighborhood, 1)

                    while (two_neighbors_indices) :
                        idx = random.choice(two_neighbors_indices)
                        two_neighbors_indices.remove(idx)
                        if (not facility[idx]) :
                            facility[idx] = 1
                            index_list.remove(idx)
                            neighborhood[idx-1] -= 1
                            neighborhood[idx+1] -= 1

                            print(f'Indice escolhido: {idx}')
                            print(f'Instalacao: {facility}')
                            print(f'Mapa de adjacencias: {neighborhood}')
                            break
                    
                    else :
                        while (one_neighbor_indices) :
                            idx = random.choice(one_neighbor_indices)
                            one_neighbor_indices.remove(idx)
                            if (not facility[idx]) :
                                facility[idx] = 1
                                index_list.remove(idx)
                                neighborhood[idx-1] -= 1
                                neighborhood[idx+1] -= 1

                                print(f'Indice escolhido: {idx}')
                                print(f'Instalacao: {facility}')
                                print(f'Mapa de adjacencias: {neighborhood}')
                                break

                        else :
                            idx = random.choice(index_list)
                            if (not facility[idx]) :
                                facility[idx] = 1
                                index_list.remove(idx)
                                neighborhood[idx-1] -= 1
                                neighborhood[idx+1] -= 1

                                print(f'Indice escolhido: {idx}')
                                print(f'Instalacao: {facility}')
                                print(f'Mapa de adjacencias: {neighborhood}')

            else :
                # testa se o recurso mais à direita está disponível    
                if (not facility[n-1]) :
                    facility[n-1] = 1
                    index_list.remove(n-1)
                    neighborhood[n-2] -= 1

                    print(f'Indice escolhido: {n-1}')
                    print(f'Instalacao: {facility}')
                    print(f'Mapa de adjacencias: {neighborhood}')
                
                elif (not facility[0]) :
                    facility[0] = 1
                    index_list.remove(0)
                    neighborhood[1] -= 1

                    print(f'Indice escolhido: {0}')
                    print(f'Instalacao: {facility}')
                    print(f'Mapa de adjacencias: {neighborhood}')
                
                else :
                    two_neighbors_indices = self.find_indices(neighborhood, 2)
                    one_neighbor_indices = self.find_indices(neighborhood, 1)

                    while (two_neighbors_indices) :
                        idx = random.choice(two_neighbors_indices)
                        two_neighbors_indices.remove(idx)
                        if (not facility[idx]) :
                            facility[idx] = 1
                            index_list.remove(idx)
                            neighborhood[idx-1] -= 1
                            neighborhood[idx+1] -= 1

                            print(f'Indice escolhido: {idx}')
                            print(f'Instalacao: {facility}')
                            print(f'Mapa de adjacencias: {neighborhood}')
                            break

                    else :
                        while (one_neighbor_indices) :
                            idx = random.choice(one_neighbor_indices)
                            one_neighbor_indices.remove(idx)
                            if (not facility[idx]) :
                                facility[idx] = 1
                                index_list.remove(idx)
                                neighborhood[idx-1] -= 1
                                neighborhood[idx+1] -= 1

                                print(f'Indice escolhido: {idx}')
                                print(f'Instalacao: {facility}')
                                print(f'Mapa de adjacencias: {neighborhood}')
                                break

                        else :
                            idx = random.choice(index_list)
                            if (not facility[idx]) :
                                    facility[idx] = 1
                                    index_list.remove(idx)
                                    neighborhood[idx-1] -= 1
                                    neighborhood[idx+1] -= 1

                                    print(f'Indice escolhido: {idx}')
                                    print(f'Instalacao: {facility}')
                                    print(f'Mapa de adjacencias: {neighborhood}')

            users -= 1
            steps += 1

            discomfort = self.helper.count_discomfort(facility)
            disc_list.append(discomfort)

            print(f'Coef. incomodo global: {discomfort}')

        print()
        return steps, discomfort, disc_list

def main() :
    ap = Approaches()
    ap.completely_random(5)
    ap.individualist(5)
    ap.altruistic(5)
    ap.individualist_altruistic(5)
    ap.cleaner(5)
    ap.discomfort_minimization(5, 3)

main()
