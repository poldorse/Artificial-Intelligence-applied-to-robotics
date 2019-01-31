import sys
import datetime

#
# A* Algorithm
#
def A_estrella(root, x_sol, y_sol):
    
    llista = [root]
    f = 0

    while llista:
        
        cur_node = llista[0]
        cur_node.h = cur_node.get_h(x_sol, y_sol)
        f = cur_node.g + cur_node.h
        
        if cur_node.x == x_sol and cur_node.y == y_sol:
            print("Solucio: ")
            print(cur_node.path)
            return cur_node.path
            break
            
        pare = llista.pop(0)
        for child in pare.get_children():
            child.g = f
            llista.insert(0, child)
        
        llista.sort(key = lambda x : x.g, reverse=False)
        
        if cur_node.x != x_sol and cur_node.y != y_sol:
            llista[0].path.append(llista[0])
  
      
#
# A* Algorithm
#
def Moviments(path):
    pos_actual = path[0]
    direccio = 1
    accions = [] 
    i = 0
    
    while pos_actual.id != "goal1":
        i = i + 1
        
        if pos_actual.x < path[i].x:
            if direccio == 1:
                accions.append("forward")
                direccio = 1
            elif direccio == 2:
                accions.append("left-forward")
                direccio = 1
            elif direccio == 3:
                accions.append("180-forward")
                direccio = 1
            elif direccio == 4:
                accions.append("right-forward")
                direccio = 1
                
        if pos_actual.x > path[i].x:
            if direccio == 1:
                accions.append("180-forward")
                direccio = 3
            elif direccio == 2:
                accions.append("right-forward")
                direccio = 3
            elif direccio == 3:
                accions.append("forward")
                direccio = 3
            elif direccio == 4:
                accions.append("left-forward")
                direccio = 3
                
        if pos_actual.y < path[i].y:
            if direccio == 1:
                accions.append("left-forward")
                direccio = 4
            elif direccio == 2:
                accions.append("180-forward")
                direccio = 4
            elif direccio == 3:
                accions.append("left-forward")
                direccio = 4
            elif direccio == 4:
                accions.append("forward")
                direccio = 4
                
        if pos_actual.y > path[i].y:
            if direccio == 1:
                accions.append("right-forward")
                direccio = 2
            elif direccio == 2:
                accions.append("forward")
                direccio = 2
            elif direccio == 3:
                accions.append("right-forward")
                direccio = 2
            elif direccio == 4:
                accions.append("180-forward")
                direccio = 2

        pos_actual = path[i]
        
    return accions

#
# The tree
#
class TreeNode(object):
    def __init__(self, id_, x, y, dad=None):
        self.id = id_
        self.children = []
        self.g = 0
        self.f = 0
        self.x = x
        self.y = y
        self.dad = dad
        self.path = []
    
    def __repr__(self):
        return "[%s]" % self.id
    
    def add_child(self, node):
        node.add_dad(self)
        self.children.append(node)

    def add_path(self):
        self.path = self.dad.path[:]
        self.path.append(self)
    
    def add_dad(self, node):
        self.dad = node

    def get_dad(self):
        return self.dad
    
    def get_children(self):
        return self.children
    
    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children
    
    def get_h(self, x_sol, y_sol):
        return abs(self.x - x_sol) + abs(self.y - y_sol)
        
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y
    
#
# Test tree
#
def get_example_tree():
    
    #create nodes
    root = TreeNode("a4",1,3)
    
    a1 = TreeNode("a1",1,6)
    a2 = TreeNode("a2",1,5)
    a3 = TreeNode("a3",1,4)
    a5 = TreeNode("a5",1,2)
    a6 = TreeNode("a6",1,1)
    
    b1 = TreeNode("b1",2,6)
    b2 = TreeNode("b2",2,5)
    b3 = TreeNode("b3",2,4)
    b4 = TreeNode("b4",2,3)
    b5 = TreeNode("b5",2,2)
    b6 = TreeNode("b6",2,1)
    
    c1 = TreeNode("c1",3,6)
    c2 = TreeNode("c2",3,5)
    c3 = TreeNode("c3",3,4)
    c4 = TreeNode("c4",3,3)
    c5 = TreeNode("c5",3,2)
    c6 = TreeNode("c6",3,1)
    
    d1 = TreeNode("d1",4,6)
    d2 = TreeNode("d2",4,5)
    d3 = TreeNode("d3",4,4)
    d4 = TreeNode("d4",4,3)
    d5 = TreeNode("d5",4,2)
    d6 = TreeNode("d6",4,1)
    
    e1 = TreeNode("e1",5,6)
    e2 = TreeNode("e2",5,5)
    e3 = TreeNode("e3",5,4)
    e4 = TreeNode("e4",5,3)
    e5 = TreeNode("e5",5,2)
    e6 = TreeNode("e6",5,1)
    
    f1 = TreeNode("f1",6,6)
    f2 = TreeNode("f2",6,5)
    f3 = TreeNode("f3",6,4)
    f4 = TreeNode("f4",6,3)
    f5 = TreeNode("f5",6,2)
    f6 = TreeNode("f6",6,1)

    g1 = TreeNode("g1",7,6)
    g2 = TreeNode("g2",7,5)
    g3 = TreeNode("g3",7,4)
    goal1 = TreeNode("goal1",7,3)
    goal2 = TreeNode("goal2",7,3)
    g5 = TreeNode("g5",7,2)
    g6 = TreeNode("g6",7,1)
    
    #add nodes
    root.add_child(a5)
    root.add_child(b4)
    root.path.append(root)
    
    a5.add_child(a6)
    a5.add_path()
    
    a6.add_child(b6)
    a6.add_path()
    
    b6.add_child(c6)
    b6.add_path()
    
    c6.add_child(d6)
    c6.add_path()
    
    d6.add_child(e6)
    d6.add_path()
    
    e6.add_child(f6)
    e6.add_path()
    
    f6.add_child(g6)
    f6.add_path()
    
    g6.add_child(g5)
    g6.add_path()
    
    g5.add_child(goal1)
    g5.add_path()
    
    goal1.add_path()
    
    b4.add_child(b3)
    b4.add_path()
    
    b3.add_child(a3)
    b3.add_path()
    
    a3.add_child(a2)
    a3.add_path()
    
    a2.add_child(a1)
    a2.add_path()
    
    a1.add_child(b1)
    a1.add_path()
    
    b1.add_child(b2)
    b1.add_path()
    
    b2.add_child(c2)
    b2.add_path()
    
    c2.add_child(c1)
    c2.add_path()
    
    c1.add_child(d1)
    c1.add_path()
    
    d1.add_child(d2)
    d1.add_path()
    
    d2.add_child(d3)
    d2.add_path()
    
    d3.add_child(c3)
    d3.add_path()
    
    c3.add_child(c4)
    c3.add_path()
    
    c4.add_child(c5)
    c4.add_path()
    
    c5.add_child(b5)
    c5.add_child(d5)
    c5.add_path()
    
    b5.add_path()
        
    d5.add_child(e5)
    d5.add_path()
    
    e5.add_child(f5)
    e5.add_path()
    
    f5.add_child(f4)
    f5.add_path()
    
    f4.add_child(e4)
    f4.add_child(f3)
    f4.add_path()
    
    e4.add_child(d4)
    e4.add_path()
    
    d4.add_path()
    
    f3.add_child(f2)
    f3.add_path()
    
    f2.add_child(f1)
    f2.add_path()
    
    f1.add_child(e1)
    f1.add_child(g1)
    f1.add_path()
    
    e1.add_child(e2)
    e1.add_path()
    
    e2.add_child(e3)
    e2.add_path()
    
    e3.add_path()
    
    g1.add_child(g2)
    g1.add_path()
    
    g2.add_child(g3)
    g2.add_path()
    
    g3.add_child(goal2)
    g3.add_path()
    
    goal2.add_path()
    
    return root



#
# The main
#
if __name__ == "__main__":
    
    root = get_example_tree()
    
    print("\n------ A* ------\n")
    start = datetime.datetime.now()
    path = A_estrella(root, 7, 3)
    accions = Moviments(path)
    print()
    print("Accions:")
    print(accions)
    fitxer = open("accions.txt", "w")
    i = 0
    while i < len(accions):
        fitxer.write("%s\n" % accions[i])
        i = i + 1
    fitxer.close()
    done = datetime.datetime.now()
    elapsed = done - start
    print ("\nFinished in ", elapsed.microseconds , " microseconds")
