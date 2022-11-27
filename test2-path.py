from utility import Search,BuildGraph;

def main():        
    search =Search()
    graph = BuildGraph('romania4x.txt').giveMeGraph()
    nodes = graph.nodes()
    
    print()
    print("Breadth Path")
    print()
    for start_node in nodes:
        for target in nodes:
            path = search.breadth_first_search(start_node,target)
            print(path)
            
    print()
    print("Depth Path")
    print()
    for start_node in nodes:
        for target in nodes:
            path = search.depth_first_search(start_node,target)
            print(path)

    print()
    print("Dijkstra Path")
    print()
    for start_node in nodes:
        for target in nodes:
            path = search.dijkstra_search(start_node, target)
            print(path)

    print()
    print("A Star Path")
    print()
    for start_node in nodes:
        for target in nodes:
            path = search.a_star_search(start_node,target)
            print(path)
main()

    


    
    




