import random
import copy
import numpy as np



with open('day25test.txt') as f:
    lines = f.readlines()
    q=0
    edges = {} 
    nodeNames = {}
    edgeSet = set()
    for i in range(len(lines)):
        lines[i] = (lines[i][:3] + lines[i][4:-1]).split()
        for j in range(len(lines[i])):
            if lines[i][j] not in nodeNames:
                nodeNames[lines[i][j]] = q
                q+=1
            lines[i][j] = nodeNames[lines[i][j]]
        for j in range(1):
            for k in range(1,len(lines[i])):
                if k!=j:
                    if (','+str(lines[i][j])+',') in edges:
                        if (lines[i][j],lines[i][k]) not in edges[','+str(lines[i][j])+',']:
                            #edges[','+str(lines[i][j])+','] += [(lines[i][j],lines[i][k])]
                            edgeSet.add((lines[i][j],lines[i][k]))
                    else:
                        #edges[','+str(lines[i][j])+','] = [(lines[i][j],lines[i][k])]
                        edgeSet.add((lines[i][j],lines[i][k]))
                    if (',' + str(lines[i][k]) + ',') not in edges:
                        #edges[',' + str(lines[i][k])+','] = [(lines[i][k],lines[i][j])]
                        edgeSet.add((lines[i][k],lines[i][j]))
                    else:
                        #edges[','+str(lines[i][k])+','] += [(lines[i][k],lines[i][j])]
                        edgeSet.add((lines[i][k],lines[i][j]))
    print(len(nodeNames))
    adjMatrix =  np.zeros((len(nodeNames),len(nodeNames)))
    degMatrix = np.zeros((len(nodeNames),len(nodeNames)))
    laplacian = np.zeros((len(nodeNames),len(nodeNames)))

    for edge in edgeSet:
        adjMatrix[edge[0],edge[1]] =1
        adjMatrix[edge[1],edge[0]] =1

    for i in range(len(adjMatrix)):
        degMatrix[i,i] = adjMatrix[:,i].sum()
    print(degMatrix)
    laplacian = degMatrix- adjMatrix
    print(laplacian)
    eigenvalues,eigenvectors = np.linalg.eigh(laplacian)
    less = 0
    greater = 0
    for c in (eigenvectors[:,1]):
        if c>0:
            greater +=1
        else:
            less +=1
    print(less*greater)















   # vertices = []
   # for vert in edges:
   #     vertices.append(vert)

   # def contractVertices(nedges,nvertices,first,second,edgeSetCopy):
   #     newEdges = []
   #     for edge in nedges[first]:
   #         if (','+str(edge[1])+',') not in second and (','+str(edge[1])+',') not in first:
   #             newEdges.append(edge)
   #         elif edge in edgeSetCopy:
   #             edgeSetCopy.remove(edge)
   #     for edge in nedges[second]:
   #         if (','+str(edge[1])+',') not in first and (','+str(edge[1])+',') not in second:
   #             newEdges.append(edge)
   #         elif edge in edgeSetCopy:
   #             edgeSetCopy.remove(edge)
   #     newVert = first+second
   #     nvertices.remove(first)
   #     nvertices.remove(second)
   #     nvertices.append(newVert)
   #     nedges.pop(first)
   #     nedges.pop(second)
   #     nedges[newVert] = newEdges
   #     return nedges, nvertices, edgeSetCopy

   # k=0
   # minLeng = float('inf')
   # minVert = []
   # ##CHOOSE AN EDGE, NOT TWO VERTICES
   # def findSet(k,verts):
   #     for vert in verts:
   #         if vert.find(',' + str(k) + ',') !=-1:
   #             return vert
   # print("ASDFASDFP")
   # while k<1000:   
   #     vertCopy = vertices.copy()
   #     edgeCopy = edges.copy()
   #     edgeSetCopy = edgeSet.copy()
   #     while len(vertCopy)>2:
   #         first = random.choice(list(edgeSetCopy))
   #         second = random.choice(list(edgeSetCopy))
   #         first = findSet(first[0],vertCopy)
   #         second = findSet(second[0],vertCopy)
   #         while first == second: 
   #             second = random.choice(list(edgeSetCopy))
   #             second = findSet(second[0],vertCopy)
   #         edgeCopy, vertCopy, edgeSetCopy = contractVertices(edgeCopy,vertCopy,first,second,edgeSetCopy)
   #     if len(edgeCopy[vertCopy[0]]) == 3 and len(edgeCopy[vertCopy[1]]) == 3:
   #         print(vertCopy,'asdfasdfasdfasdfasdfwefwef23fihasvbnasd')
   #         print(edgeCopy)
   #         print((vertCopy[0].count(','))/2,(vertCopy[1].count(','))/2,(vertCopy[0].count(','))/2*(vertCopy[1].count(','))/2,)
   #         break
   #     k+=1

   #        


   #      #   first = ',12,'
   #      #   second = ',8,'
   #      #   edgeCopy, vertCopy, edgeSetCopy = contractVertices(edgeCopy,vertCopy,first,second,edgeSetCopy)
   #      #   first = ',12,,8,'
   #      #   second = ',0,'
   #      #   edgeCopy, vertCopy, edgeSetCopy = contractVertices(edgeCopy,vertCopy,first,second,edgeSetCopy)
   #      #   first = ',12,,8,,0,'
   #      #   second = ',13,'
   #      #   edgeCopy, vertCopy, edgeSetCopy = contractVertices(edgeCopy,vertCopy,first,second,edgeSetCopy)
   #      #   first = ',12,,8,,0,,13,'
   #      #   second = ',1,'
   #      #   edgeCopy, vertCopy, edgeSetCopy = contractVertices(edgeCopy,vertCopy,first,second,edgeSetCopy)
   #      #   first = ',12,,8,,0,,13,,1,'
   #      #   second = ',2,'
   #      #   edgeCopy, vertCopy, edgeSetCopy = contractVertices(edgeCopy,vertCopy,first,second,edgeSetCopy)

   #     

   # print("ASDFASDFASDF")
