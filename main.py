import sys

sys.stdin = open("input.txt", "r")


class ClassModel():
    def __init__(self, name="unnamed"):
        self.name = name
        self.childs = {self}
        self.parents = set()

    def add_parents(self, parents):
        self.parents |= parents
        for p in parents:
            self.parents |= p.parents

        for c in self.childs:
            c.parents |= self.parents

        for p in self.parents:
            p.childs |= self.childs
        return self

    def __repr__(self):
        return ' '.join(
            [self.name, 'CHILDS:', *[child.name for child in self.childs], 'PARENTS:', *[p.name for p in self.parents]])

    # def add_childs(self, childs):
    #     self.childs |= childs
    #     for parent in self.parents:
    #         parent.childs |= childs
    #     for c in childs:
    #         c.parents |= self.parents
    #     return self


models = dict()


def create_model(name, parents=[]):
    if name not in models:
        models[name] = ClassModel(name=name)

    paretns_set = set()
    for p_name in parents:
        if p_name not in models:
            models[p_name] = ClassModel(name=p_name)
        paretns_set.add(models[p_name])

    models[name].add_parents(paretns_set)


def is_ancestor(ancestor_name, child_name):
    if models[child_name] in models[ancestor_name].childs:
        print("Yes")
    else:
        print("No")


def model_from_input(input_str):
    if input_str[0] == '#':
        return
    line = input_str.split(":")
    class_name = line[0].strip()
    if len(line) == 2:
        class_parents = line[1].split()
        create_model(class_name, parents=class_parents)
    else:
        create_model(class_name)


if __name__ == "__main__":
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
