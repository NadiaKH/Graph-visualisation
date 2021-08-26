import viz.structures as structures
from viz.draw import generate_gif


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
            #print("\ntop", top)
            try:
                next_v = next(self.graph[top])

            except StopIteration:
                #print("pop")
                self.stack.pop()
            else:
                #print(next_v, end=' ')
                if not self.seen[next_v]:
                    self.put(next_v)
                    break
        else:
            raise StopIteration()

        return top, next_v


#if __name__ == '__main__':
    #edges = [x for x in DFS(1, graph1)]
    #traverse = [edge[1] for edge in edges]
    #print(edges)
    #print(traverse)
    #generate_gif(graph1, edges)

    #s = structures.Stack(10)
    #s.push(1)
    #s.pop()
    #print(s.empty())


