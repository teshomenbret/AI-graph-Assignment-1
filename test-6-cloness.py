from utility import Search,BuildGraph;
from matplotlib import pyplot as plt

def main():        
    search =Search()
    graph = BuildGraph('romania.txt').giveMeGraph()
    nodes = graph.nodes()
    dijkstra_node_total_distance={}
    a_star_node_total_distance={} 
    dijkstra_length = []
    a_star_length=[]
    dijkstra_name = []
    a_star_name =[]


# closness centralities 

    # by Dijkstra Search
    for start_node in nodes:
        for target in nodes:
            dijkstra_node_total_distance[start_node.data()] =0
            if start_node != target:
                dijkstra_distance = search.dijkstra_search(start_node, target)
                dijkstra_node_total_distance[start_node.data()] = dijkstra_node_total_distance[start_node.data()]+dijkstra_distance

 
    for node_name, length in dijkstra_node_total_distance.items():
        dijkstra_name.append(node_name)
        dijkstra_length.append(length/20)
        print(node_name,"  ",length/20 )

    #plot the bar and display
    plt.bar(dijkstra_name,dijkstra_length, color ='maroon',)
    plt.xlabel("Name")
    plt.ylabel("Dgree")
    plt.title("Dgree Centeralites")
    plt.show()



    # for node in nodes:
    #     dijkstra_betweenness[node.data()] = 0
    #     for path in all_pathes_dijkstra:
    #         if node.data() in path:
    #             dijkstra_betweenness[node.data()] = dijkstra_betweenness[node.data()]+1 
    # print()
    # for node, center in dijkstra_betweenness.items():
    #     print(node, center/len(all_pathes_dijkstra))

    # by A Star Search
    # for start_node in nodes:
    #     for target in nodes:
    #         if start_node != target:
    #             a_star_distance = search.dijkstra_search(start_node, target)
    #             a_star_node_total_distance[start_node.data()] =a_star_distance

    # a_star_betweenness ={}
    # for node in nodes:
    #     a_star_betweenness[node.data()] = 0
    #     for path in all_pathes_a_star:
    #         if node.data() in path:
    #             a_star_betweenness[node.data()] = a_star_betweenness[node.data()]+1 
    # print()            
    # for node, center in a_star_betweenness.items():
    #     print(node, center/len(all_pathes_a_star))

    
        



main()

    


    
    




