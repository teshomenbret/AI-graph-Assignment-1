from utility import Search,BuildGraph;
from matplotlib import pyplot as plt

def main():        
    search =Search()
    graph = BuildGraph('romania.txt').giveMeGraph()
    nodes = graph.nodes()     

# dgree centralities 
    node_name = []
    num_degree = []
    for node in nodes:
        num_degree.append(len(node.incident_edges()))
        node_name.append(node.data()) 
        print(node.data(),"  ",len(node.incident_edges()))  

    #plot the bar and display
    plt.bar(node_name,num_degree, color ='maroon',)
    plt.xlabel("Name")
    plt.ylabel("Dgree")
    plt.title("Dgree Centeralites")
    plt.show()

   

main()

    


    
    




