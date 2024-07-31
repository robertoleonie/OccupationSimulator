import matplotlib.pyplot as plt
import pandas as pd

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
    df = pd.read_csv('all_metrics.csv', encoding='latin-1')
    df = df[df['Abordagem'] == 'individualista']
    df.reset_index(drop=True, inplace=True)

    means       = df['Tempo Médio']
    std_devs    = df['Desvio padrão do tempo']
    n_inputs    = df['Posições']

    ci = ConfidenceInterval()
    ci.custom_boxplot_68(means, std_devs, n_inputs)
    ci.custom_boxplot_95(means, std_devs, n_inputs)
    ci.custom_boxplot_99(means, std_devs, n_inputs)

main()