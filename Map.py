from Point import Point
from Triangle import Triangle
from Delaunay2d import Delaunay2d
import numpy as np
import GameController


class Map:

    # List of triangulated map
    #   triangleList = None #= [Triangle(Point(0,400), Point(200,400), Point(200, 600)),
    #                Triangle(Point(0,400), Point(0,600), Point(200, 600))]


    def __init__(self, w, h):
        self.winWidth = w
        self.winHeight = h
        self.startPosition = Point(100,300) #start race position
        self.endPosition = None # end race position
        self.DelaunayTriangleList = list()
        self.triangleDotList = list()
        self.triangleObstacleList = list()
        self.relativeDots = [np.array([0.3, 0]), np.array([0.1, 0.2]), np.array([0, 0.6]), np.array([0.15, 0.85]), np.array([0.7, 1]), np.array([0.8, 0.8]), np.array([1, 0.65]), np.array([0.9, 0.4]), np.array([0.7, 0.3]), np.array([0.65, 0.2])]
        self.dots = list(map(lambda x:self.scaleCoordinates(x), self.relativeDots))
        self.relativeDots = [np.array([0.4, 0.4]), np.array([0.4, 0.6]), np.array([0.6, 0.6]), np.array([0.6, 0.4])]
        self.obstacleDots = list(map(lambda x: self.scaleCoordinates(x), self.relativeDots))
        self.relativeCheckLines = [[Point(0.5, 0.4), Point(0.5, 0.2)],[Point(0.6, 0.5), Point(0.8, 0.5)],[Point(0.5, 0.6), Point(0.5, 0.8)],[Point(0.2, 0.5), Point(0.4, 0.5)]]
        self.checkLines = list(map(lambda x: self.scaleCheckpoints(x), self.relativeCheckLines))
        self.TriangulateMap()


    def scaleCoordinates(self, x):
        return np.array([x[0] * self.winWidth, x[1] * self.winHeight])

    def scaleCheckpoints(self, p):
        return [Point(p[0].x * self.winWidth, p[0].y * self.winHeight),
                Point(p[1].x * self.winWidth, p[1].y * self.winHeight)]

    # Triangulate map
    def TriangulateMap(self):
        self.DelaunayTriangleList = Delaunay2d(self.dots).getTriangles()
        for t in self.DelaunayTriangleList:
            tr = Triangle(Point(Delaunay2d(self.dots).points[t[0]][0], Delaunay2d(self.dots).points[t[0]][1]), \
                          Point(Delaunay2d(self.dots).points[t[1]][0], Delaunay2d(self.dots).points[t[1]][1]), \
                          Point(Delaunay2d(self.dots).points[t[2]][0], Delaunay2d(self.dots).points[t[2]][1]))
            self.triangleDotList.append(tr)
        self.DelaunayTriangleList2 = Delaunay2d(self.obstacleDots).getTriangles()
        for t in self.DelaunayTriangleList2:
            tr = Triangle(Point(Delaunay2d(self.obstacleDots).points[t[0]][0], Delaunay2d(self.obstacleDots).points[t[0]][1]), \
                          Point(Delaunay2d(self.obstacleDots).points[t[1]][0], Delaunay2d(self.obstacleDots).points[t[1]][1]), \
                          Point(Delaunay2d(self.obstacleDots).points[t[2]][0], Delaunay2d(self.obstacleDots).points[t[2]][1]))
            self.triangleObstacleList.append(tr)


    '''
    TODO:
    2. Singlton klasa
    3. Start i EndPosition da se obradi kad je presao trku i stigao do cilja
    4. Generisanje komplikovanije staze
    '''