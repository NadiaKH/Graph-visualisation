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
        self.seen = seen = {v: False for v in graph}
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
            return self.init_v

        next_v = None

        while not next_v or self.seen[next_v]:
            top = self.stack.top()
            if not top:
                raise StopIteration()

            try:
                next_v = next(self.graph[top])
            except StopIteration:
                self.stack.pop()

        self.put(next_v)
        return next_v


if __name__ == '__main__':
    for x in DFS(1, graph1):
        print(x)


