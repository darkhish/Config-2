import graphviz
import io



def Render():
    dot = graphviz.Digraph()
    dot.node('A', 'Node A')
    dot.node('B', 'Node B')
    dot.edge('A', 'B', 'Edge 1')
    dot.edge('B', 'A', 'Edge 2')

    dot.render('graph', view=True)


dot = graphviz.Digraph()

with io.open('packages.txt', 'r', encoding='utf-8') as file:
    cnt = 0
    libs = []
    for line in file:
        if line.find('Package') == 0:
            print('Package:', line, end='')
            package = line[8:].replace('_', '-')
            dot.node(package, 'Package' + package)
        if line.find('Depends') == 0:
            print(line, end='')
            depends = str.split(line[8:], ',')
            for lib in depends:
                cnt += 1
                index = lib.find('(')
                if index > 0 :
                    lib = lib[0:index - 1]
                lib = lib.replace('_', '-')
                if not(lib in libs):
                    libs.append(lib)
                    dot.node(lib, 'Lib' + lib)
                    dot.edge(package, lib, '-')
    print(cnt, len(libs))

dot.render('graph', view=True)