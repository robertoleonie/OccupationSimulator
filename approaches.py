import random

class Approaches() :
    def __init__(self) :
        pass

    def find_indices(self, input_list, element):
            return [i for i, x in enumerate(input_list) if x == element]
    
    def find_sublist_start_index(self, subset, arr):
        size = len(subset)
        
        for i in range(len(arr) - size + 1):
            if arr[i:i + size] == subset:
                return i
        
        return -1

    def completely_random(self, n) :
        facility = [0] * n
        index_list = [i for i in range(0,n)]
        steps = 0

        while (index_list) :
            idx = random.choice(index_list)
            facility[idx] = 1
            index_list.remove(idx)

            steps += 1

        return steps

    def individualist(self, n) :
        facility = [0] * n
        index_list = [i for i in range(0,n)]
        steps = 0

        while (index_list) :
            idx = random.choice(index_list)
            facility[idx] = 1
            index_list.remove(idx)

            if idx > 0 and idx-1 in index_list :
                index_list.remove(idx-1)
            if idx < n-1 and idx+1 in index_list :
                index_list.remove(idx+1)

            steps += 1

        return steps

    def altruistic(self, n) :
        facility = [0] * n
        index_list = []
        steps = 0

        if (n % 2 == 0) :
            coin = random.randint(0,1)
            index_list = [i for i in range(coin,n,2)]
        else :
            index_list = [i for i in range(0,n,2)]

        while (index_list) :
            idx = random.choice(index_list)
            facility[idx] = 1
            index_list.remove(idx)

            steps += 1

        return steps

    def individualist_altruistic(self, n) :
        facility = [0] * n
        index_list = [i for i in range(0,n)]
        steps = 0

        coin = random.randint(0,1)
        if (coin) :
            seq = [n-1, 0]
        else :
            seq = [0, n-1]

        while (seq) :
            idx = seq.pop(0)
            facility[idx] = 1
            if idx == 0:
                facility[idx + 1] = 'X'
            else:
                facility[idx - 1] = 'X'
            index_list.remove(idx)
            steps += 1

            print(idx, '\n', facility, '\n', index_list, '\n', steps, '\n')

        while (index_list) :
            if (self.find_sublist_start_index([0], facility) != -1) :
                pos = self.find_sublist_start_index(['X', 'X'], facility)
                print(pos)
                coin = random.randint(0,1)
                print(coin)
                if (pos == -1) :    
                    if (coin) :
                        pos = self.find_sublist_start_index([0, 0, 'X'], facility)
                        print(pos)
                        if (pos != -1) :
                            idx = pos+1
                            facility[idx] = 1
                            facility[idx-1] = 'X'
                            index_list.remove(idx)

                            print(idx, '\n', facility, '\n', index_list, '\n', steps, '\n')

                    else :
                        pos = self.find_sublist_start_index(['X', 0, 0], facility)
                        print(pos)
                        if (pos != -1) :
                            idx = pos+1
                            facility[idx] = 1
                            facility[idx+1] = 'X'
                            index_list.remove(idx)

                            print(idx, '\n', facility, '\n', index_list, '\n', steps, '\n')

                else :
                    idx = pos + coin
                    facility[idx] = 1
                    index_list.remove(idx)

                    print(idx, '\n', facility, '\n', index_list, '\n', steps, '\n')

            else :
                idx = random.choice(index_list)
                facility[idx] = 1
                index_list.remove(idx)

                print(idx, '\n', facility, '\n', index_list, '\n', steps, '\n')

            steps += 1

        return steps

    def cleaner(self, n) :
        facility = [0] * n
        index_list = []
        steps = 0

        if (n % 2 == 0) :
            coin = random.randint(0,1)
            index_list = [i for i in range(coin,n,2)]
        else :
            index_list = [i for i in range(1,n,2)]

        while (index_list) :
            idx = random.choice(index_list)
            facility[idx] = 1
            index_list.remove(idx)

            steps += 1

        return steps

    def discomfort_optimization(self, n, users) :
        if (users > n) :
            raise ValueError("Erro: número de usuários maior do que a capacidade da instalação!\n")

        facility = [0] * n
        index_list = [i for i in range(0,n)]
        neighborhood = [1] + [2] * (n-2) + [1]
        steps = 0

        while (users) :
            coin = random.randint(0,1)

            if (coin == 0) :
                # testa se o recurso mais à esquerda está disponível
                if (not facility[0]) :
                    facility[0] = 1
                    index_list.remove(0)
                    neighborhood[1] -= 1
                    
                elif (not facility[n-1]) :
                    facility[n-1] = 1
                    index_list.remove(n-1)
                    neighborhood[n-2] -= 1
                
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
                                break

                        else :
                            idx = random.choice(index_list)
                            if (not facility[idx]) :
                                facility[idx] = 1
                                index_list.remove(idx)
                                neighborhood[idx-1] -= 1
                                neighborhood[idx+1] -= 1

            else :
                # testa se o recurso mais à direita está disponível    
                if (not facility[n-1]) :
                    facility[n-1] = 1
                    index_list.remove(n-1)
                    neighborhood[n-2] -= 1
                
                elif (not facility[0]) :
                    facility[0] = 1
                    index_list.remove(0)
                    neighborhood[1] -= 1
                
                else :
                    two_neighbors_indices = find_indices(neighborhood, 2)
                    one_neighbor_indices = find_indices(neighborhood, 1)

                    while (two_neighbors_indices) :
                        idx = random.choice(two_neighbors_indices)
                        two_neighbors_indices.remove(idx)
                        if (not facility[idx]) :
                            facility[idx] = 1
                            index_list.remove(idx)
                            neighborhood[idx-1] -= 1
                            neighborhood[idx+1] -= 1
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
                                break

                        else :
                            idx = random.choice(index_list)
                            if (not facility[idx]) :
                                    facility[idx] = 1
                                    index_list.remove(idx)
                                    neighborhood[idx-1] -= 1
                                    neighborhood[idx+1] -= 1

            users -= 1
            steps += 1

        return steps
