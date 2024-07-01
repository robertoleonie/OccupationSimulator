import random

class Approaches() :
    def __init__(self) :
        pass

    def completely_random(n) :
        facility = [0] * n
        index_list = [i for i in range(0,n)]
        steps = 0

        while (index_list) :
            idx = random.choice(index_list)
            facility[idx] = 1
            index_list.remove(idx)

            steps += 1

        return steps

    def individualist(n) :
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

    def altruistic(n) :
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

    def cleaner(n) :
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

    def discomfort_optimization(n, users) :
        def find_indices(input_list, element):
            return [i for i, x in enumerate(input_list) if x == element]

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
