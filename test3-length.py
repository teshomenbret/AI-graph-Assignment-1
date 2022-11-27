from utility import Search,BuildGraph;
from matplotlib import pyplot as plt

def main():        
    search =Search()
    graph = BuildGraph('romania4x.txt').giveMeGraph()
    nodes = graph.nodes()

    def breadth_search():
        length = 0
        for fnode in nodes :
            for lnode in nodes :
                if fnode != lnode :
                    length += len(search.breadth_first_search(fnode,lnode))
        return length
                    
    def depth_search():
        length = 0
        for fnode in nodes :
            for lnode in nodes :
                if fnode != lnode :
                    length += len(search.depth_first_search(fnode,lnode))
        return length
    
    def dijkstra():
        length = 0
        for fnode in nodes :
            for lnode in nodes :
                if fnode != lnode :
                    length += len(search.dijkstra_search(fnode,lnode))
        return length

    def a_star():
        length = 0
        for fnode in nodes :
            for lnode in nodes :
                if fnode != lnode :
                    length += len(search.a_star_search(fnode,lnode))
        return length
    
    breadth_length =  breadth_search()/380
    depth_length =  depth_search()/380
    dijkstra_length = dijkstra()/380
    a_star_length =  a_star()/380
    search_type = ["BFS","DFS","DIJKSTRA","A *STAR"]
    average_length = [breadth_length,depth_length,dijkstra_length,a_star_length]

    # print the data  
    print("Breadth Length: ",breadth_length)
    print("Depth Length: ",depth_length)
    print("Dijkstra Length: ",dijkstra_length)
    print("A Star Length: ",a_star_length)
    
    #plot the bar and display
    plt.bar(search_type,average_length, color ='maroon',)
    plt.xlabel("Search Type")
    plt.ylabel("Average length Generated")
    plt.title("Search Type and length Generated relashinshep")
    plt.show()


main()

    


    
    




