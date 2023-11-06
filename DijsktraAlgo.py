from collections import defaultdict
from datetime import datetime
ct = datetime.now()

formatted_time = ct.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current Time: {formatted_time}")

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.traffic_level = defaultdict(list)


    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance, traffic_level, road_congestion):
        self.edges[fromNode].append([toNode, traffic_level, road_congestion])
        self.distances[(fromNode, toNode)] = distance 

def Dijkstra(graph, initial, target):
    visited = {initial: 0}
    visited_factors = {initial: 0}
    path = defaultdict(list) 
    traffic = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node  

        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        if minNode == target:
            break

        for edge in graph.edges[minNode]:
            road_factors = edge[1] + edge[2]
            weight = currentWeight + graph.distances[(minNode, edge[0])] 
            if edge[0] not in visited or weight < visited[edge[0]]:
                visited[edge[0]] = weight
                path[edge[0]] = [minNode, edge[1], edge[2]] 

    return visited, path

# Creating coordinates and network for start_node, target_node, distance, traffic congestion, road congestion
def CreateGraph():
    customGraph = Graph()
    customGraph.addNode("BFP")
    customGraph.addNode("TOTAL")
    customGraph.addNode("ALAWIHAO")
    customGraph.addNode("GREENVIEW")
    customGraph.addNode("SAMAKA")
    customGraph.addNode("IRAYA")
    customGraph.addNode("CAMAMBUGANP-1")
    customGraph.addNode("CAMAMBUGANP-2")
    customGraph.addNode("CAMAMBUGANP-3")
    customGraph.addNode("BIBIRAO")
    customGraph.addEdge("BFP", "TOTAL", 200, 1, 2)
    customGraph.addEdge("BFP", "GAHONON", 100, 3, 4)
    customGraph.addEdge("TOTAL", "ALAWIHAO", 900, 3, 2)
    customGraph.addEdge("TOTAL", "GREENVIEW", 400, 1, 2)
    customGraph.addEdge("GREENVIEW", "SAMAKA", 500, 1, 4)
    customGraph.addEdge("GREENVIEW", "IRAYA", 100, 3, 2)
    customGraph.addEdge("GREENVIEW", "CAMAMBUGANP-1", 200, 2, 4)
    customGraph.addEdge("CAMAMBUGANP-1", "CAMAMBUGANP-2", 300, 1, 2)
    customGraph.addEdge("CAMAMBUGANP-1", "CAMAMBUGANP-3", 100, 1, 2)
    customGraph.addEdge("CAMAMBUGANP-1", "BIBIRAO", 400, 1, 2) 

    
    '''customGraph = Graph()
    customGraph.addNode("A")
    customGraph.addNode("B")
    customGraph.addNode("C")
    customGraph.addNode("D")
    customGraph.addNode("E")
    customGraph.addNode("F")
    customGraph.addNode("G")
    customGraph.addNode("H")
    customGraph.addEdge("A", "B", 8, 1, 2)
    customGraph.addEdge("A", "C", 3, 2, 4)
    customGraph.addEdge("A", "E", 3, 2, 2)
    customGraph.addEdge("A", "D", 6, 3, 2)
    customGraph.addEdge("B", "D", 8, 3, 4)
    customGraph.addEdge("B", "F", 30, 1, 2)
    customGraph.addEdge("C", "D", 12, 2, 4)
    customGraph.addEdge("E", "F", 11, 1, 2)
    customGraph.addEdge("E", "H", 5, 1, 2)
    customGraph.addEdge("F", "H", 8, 1, 4)'''

    return customGraph

# Algorithm for getting the shortest path
def SearchShortestPath(startNode, targetNode, paths, distances): 
    shortestDistance = distances[targetNode] 
    shortestPath = [targetNode] 
    shortestTraffic = []
    roadLane = []

    while shortestPath[-1] != startNode: 
        recommended_path = paths[shortestPath[-1]][0]
        recommended_traffic = paths[shortestPath[-1]][1]
        recommended_roadlane = paths[shortestPath[-1]][2]
        shortestPath.append(recommended_path)
        shortestTraffic.append(recommended_traffic)
        roadLane.append(recommended_roadlane)
    
    shortestPath.reverse()
    shortestTraffic.reverse()

    starting_point = 0
    shortestTraffic.insert(0, starting_point)
    roadLane.insert(0, starting_point)


    return shortestDistance, shortestPath, shortestTraffic, roadLane


# Initialize all the data and get the shortest possible route
def GetShortestPath(Initial, Destination):
    start_node = Initial
    target_node = Destination

    # Create and get the Graph
    customGraph = CreateGraph()

    # Implement Dijkstra algorithm and get the distances and paths
    distances, paths = Dijkstra(customGraph, start_node, target_node) 

    # Get the shortest path only
    shortest_distance, shortest_path, shortest_traffic, roadLane = SearchShortestPath(start_node, target_node, paths, distances)

    print("-"*40)
    print("Starting Point:", Initial)
    print("Destination:", Destination)
    print("-"*40)
    print("Shortest Distance:", shortest_distance * 0.001, "km")
    print("Shortest Path:", shortest_path)
    print("-"*40)
    print("Expected Traffic:") 

    for i, (path, traffic) in enumerate(zip(shortest_path, shortest_traffic)):  
        trafficLevel = ""
        pathLabel = "" 

        if path == "A":
            pathLabel = "Fire Station"
        elif path == "B":
            pathLabel = "SM City"
        elif path == "C":
            pathLabel = "Mantagbac Road"
        elif path == "D":
            pathLabel = "Vinzons Ave."
        elif path == "E":
            pathLabel = "Total Road"
        elif path == "F":
            pathLabel = "Japan Surplus"
        elif path == "H":
            pathLabel = "Pabico Elem School"

        if traffic == 0:
            trafficLevel = "[You're Here]"
        elif traffic == 1:
            trafficLevel = "Minimal traffic"
        elif traffic == 2:
            trafficLevel = "Moderate traffic"
        elif traffic == 3:
            trafficLevel = "Heavy traffic"
            
        print(f'~> {path}: {trafficLevel} '  )
        
    print("-"*40)

    print("Road Condition")
    for i, (path, lane) in enumerate(zip(shortest_path, roadLane)):  
        trafficLevel = ""
        pathLabel = "" 

        '''if path == "A":
            pathLabel = "Fire Station"
        elif path == "B":
            pathLabel = "SM City"
        elif path == "C":
            pathLabel = "Mantagbac Road"
        elif path == "D":
            pathLabel = "Vinzons Ave."
        elif path == "E":
            pathLabel = "Total Road"
        elif path == "F":
            pathLabel = "Japan Surplus"
        elif path == "H":
            pathLabel = "Pabico Elem School"

        if lane == 0:
            print(f"~> {pathLabel}: [You're Here]"  )
        else:
            print(f"~> {pathLabel}: {lane}-way-road")'''
                
    print("-"*40)

    return shortest_path, shortest_distance

GetShortestPath("BFP", "BIBIRAO")