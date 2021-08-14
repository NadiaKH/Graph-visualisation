import structures

graph1 = {1: [2, 4, 5],
          2: [1, 3],
          3: [2, 5],
          4: [1, 5],
          5: [6, 7],
          6: [5, 8, 10],
          7: [5, 8, 9],
          8: [6, 7, 9, 10, 11],
          9: [7, 8],
          10: [6, 8],
          11: [8]}

graph2 = {
 0: [1, 2, 6, 14, 16, 18, 22, 25, 48],
 1: [0, 9, 14, 16, 32, 41, 43, 45, 47],
 2: [0, 17, 19, 33, 43],
 3: [13, 20, 46],
 4: [13, 26, 43, 47],
 5: [20, 28, 37, 43],
 6: [0, 13, 15, 17, 20, 31, 42],
 7: [8, 18, 25, 27, 28, 33, 36, 45, 46],
 8: [7, 10, 11, 31, 35, 44],
 9: [1, 12, 24, 25, 42],
 10: [8, 14, 25, 26, 37],
 11: [8, 12, 22, 23, 26, 30, 42],
 12: [9, 11],
 13: [3, 4, 6, 15],
 14: [0, 1, 10, 19, 34, 35, 47],
 15: [6, 13, 26, 28, 31, 35],
 16: [0, 1, 23, 24, 31, 36],
 17: [2, 6, 29, 32, 39],
 18: [0, 7, 20, 22, 38, 43, 48],
 19: [2, 14, 21, 24, 26],
 20: [3, 5, 6, 18, 28, 38, 45, 47],
 21: [19, 22, 44, 45],
 22: [0, 11, 18, 21, 41],
 23: [11, 16, 29, 30],
 24: [9, 16, 19, 27, 34, 47, 49],
 25: [0, 7, 9, 10, 37],
 26: [4, 10, 11, 15, 19, 30],
 27: [7, 24, 37],
 28: [5, 7, 15, 20, 35],
 29: [17, 23, 40, 46, 47, 49],
 30: [11, 23, 26, 31, 33, 39, 40],
 31: [6, 8, 15, 16, 30, 48],
 32: [1, 17, 39, 40],
 33: [2, 7, 30, 37, 39, 46],
 34: [14, 24, 44],
 35: [8, 14, 15, 28],
 36: [7, 16, 46],
 37: [5, 10, 25, 27, 33],
 38: [18, 20, 48],
 39: [17, 30, 32, 33, 49],
 40: [29, 30, 32],
 41: [1, 22, 42, 49],
 42: [6, 9, 11, 41, 48],
 43: [1, 2, 4, 5, 18, 44],
 44: [8, 21, 34, 43, 46],
 45: [1, 7, 20, 21],
 46: [3, 7, 29, 33, 36, 44],
 47: [1, 4, 14, 20, 24, 29],
 48: [0, 18, 31, 38, 42],
 49: [24, 29, 39, 41]}

class Children:
    def __init__(self, children):
        self.children = children
        self.index = 0

    def __next__(self):
        if self.index < len(self.children):
            self.index += 1
            return self.children[self.index - 1]
        raise StopIteration()

    def __iter__(self):
        return self


class DFS:
    def __init__(self, init_v, graph):
        self.seen = {v: False for v in graph}
        self.graph = {v: Children(graph[v]) for v in graph}
        self.init_v = init_v
        self.stack = structures.Stack(len(graph))

    def put(self, v):
        self.stack.push(v)
        self.seen[v] = True


    def top(self):
        return self.stack.top()

    def __iter__(self):
        return self

    def __next__(self):

        if not self.seen[self.init_v]:
            self.put(self.init_v)
            return None, self.init_v

        next_v = None
        top = None

        #while not next_v or self.seen[next_v]:
        while not self.stack.empty():
            top = self.stack.top()
            print(self.stack.index)
            print("top", top)
            try:
                next_v = next(self.graph[top])

            except StopIteration:
                print("pop")
                self.stack.pop()
            else:
                if not self.seen[next_v]:
                    self.put(next_v)
                    break
        else:
            raise StopIteration()

        return top, next_v


if __name__ == '__main__':
    edges = [x for x in DFS(1, graph2)]
    traverse = [edge[1] for edge in edges]
    print(edges)
    print(traverse)

    #s = structures.Stack(10)
    #s.push(1)
    #s.pop()
    #print(s.empty())


