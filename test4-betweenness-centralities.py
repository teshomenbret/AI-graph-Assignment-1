from utility import Search,BuildGraph;
from matplotlib import pyplot as plt

def main():        
    search =Search()
    graph = BuildGraph('romania.txt').giveMeGraph()
    nodes = graph.nodes()
    all_pathes_dijkstra=[]
    all_pathes_a_star=[]
    dijkstra_node_name =[]
    dijkstra_center = []

    for start_node in nodes:
        for target in nodes:
            if start_node != target:
                dijkstra_path = search.dijkstra_search(start_node, target)
                a_star_path = search.a_star_search(start_node,target)
                all_pathes_dijkstra.append(dijkstra_path)
                all_pathes_a_star.append(a_star_path)
            

# Betweenness centralities 

    # by Dijkstra Search
    print("\n Betweenness centralities By Dijkstra Search \n")
    dijkstra_betweenness ={}
    for node in nodes:
        dijkstra_betweenness[node.data()] = 0
        for path in all_pathes_dijkstra:
            if node.data() in path:
                dijkstra_betweenness[node.data()] = dijkstra_betweenness[node.data()]+1 
    print()
    for node, center in dijkstra_betweenness.items():
        dijkstra_node_name.append(node)
        dijkstra_center.append(center)
        print(node, center/len(all_pathes_dijkstra))

    # by A Star Search
    print("\n Betweenness centralities By Star Search \n")
    a_star_betweenness ={}
    for node in nodes:
        a_star_betweenness[node.data()] = 0
        for path in all_pathes_a_star:
            if node.data() in path:
                a_star_betweenness[node.data()] = a_star_betweenness[node.data()]+1 
    print()            
    for node, center in a_star_betweenness.items():
        print(node, center/len(all_pathes_a_star))

    #plot the bar and display
    plt.bar(dijkstra_node_name,dijkstra_center, color ='maroon',)
    plt.xlabel("Name")
    plt.ylabel("Betwenness")
    plt.title("Betwenness Centeralites")
    plt.show()

main()

    


    
    




