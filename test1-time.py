import timeit
from utility import Search,BuildGraph;
from matplotlib import pyplot as plt

def main():        
    search =Search()
    graph = BuildGraph('romania4x.txt').giveMeGraph()
    nodes = graph.nodes()
   
    def breadth_search():
        for fnode in nodes :
            for lnode in nodes :
                if fnode != lnode :
                    search.breadth_first_search(fnode,lnode)
    def depth_search():
        for fnode in nodes :
            for lnode in nodes :
                if fnode != lnode :
                    search.depth_first_search(fnode,lnode)
    
    def dijkstra():
        for fnode in nodes :
            for lnode in nodes :
                if fnode != lnode :
                    search.dijkstra_search(fnode,lnode)
    def a_star():
        for fnode in nodes :
            for lnode in nodes :
                if fnode != lnode :
                    search.a_star_search(fnode,lnode)
    
    breadth_time = timeit.timeit(stmt = breadth_search,number = 100)/100
    depth_time = timeit.timeit(stmt = depth_search,number = 100)/100
    dijkstra_time =timeit.timeit(stmt = dijkstra,number = 100)/100
    a_star_time = timeit.timeit(stmt = a_star,number = 100)/100
    search_type = ["BFS","DFS","DIJKSTRA","A *STAR"]
    average_time = [breadth_time,depth_time,dijkstra_time,a_star_time]
     
    # print the data  
    print("Breadth Elapsed Time: ",breadth_time)
    print("Depth Elapsed Time: ",depth_time)
    print("Dijkstra Elapsed Time: ",dijkstra_time)
    print("A Star Elapsed Time: ",a_star_time)

    #plot the bar and display
    plt.bar(search_type,average_time, color ='maroon',)
    
    plt.xlabel("Search Type")
    plt.ylabel("Avarage Time Elapsed")
    plt.title("Search Type and Time Elapsed relashinshep")
    plt.show()
    

main()

    


    
    




