import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    prev = {vertex: None for vertex in graph}
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]: continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, prev


graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

start = 'A'
distances, prev = dijkstra(graph, start)

print("Odległości od wierzchołka startowego:")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")

print("\nPoprzednicy:")
for vertex, prev in prev.items():
    print(f"{vertex}: {prev}")