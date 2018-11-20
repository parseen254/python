# -*- coding: utf-8 -*-
'''
An auto-balanced binary tree!
'''
import math
import random
class my_queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0
    def isEmpty(self):
        return self.head == self.tail
    def push(self,data):
        self.data.append(data)
        self.tail = self.tail + 1
    def pop(self):
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret
    def count(self):
        return self.tail - self.head
    def print(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])
        
class my_node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    def getdata(self):
        return self.data
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def getheight(self):
        return self.height
    def setdata(self,data):
        self.data = data
        return
    def setleft(self,node):
        self.left = node
        return
    def setright(self,node):
        self.right = node
        return
    def setheight(self,height):
        self.height = height
        return

def getheight(node):
#    print("xxx")
    if node is None:
        return 0
    return node.getheight()

def my_max(a,b):
    if a > b:
        return a
    return b



def leftrotation(node):
    print("left rotation node:",node.getdata())
    ret = node.getleft()
    node.setleft(ret.getright())
    ret.setright(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret

def rightrotation(node):
    print("right rotation node:",node.getdata())
    ret = node.getright()
    node.setright(ret.getleft())
    ret.setleft(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret

def lrrotation(node):
    node.setright(leftrotation(node.getright()))
    return rightrotation(node)

def rlrotation(node):
    node.setleft(rightrotation(node.getleft()))
    return leftrotation(node)

def insert_node(node,data):
    if node is None:
        return my_node(data)
    if data < node.getdata():
        node.setleft(insert_node(node.getleft(),data))
        if getheight(node.getleft()) - getheight(node.getright()) == 2:
            if data < node.getleft().getdata():
                node = leftrotation(node)
            else:
                node = rlrotation(node)
    else:
        node.setright(insert_node(node.getright(),data))
        if getheight(node.getright()) - getheight(node.getleft()) == 2:
            if data < node.getright().getdata():
                node = lrrotation(node)
            else:
                node = rightrotation(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    return node

def getRightMost(root):
    while root.getright() is not None:
        root = root.getright()
    return root.getdata()
def getLeftMost(root):
    while root.getleft() is not None:
        root = root.getleft()
    return root.getdata()

def del_node(root,data):
    if root.getdata() == data:
        if root.getleft() is not None and root.getright() is not None:
            temp_data = getLeftMost(root.getright())
            root.setdata(temp_data)
            root.setright(del_node(root.getright(),temp_data))
        elif root.getleft() is not None:
            root = root.getleft()
        else:
            root = root.getright()
    elif root.getdata() > data:
        if root.getleft() is None:
            print("No such data")
            return root
        else:
            root.setleft(del_node(root.getleft(),data))
    elif root.getdata() < data:
        if root.getright() is None:
            return root
        else:
            root.setright(del_node(root.getright(),data))
    if root is None:
        return root
    if getheight(root.getright()) - getheight(root.getleft()) == 2:
        if getheight(root.getright().getright()) > getheight(root.getright().getleft()):
            root = rightrotation(root)
        else:
            root = lrrotation(root)
    elif getheight(root.getright()) - getheight(root.getleft()) == -2:
        if getheight(root.getleft().getleft()) > getheight(root.getleft().getright()):
            root = leftrotation(root)
        else:
            root = rlrotation(root)
    height = my_max(getheight(root.getright()),getheight(root.getleft())) + 1
    root.setheight(height)
    return root

class AVLtree:
    def __init__(self):
        self.root = None
    def getheight(self):
#        print("yyy")
        return getheight(self.root)
    def insert(self,data):
        print("insert:"+str(data))
        self.root = insert_node(self.root,data)
        
    def del_node(self,data):
        print("delete:"+str(data))
        if self.root is None:
            print("Tree is empty!")
            return
        self.root = del_node(self.root,data)
    def traversale(self):
        q = my_queue()
        q.push(self.root)
        layer = self.getheight()
        if layer == 0:
            return
        cnt = 0
        while not q.isEmpty():
            node = q.pop()
            space = " "*int(math.pow(2,layer-1))
            print(space,end = "")
            if node is None:
                print("*",end = "")
                q.push(None)
                q.push(None)
            else:
                print(node.getdata(),end = "")
                q.push(node.getleft())
                q.push(node.getright())
            print(space,end = "")
            cnt = cnt + 1
            for i in range(100):
                if cnt == math.pow(2,i) - 1:
                    layer = layer -1 
                    if layer == 0:
                        print()
                        print("*************************************")
                        return
                    print()
                    break
        print()
        print("*************************************")
        return
    
    def test(self):
        getheight(None)
        print("****")
        self.getheight()
if __name__ == "__main__":
#    t = AVLtree()
#    t.test()
#    q = my_queue()
##    q.push(1)
##    q.push(2)
#    for i in range(10):
#        q.push(i)
#    q.print()
#    q.push(90)
#    q.print()
#    
#    q.pop()
#    q.print()
    t = AVLtree()
    t.traversale()
#    t.insert(7)
##    t.traversale()
#    
#    t.insert(8)
#    t.traversale()
#    t.insert(3)
#    t.traversale()
#    t.insert(6)
#    t.traversale()
#    t.insert(1)
#    t.traversale()
#    t.insert(10)
#    t.traversale()
#    t.insert(14)
#    t.traversale()
#    t.insert(13)
#    t.traversale()
##    t.traversale()
#    t.insert(4)
#    t.traversale()
#    t.insert(7)
#    t.traversale()
#    
#    
#    t.del_node(8)
#    t.traversale()
#    t.del_node(3)
#    t.traversale()
#    t.del_node(6)
#    t.traversale()
#    t.del_node(1)
#    t.traversale()
#    t.del_node(10)
#    t.traversale()
#    t.del_node(14)
#    t.traversale()
#    t.del_node(13)
#    t.traversale()
##    t.traversale()
#    t.del_node(4)
#    t.traversale()
#    t.del_node(7)
#    t.traversale()
    l = list(range(10))
    random.shuffle(l)
    for i in l:
        t.insert(i)
        t.traversale()
        
    random.shuffle(l)
    for i in l:
        t.del_node(i)
        t.traversale()
    
    
        





























