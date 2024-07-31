from statistics import mean, variance
import matplotlib.pyplot as plt
import pandas as pd
import approaches

class Benchmarking():
    def __init__(self):
        self.apps = approaches.Approaches()

    def completely_random_metrics(self, positions, rounds=1000):
        self._round_steps_random = []
        self._round_disc_random = []

        for _ in range(rounds):
            steps, disc = self.apps.completely_random(positions)
            self._round_steps_random.append(steps)
            self._round_disc_random.append(disc)
        
        sample_mean_steps = mean(self._round_steps_random)
        sample_var_steps = variance(self._round_steps_random)
        sample_sd_steps = sample_var_steps ** (1/2)

        sample_mean_disc = mean(self._round_disc_random)
        sample_var_disc = variance(self._round_disc_random)
        sample_sd_disc = sample_var_disc ** (1/2)

        return sample_mean_steps, sample_sd_steps, sample_mean_disc, sample_sd_disc
    
    def individualist_metrics(self, positions, rounds=1000):
        self._round_steps_individualist = []
        self._round_disc_individualist = []

        for _ in range(rounds):
            steps, disc = self.apps.individualist(positions)
            self._round_steps_individualist.append(steps)
            self._round_disc_individualist.append(disc)
        
        sample_mean_steps = mean(self._round_steps_individualist)
        sample_var_steps = variance(self._round_steps_individualist)
        sample_sd_steps = sample_var_steps ** (1/2)

        sample_mean_disc = mean(self._round_disc_individualist)
        sample_var_disc = variance(self._round_disc_individualist)
        sample_sd_disc = sample_var_disc ** (1/2)

        return sample_mean_steps, sample_sd_steps, sample_mean_disc, sample_sd_disc

    def altruistic_metrics(self, positions, rounds=1000):
        self._round_steps_altruistic = []
        self._round_disc_altruistic = []

        for _ in range(rounds):
            steps, disc = self.apps.altruistic(positions)
            self._round_steps_altruistic.append(steps)
            self._round_disc_altruistic.append(disc)
        
        sample_mean_steps = mean(self._round_steps_altruistic)
        sample_var_steps = variance(self._round_steps_altruistic)
        sample_sd_steps = sample_var_steps ** (1/2)

        sample_mean_disc = mean(self._round_disc_altruistic)
        sample_var_disc = variance(self._round_disc_altruistic)
        sample_sd_disc = sample_var_disc ** (1/2)

        return sample_mean_steps, sample_sd_steps, sample_mean_disc, sample_sd_disc

    def individualist_altruistic_metrics(self, positions, rounds=1000):
        self._round_steps_individualist_altruistic = []
        self._round_disc_individualist_altruistic = []

        for _ in range(rounds):
            steps, disc = self.apps.individualist_altruistic(positions)
            self._round_steps_individualist_altruistic.append(steps)
            self._round_disc_individualist_altruistic.append(disc)
        
        sample_mean_steps = mean(self._round_steps_individualist_altruistic)
        sample_var_steps = variance(self._round_steps_individualist_altruistic)
        sample_sd_steps = sample_var_steps ** (1/2)

        sample_mean_disc = mean(self._round_disc_individualist_altruistic)
        sample_var_disc = variance(self._round_disc_individualist_altruistic)
        sample_sd_disc = sample_var_disc ** (1/2)

        return sample_mean_steps, sample_sd_steps, sample_mean_disc, sample_sd_disc
    
    def cleaner_metrics(self, positions, rounds=1000):
        self._round_steps_cleaner = []
        self._round_disc_cleaner = []

        for _ in range(rounds):
            steps, disc = self.apps.cleaner(positions)
            self._round_steps_cleaner.append(steps)
            self._round_disc_cleaner.append(disc)
        
        sample_mean_steps = mean(self._round_steps_cleaner)
        sample_var_steps = variance(self._round_steps_cleaner)
        sample_sd_steps = sample_var_steps ** (1/2)

        sample_mean_disc = mean(self._round_disc_cleaner)
        sample_var_disc = variance(self._round_disc_cleaner)
        sample_sd_disc = sample_var_disc ** (1/2)

        return sample_mean_steps, sample_sd_steps, sample_mean_disc, sample_sd_disc
    
    def discomfort_optimization_metrics(self, positions, rounds=1000):
        self._round_steps_d_opt = []
        self._round_disc_d_opt = []

        for _ in range(rounds):
            steps, disc = self.apps.discomfort_optimization(positions, users=positions//2)
            self._round_steps_d_opt.append(steps)
            self._round_disc_d_opt.append(disc)
        
        sample_mean_steps = mean(self._round_steps_d_opt)
        sample_var_steps = variance(self._round_steps_d_opt)
        sample_sd_steps = sample_var_steps ** (1/2)

        sample_mean_disc = mean(self._round_disc_d_opt)
        sample_var_disc = variance(self._round_disc_d_opt)
        sample_sd_disc = sample_var_disc ** (1/2)

        return sample_mean_steps, sample_sd_steps, sample_mean_disc, sample_sd_disc

class Simulation():
    def __init__(self):
        self._benchmarking = Benchmarking()
        self.app = ['completamente aleatória', 'individualista', 'altruística', \
                    'individualista-altruística', 'faxineiro', 'otimização do incômodo']

    def all_steps_means(self, positions):
        completely_random_sample_mean = self._benchmarking.completely_random_metrics(positions)[0]
        individualist_sample_mean = self._benchmarking.individualist_metrics(positions)[0]
        altruistic_sample_mean = self._benchmarking.altruistic_metrics(positions)[0]
        ind_alt_sample_mean = self._benchmarking.individualist_altruistic_metrics(positions)[0]
        cleaner_sample_mean = self._benchmarking.cleaner_metrics(positions)[0]
        discomfort_optimization_sample_mean = self._benchmarking.discomfort_optimization_metrics(positions)[0]

        return completely_random_sample_mean, individualist_sample_mean, altruistic_sample_mean, \
            ind_alt_sample_mean, cleaner_sample_mean, discomfort_optimization_sample_mean

    '''
    def all_variances(self, positions):
        completely_random_sample_var = self._benchmarking.completely_random_metrics(positions)[1]
        individualist_sample_var = self._benchmarking.individualist_metrics(positions)[1]
        altruistic_sample_var = self._benchmarking.altruistic_metrics(positions)[1]
        cleaner_sample_var = self._benchmarking.cleaner_metrics(positions)[1]
        discomfort_optimization_sample_var = self._benchmarking.discomfort_optimization_metrics(positions)[1]

        return completely_random_sample_var, individualist_sample_var, altruistic_sample_var, \
            cleaner_sample_var, discomfort_optimization_sample_var
    '''

    def all_steps_std_devs(self, positions):
        completely_random_sample_sd = self._benchmarking.completely_random_metrics(positions)[1]
        individualist_sample_sd = self._benchmarking.individualist_metrics(positions)[1]
        altruistic_sample_sd = self._benchmarking.altruistic_metrics(positions)[1]
        ind_alt_sample_sd = self._benchmarking.individualist_altruistic_metrics(positions)[1]
        cleaner_sample_sd = self._benchmarking.cleaner_metrics(positions)[1]
        discomfort_optimization_sample_sd = self._benchmarking.discomfort_optimization_metrics(positions)[1]

        return completely_random_sample_sd, individualist_sample_sd, altruistic_sample_sd, \
            ind_alt_sample_sd, cleaner_sample_sd, discomfort_optimization_sample_sd
    
    def all_discomfort_means(self, positions):
        completely_random_sample_mean = self._benchmarking.completely_random_metrics(positions)[2]
        individualist_sample_mean = self._benchmarking.individualist_metrics(positions)[2]
        altruistic_sample_mean = self._benchmarking.altruistic_metrics(positions)[2]
        ind_alt_sample_mean = self._benchmarking.individualist_altruistic_metrics(positions)[2]
        cleaner_sample_mean = self._benchmarking.cleaner_metrics(positions)[2]
        discomfort_optimization_sample_mean = self._benchmarking.discomfort_optimization_metrics(positions)[2]

        return completely_random_sample_mean, individualist_sample_mean, altruistic_sample_mean, \
            ind_alt_sample_mean, cleaner_sample_mean, discomfort_optimization_sample_mean

    def all_discomfort_std_devs(self, positions):
        completely_random_sample_sd = self._benchmarking.completely_random_metrics(positions)[3]
        individualist_sample_sd = self._benchmarking.individualist_metrics(positions)[3]
        altruistic_sample_sd = self._benchmarking.altruistic_metrics(positions)[3]
        ind_alt_sample_sd = self._benchmarking.individualist_altruistic_metrics(positions)[3]
        cleaner_sample_sd = self._benchmarking.cleaner_metrics(positions)[3]
        discomfort_optimization_sample_sd = self._benchmarking.discomfort_optimization_metrics(positions)[3]

        return completely_random_sample_sd, individualist_sample_sd, altruistic_sample_sd, \
            ind_alt_sample_sd, cleaner_sample_sd, discomfort_optimization_sample_sd

    def all_metrics(self, n_inputs):
        self.cols = ['Posições', 'Abordagem', 'Tempo Médio', 'Desvio padrão do tempo', 'Incômodo Médio', 'Desvio do Incômodo']
        df = pd.DataFrame(columns=self.cols)

        for n in n_inputs:
            for ap in range(6):
                new_line = {self.cols[0]: n, 
                            self.cols[1]: self.app[ap], 
                            self.cols[2]: round(self.all_steps_means(n)[ap], 3),
                            self.cols[3]: round(self.all_steps_std_devs(n)[ap], 3), 
                            self.cols[4]: round(self.all_discomfort_means(n)[ap], 3),
                            self.cols[5]: round(self.all_discomfort_std_devs(n)[ap], 3)}
                print(new_line)
                df.loc[len(df)] = new_line

        df.to_csv('all_metrics.csv', sep=',', index=False, encoding='latin-1')

        return df

class Plot():
    def __init__(self, n_inputs):
        self.n_inputs = n_inputs
        self.sim = Simulation()

        # self.df = self.sim.all_metrics(self.n_inputs)
        import pandas as pd
        self.df = pd.read_csv('all_metrics.csv', encoding='latin-1')
        self.n_inputs = n_inputs

        self._apps = {i: self.sim.app[i] for i in range(6)}
        self._structures = {self.sim.app[i]: f"x{i}" for i in range(6)}

    '''
    def generate_paired_data(self, first_approach:str, second_approach:str):
        first_structure = self._structures[first_approach]
        second_structure = self._structures[second_approach]

        if first_structure == second_structure:
            raise ValueError("Impossível comparar uma mesma abordagem duas vezes.")

        self.first_data = getattr(self, first_structure, None)
        self.second_data = getattr(self, second_structure, None)

    def draw_paired_graphics(self, first_data:str, second_data:str):
        self.generate_paired_data(first_data, second_data)

        plt.figure(figsize=(10, 6))

        plt.plot(self.n_inputs, self.first_data, label=first_data, alpha=0.7)
        plt.plot(self.n_inputs, self.second_data, label=second_data, alpha=0.7)

        plt.xlabel("Entrada n de capacidade da instalação")
        plt.ylabel("Tempo médio de execução")
        plt.title(f"Gráfico comparativo das abordagens {first_data} e {second_data}")
        plt.legend()
        plt.grid(True)
        plt.show()
    '''
       
    def draw_all_steps_line_graphics(self):
        print(self.df.head())
        plt.figure(figsize=(10, 6))

        for app in self._apps.values() :
            filter = self.df['Abordagem'] == app
            x_values = self.df.loc[filter, 'Posições']
            y_values = self.df.loc[filter, 'Tempo Médio']

            plt.plot(x_values, y_values, label=app, alpha=0.7)

        plt.xlabel("Entrada n de capacidade da instalação")
        plt.ylabel("Número médio de passos")
        plt.title("Gráfico comparativo para todas as abordagens")
        plt.legend()
        plt.grid(True)
        plt.show()

    def draw_all_disc_line_graphics(self):
        plt.figure(figsize=(10, 6))

        for app in self._apps.values() :
            filter = self.df['Abordagem'] == app
            x_values = self.df.loc[filter, 'Posições']
            y_values = self.df.loc[filter, 'Incômodo Médio']

            plt.plot(x_values, y_values, label=app, alpha=0.7)

        plt.xlabel("Entrada n de capacidade da instalação")
        plt.ylabel("Incômodo médio ao fim das 1000 rodadas")
        plt.title("Comparação dos incômodos das abordagens")
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    n_inputs = [1, 2, 3, 5, 10, 20, 30, 50, 100, 200, 300, 500, 1000]

    plot = Plot(n_inputs)
    plot.draw_all_steps_line_graphics()
    plot.draw_all_disc_line_graphics()

    '''
    plot.draw_paired_graphics('completamente aleatória', 'individualista')
    plot.draw_paired_graphics('completamente aleatória', 'individualista-altruística')
    plot.draw_paired_graphics('completamente aleatória', 'altruística')
    plot.draw_paired_graphics('completamente aleatória', 'faxineiro')
    plot.draw_paired_graphics('completamente aleatória', 'otimização do incômodo')
    '''

main()
