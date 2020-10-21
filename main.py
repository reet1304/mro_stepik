import sys
sys.stdin = open("input.txt", "r")


class ClassModel():
    def __init__(self):
        self.childs = {self}
        self.parents = {self}

    def add_parents(self, parents):
        self.parents |= parents
        for child in self.childs:
            child.parents |= parents
        for p in parents:
            p.childs |= self.childs
        return self

    def add_childs(self, childs):
        self.childs |= childs
        for parent in self.parents:
            parent.childs |= childs
        for c in childs:
            c.parents |= self.parents
        return self


models = dict()


def create_model(name, parents=[]):
    if name not in models:
        models[name] = ClassModel()

    paretns_set = set()
    for p_name in parents:
        if p_name not in models:
            models[p_name] = ClassModel()
        models[p_name].add_childs({models[name]})
        paretns_set.add(models[p_name])
    models[name].add_parents(paretns_set)


def is_ancestor(ancestor_name, child_name):
    if models[child_name] in models[ancestor_name].childs:
        print("Yes")
    else:
        print("No")


def model_from_input(input_str):
    line = input_str.split(":")
    class_name = line[0].strip()
    if len(line) == 2:
        class_parents = line[1].split()
        create_model(class_name, parents=class_parents)
    else:
        create_model(class_name)


x = int(input())
for i in range(x):
    model_from_input(input())
o = int(input())
for i in range(o):
    s = input()
    s = s.split()
    for i in s:
        i.strip()
    is_ancestor(s[0], s[1])