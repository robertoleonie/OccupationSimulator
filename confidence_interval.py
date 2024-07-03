import matplotlib.pyplot as plt

class ConfidenceInterval() :
    def __init__(self) :
        pass

    def custom_boxplot_68(self, means, std_devs, labels):
        num_groups = len(means)

        plt.figure(figsize=(10, 6))

        for i in range(num_groups):
            # Definindo os limites do intervalo de confiança de 68%
            lower_bound = means[i] - 1 * std_devs[i]
            upper_bound = means[i] + 1 * std_devs[i]

            # Desenhando o retângulo do intervalo de confiança
            rect = plt.Rectangle((i+0.8, lower_bound), 0.4, upper_bound-lower_bound, fill=True, color='blue', alpha=0.3)
            plt.gca().add_patch(rect)

            # Adicionando a linha da média
            plt.plot([i+0.8, i+1.2], [means[i], means[i]], color='red', linewidth=2)

            # Adicionando as linhas dos extremos do intervalo de confiança
            plt.plot([i+0.8, i+0.8], [means[i]-1*std_devs[i], means[i]+1*std_devs[i]], color='black')
            plt.plot([i+1.2, i+1.2], [means[i]-1*std_devs[i], means[i]+1*std_devs[i]], color='black')

        # Configurações do gráfico
        plt.xticks(range(1, num_groups + 1), labels)
        plt.xlabel('Grupos')
        plt.ylabel('Valores')
        plt.title('Intervalos de Confiança de 68%')
        plt.legend(['IC', 'Média'], loc='lower right')
        plt.grid(True)
        plt.show()

    def custom_boxplot_95(self, means, std_devs, n_inputs):
        num_groups = len(means)

        plt.figure(figsize=(10, 6))

        for i in range(num_groups):
            lower_bound = means[i] - 2*std_devs[i]
            upper_bound = means[i] + 2*std_devs[i]

            rect = plt.Rectangle((i+0.8, lower_bound), 0.4, upper_bound-lower_bound, fill=True, color='blue', alpha=0.3)
            plt.gca().add_patch(rect)

            plt.plot([i+0.8, i+1.2], [means[i], means[i]], color='red', linewidth=2)
            plt.plot([i+0.8, i+0.8], [means[i]-std_devs[i], means[i]+std_devs[i]], color='black')
            plt.plot([i+1.2, i+1.2], [means[i]-std_devs[i], means[i]+std_devs[i]], color='black')

        plt.xticks(range(1, num_groups + 1), [f'{n}' for n in n_inputs])
        plt.xlabel('Capacidades n de instalação')
        plt.ylabel('Médias')
        plt.title('Intervalos de confiança de 95%')
        plt.legend(['IC', 'Média'], loc='lower right')
        plt.grid(True)
        plt.show()

    def custom_boxplot_99(self, means, std_devs, n_inputs):
        num_groups = len(means)

        plt.figure(figsize=(10, 6))

        for i in range(num_groups):
            lower_bound = means[i] - 3*std_devs[i]
            upper_bound = means[i] + 3*std_devs[i]

            rect = plt.Rectangle((i+0.8, lower_bound), 0.4, upper_bound-lower_bound, fill=True, color='blue', alpha=0.3)
            plt.gca().add_patch(rect)

            plt.plot([i+0.8, i+1.2], [means[i], means[i]], color='red', linewidth=2)
            plt.plot([i+0.8, i+0.8], [means[i]-std_devs[i], means[i]+std_devs[i]], color='black')
            plt.plot([i+1.2, i+1.2], [means[i]-std_devs[i], means[i]+std_devs[i]], color='black')

        plt.xticks(range(1, num_groups + 1), [f'{n}' for n in n_inputs])
        plt.xlabel('Capacidades n de instalação')
        plt.ylabel('Médias')
        plt.title('Intervalos de confiança de 99%')
        plt.legend(['IC', 'Média'], loc='lower right')
        plt.grid(True)
        plt.show()

def main() :
    means       = [1, 1, 1.668, 2.483, 4.626, 8.934, 13.291, 21.899, 43.491, 86.764, 130.125, 216.422, 432.485]
    std_devs    = [0, 0, 0.481, 0.499, 0.482, 0.633, 0.793, 0.99, 1.413, 1.891, 2.248, 3.121, 4.245]
    n_inputs    = [1, 2, 3, 5, 10, 20, 30, 50, 100, 200, 300, 500, 1000]

    ci = ConfidenceInterval()
    ci.custom_boxplot_68(means, std_devs, n_inputs)
    ci.custom_boxplot_95(means, std_devs, n_inputs)
    ci.custom_boxplot_99(means, std_devs, n_inputs)

main()
