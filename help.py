class Helper() :
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
    
    def count_discomfort(self, arr):
        discomfort = 0
        n = len(arr)

        if (n > 1) :
            for i in range(n) :
                if (arr[i] == 1) :
                    if (i < n-1) :
                        if (arr[i+1] != 'X') :
                            discomfort += arr[i+1]
                    if (i > 0) :
                        if (arr[i-1] != 'X') :
                            discomfort += arr[i-1]

        return discomfort