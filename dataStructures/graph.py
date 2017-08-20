import sys
import pprint
from collections import defaultdict

class Graph(object):
    """ Graph class using a dictionary of lists, undirected by default """

    def __init__(self, edges=None, directed=False):
        self.graphDict = defaultdict(list)
        self.directed = directed
        self.addEdges(edges)

    def addEdges(self, edges):
        """ Add every edge listed on edges """
        if edges:
            for vertex1, vertex2 in edges:
                self.add(vertex1, vertex2)

    def add(self, vertex1, vertex2):
        """ Add edge between vertex1 and vertex2 """
        self.__addFromOriginToDestination(vertex1, vertex2)
        if not self.directed:
            self.__addFromOriginToDestination(vertex2, vertex1)

    def __addFromOriginToDestination(self, vertex1, vertex2):
        """ Add edge from vertex1 and vertex2 """
        if vertex1 in self.graphDict:
            self.graphDict[vertex1].append(vertex2)
        else:
            self.graphDict[vertex1] = list(vertex2)

    def removeVertex(self, vertex):
        """ Remove the given vertex from graph """
        for _, connectionTo in self.graphDict.items():
            try:
                connectionTo.remove(vertex)
            except ValueError:
                pass
        try:
            del self.graphDict[vertex]
        except KeyError:
            print("The given vertex don't exist on graph")
            pass

    def findPath(self, vertex1, vertex2, path=list()):
        """ Find any path from vertex1 to vertex2 """
        nextToVisit = [vertex1]
        isVisited = {key:False for key in self.graphDict.keys()}
        if vertex1 not in self.graphDict.keys(): return None
        while nextToVisit:
            vertexIt = nextToVisit.pop(0)
            if isVisited[vertexIt]: self.__removeVertexFromPath(vertexIt, path)
            else:
                path.append(vertexIt)
                isVisited[vertexIt] = True
                if vertexIt == vertex2: return path
                else:
                    hasAdjVertex = self.__addNextToVisit(vertexIt, nextToVisit, isVisited)
                    if not hasAdjVertex:
                        self.__removeVertexFromPath(vertexIt, path)
        return None

    def __addNextToVisit(self, vertex, nextToVisit, isVisited):
        """ Helper for add non visited adjacent vertex to nextToVisit queue """
        adjVertexList = self.graphDict[vertex]
        hasAdjVertex = False
        for adjVertex in adjVertexList:
            if not isVisited[adjVertex]:
                nextToVisit.append(adjVertex)
                hasAdjVertex = True
        return hasAdjVertex

    def __removeVertexFromPath(self, vertex, path):
        """ Helper for remove vertex from path """
        try:
            path.remove(vertex)
        except Exception as e:
            pass

    def getVertices(self):
        """ Return all vertices on graph """
        return list(self.graphDict.keys())

    def getEdges(self):
        """ Return all edges on graph """
        return self.__generateEdges()

    def __generateEdges(self):
        """ Method to generate the edges of the graph """
        edges = list()
        for vertex in self.graphDict:
            for adjVertex in self.graphDict[vertex]:
                edges.append((vertex, adjVertex))
        return edges

    def __str__(self):
        pp = pprint.PrettyPrinter()
        return pp.pformat(dict(self.graphDict))

if __name__ == "__main__":
    edges = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
    graph = Graph(edges)
    graph.add('G', 'B')
    graph.add('E', 'D')
    print("Graph content:\n{}".format(graph))
    print("Path from {} {}\n{}".format('G', 'E', graph.findPath('G', 'E')))
