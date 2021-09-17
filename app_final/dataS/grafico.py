import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class grafico:

    def criarBarplotMatplot(self, data ):
        print('Cria grafico de barra!')
        colum = []
        for i in range(len(data[0][1])):
            colum.append("UAV "+str(i+1))

        X = np.arange(len(data[0][1]))
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlabel('xlabel')
        ax.set_ylabel('ylabel')
        ax.bar(X + 0.00, data[0][1], color='b', width=0.25, label='Inline label')
        ax.bar(X + 0.25, data[1][1], color='g', width=0.25, label='Inline label')
        #ax.bar(X + 0.50, data[2], color='r', width=0.25)
        plt.xticks(X, colum)
        plt.legend("q","n")
        plt.show()

    def convertArrayToDataframe(self, data):
        print("coverter array para formato data frame")
        # columns = ["UAV", "metodo"]
        row = []
        for z in range(len(data)):
            for i in range(len(data[0][1])):
                row.append([data[z][0], data[z][1][i], "UAV "+str(i+1)])
        df=pd.DataFrame(row,columns = ["metodo","energy","id_uav"])
        return df

    def criarBarplotSeaborn(self,data):
        print ("plot seaborn")
        df=self.convertArrayToDataframe(data)

        sns.set_theme(style="whitegrid")
        # Draw a nested barplot by species and sex
        g = sns.catplot(
            data=df, kind="bar",
            x="id_uav", y="energy", hue="metodo",
            ci="sd", palette="dark",
            alpha=.6, height=6, aspect=2
        )
        g.despine(left=True)

        g.set_axis_labels("", data[0][2])
        g.legend.set_title("")
        arqSave = data[0][2]
        arqSave = arqSave.replace('(m/s)','').replace('(j)','').replace('(m)','')
        plt.savefig('graficos/'+arqSave+'.pdf')

        plt.show()

    def criarLineplotSeaborn(self, data):
            print("plot seaborn")
            # df = self.convertArrayToDataframe(data)
            sns.set_theme(style="darkgrid")

            # dots = sns.load_dataset("dots")

            # Define the palette as a list to specify exact values
            # palette = sns.color_palette("rocket_r")

            # Plot the lines on two facets
            # size_order = ["T1", "T2"]
            sns.lineplot(
                data=data,
                x="distancia",
                y="energia",
                hue="vento"
            )

            plt.show()









