if __name__ == '__main__':
    def naive_traverse(p='start', path=None, minor_revisited=False):
        path = path or [p]
        if p == 'end':
            paths.append(path)
            return
        for q in graph[p]:
            if q in path and q[0].islower():
                if q != 'start' and not minor_revisited:
                    naive_traverse(q, path + [q], True)
                continue
            naive_traverse(q, path + [q], minor_revisited)

    graph = (c := {}, *((c.setdefault(k, []).append(v), c.setdefault(v, []).append(k)) for k, v in
                        [(s for s in line.strip().split('-')) for line in open(0).readlines()]))[0]
    paths = []

    print(*(naive_traverse(minor_revisited=True), len(paths), paths.clear(), naive_traverse(), len(paths))[1::3], sep='\n')
    # print(()[1])
