from mindmapleaf import MindMapLeaf
import os


class MindMapComposite:
    def __init__(self, name, shape,):
        self.name = name
        self.shape = shape
        self.children = []


    def add(self, child):
        self.children.append(child)


    def remove(self, child):
        if child in self.children:
            self.children.remove(child)


    def __str__(self):
        return self.get_shape_representation().format(name=self.name)


    def display(self, indent=0):
        if indent == 0:
            print('mindmap\nroot', end=' ')
        print(" " * indent + self.name)
        for child in self.children:
            child.display(indent + 2)


    def get_shape_representation(self):
        shapes = {"circle": "(({name}))",
                  "oval": "({name})",
                  "square": "[{name}]",
                  "cloud": "){name}(",
                  "hexagon": "{{{{{name}}}}}",
                  "bang": ")){name}(("
                  }
        return shapes.get(self.shape, "{name}")
