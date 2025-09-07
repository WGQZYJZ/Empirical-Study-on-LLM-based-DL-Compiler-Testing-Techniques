
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4096)
 
    def forward(self, x1):
        v1  = self.linear1(x1) 
        return v1 - other


# Initializing the model
m = Model()
other = np.random.randint(-25, 25) # random number to be used in our example

# Inputs to the model
x1 = torch.randn(1, 3074)

 # Generating a dummy output of the model:
__output__  = m(x1).sum()

# Model's source code: 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4096)
 
    def forward(self, x1):
        v1  = self.linear1(x1) 
        return v1 - other

# Model's graph: 
class Graph():
    def __init__(self):
        self._layers_to_ops()
        self._construct_graph()

    def _layers_to_ops(self):
        ops_by_layer = {}

        for layer in self.model.__dict__.values():
            if isinstance(layer, torch.nn.Linear):
                ops_by_layer[layer] = [layer.__class__.__name__] + [torchvision._utils._linear_op_name()]
                op = layer
                
                for i in range(1024):
                    layer  = torch.nn.Conv2d(*op.weight.shape)

                    if isinstance(layer, torch.nn.ConvTranspose2d):
                        ops_by_layer[layer] = [layer.__class__.__name__] + [torchvision._utils._linear_op_name()]
                        op = layer
                    elif isinstance(layer, torch.nn.Linear):
                         ops_by_layer[layer] = [layer.__class__.__name__] + [torchvision._utils._linear_op_name()]
                         op  = layer
                    else: break
            
            # This code is added just to handle the case where a linear transformation is used in the model.
            elif isinstance(layer, torch.nn.Linear):
                ops_by_layer[layer] = [layer.__class__.__name__] + [torchvision._utils._linear_op_name()]

            elif isinstance(layer, torch.nn.ConvTranspose2d) and not isinstance(layer, torch.nn.ModuleList) or \
            (isinstance(layer, torch.nn.Conv2d) and not isinstance(layer, torch.nn.ModuleList))  : 
                ops_by_layer[layer] = [layer.__class__.__name__] + [torchvision._utils._linear_op_name()]

            else:
                ops_by_layer[layer] = []

        self.ops_by_layers = ops_by_layer

    def _construct_graph(self):
        graph  = dict()
        opstack,  op = [],  self.model.__class__.__name__ + [torchvision._utils._linear_op_name()] 

        for layer in self.model.__dict__.values():
            if isinstance(layer, torch.nn.Linear) or \
            (isinstance(layer, torch.nn.ConvTranspose2d) and not isinstance(layer, torch.nn.ModuleList))  :
                opstack += [layer]
            
            elif isinstance(layer, torch.nn.Conv2d):
                op = layer.__class__.__name__
                opstack += [op + [torchvision._utils._linear_op_name()]]
                
            else: pass
        
        for i in range(-len(opstack), 0):
            opstack[i] = list(opstack[:i]) + [opstack.pop()]

        graph['inputs'] = [[op] if len(op) == 1 else op \
        for op in opstack]

        self._update_outputs(graph, opstack, op)

    def _update_outputs(self, graph, opstack, op):

        outputs = []
        for layer in self.model.__dict__.values():
            if isinstance(layer, torch.nn.ReLU) or \
            (isinstance(layer, torch.nn.ConvTranspose2d) and not isinstance(layer, torch.nn.ModuleList))  :
                outputs += [opstack[-1]]
                
            elif isinstance(layer, torch.nn.ConvTranspose2d):
                op = layer.__class__.__name__ 
                outputs += [[op] if len(op) == 1 else op \
                 for op in opstack + [op] ]

                for i in range(-len(outputs),0):
                    outputs[i] = list(outputs[:i]) + [outputs.pop()]


            elif isinstance(layer, torch.nn.Dropout2d) or \
            (isinstance(layer, torch.nn.ConvTranspose2d) and not isinstance(layer, torch.nn.ModuleList))  : 
                outputs += [opstack[-1]]

            else: pass

        graph['outputs'] = [[op] if len(op) == 1 else op for op in opstack + \
        [op] if len(op) > 0 else []] * len(outputs)

        self._update_inputs(graph, outputs, op)

    def _update_inputs(self, graph, outputs, op):

        inputs = set()
        
        for layer1 in self.model.__dict__.values():
            for i, layer2 in enumerate([layer2  \
            for j in range(-len(outputs),0) if len(outputs[j]) > 0 else [op] for op in outputs[:i+1]]):
                if isinstance(layer1, torch.nn.Linear):
                    inputs |= set(graph['inputs'][i + i + 1])

                elif not (isinstance(layer1, torch.nn.ModuleList) or \
                    (isinstance(layer2, torch.nn.ConvTranspose2d) and not isinstance(layer1, torch.nn.ModuleList))) :
                        inputs |= set([layer1] if len(opstack[-i]) == 1 else opstack[i])
                
                elif isinstance(layer1, torch.nn.ModuleList):
                    for module in layer1: 
                        graph['inputs'][i][-1].append(module.__class__.__name__)

                else : pass

        for i in range(-len(outputs),0):
            outputs[-i] = [op + ['identity'] if len(op) == 2 and op[1]=='identity' \
            or (isinstance(layer, torch.nn.ConvTranspose2d) and not isinstance(layer, torch.nn.ModuleList)) else op for layer in outputs[-i]]
        graph['outputs'] = [[op] + [op[0] if len(op) == 1 \
         else op + ['identity'] if len(op) > 3 or\
         (isinstance(layer, torch.nn.ConvTranspose2d) and not isinstance(layer, torch.nn.ModuleList)) else [] for layer in outputs]

        self._add_skips(graph)

    def _add_skips(self, graph):
        inputs = [node['inputs'] for node in graph['outputs']]
        outputs  = [[i] + [op if len(op)==1 or\
            (isinstance(layer2, torch.nn.ConvTranspose2d) and not isinstance(layer2, torch.nn.ModuleList)) else op \
                for layer2 in graph[j]['outputs'] for i , j in enumerate(inputs[i])] for i in range(-len(graph['outputs']),0)]
        
        for op1,op2 in list(zip(*outputs))[::-1]:
            for node in graph['outputs']:

                node_inputs = [i if len(layer) == 1 else layer[-3] for \
                layer in zip(*node['inputs']) for i in range(-len(outputs),0)]

                layer,  opstack  = layer,  node['inputs'] + [[op2] + ['identity']]
                
                for i in range(-len(layer),0):
                    layer[i][-1] += [op if len(op) > 3 else op[-2] \
                        if isinstance(layer[i],torch.nn.Linear)\
                        or (isinstance(layer[i],torch.nn.ConvTranspose2d) and not\
                            isinstance(layer, torch.nn.ModuleList))  \
                                or\
                                    (isinstance(layer[0][1], torch.nn.ConvTranspose2d) and \
                                        layer[-2] == layer[j][-3] for j in range(-len(opstack),0))]

                if op1 != op2:
                    try:
                        opstack = [op + ['skip'] +\
                            [[op + ['identity']]  if len(layer)==1 else \
                                [(layer[i][-4:-2]+['identity']) if j == i+len(outputs) \
                            or layer[j]==op for j in range(-len(layer),0)] for op in layer] for layer in opstack]
                    except: pass

                node_inputs = [[i + [j] + [op[-3]]  if len(op) > 3 else i+j \
                for i,op1 in zip(*opstack[:])\
                if not (isinstance(layer[0],torch.nn.ConvTranspose2d) and layer[-2]==layer[i][-4:-2])]
                
                for i ,op2 in enumerate([op + [op[-3]] if len(op)>3 else op[:-1] \
                if  isinstance(node_inputs, list) or (isinstance(layer[0],torch.nn.ConvTranspose2d) and layer[-2]==layer[i][-4:-2]) for node in graph['outputs']]):
                    node['inputs'][i+len(outputs)] = op2

    def visualize_graph(self):
        graph,  dotfile = dict(),  open('temp.dot', 'w')

        graph['inputs'],  graph['outputs'], inputs ,  opstack \
            = [],[], [], []
        
        for layer in self.model.__dict__.values(): 
            if isinstance(layer, torch.nn.Linear) or \
                (isinstance(layer, torch.nn.ConvTranspose2d) and not\
                 isinstance(layer,torch.nn.ModuleList)):
                    graph['inputs'] += [layer]

        dotfile = open('temp.dot','w')
        dotfile.write('digraph G { \nrankdir=LR;\n')
        dotfile.flush()
        
        inputs  = [node['inputs'] for node in graph['outputs']]

        for i, opstack in enumerate(list(zip(*graph['inputs']))):
            
            for j , layer in enumerate(graph['outputs']):
                for node in inputs[i]:
                    op1,op2  = layer[-4:-2] if len(layer) > 3 else [opstack], opstack
                    try:
                        op1.append(node + ['identity'] if (opstack==op1[0] and\
                            isinstance(layer[j][-1],torch.nn.ConvTranspose2d)) else\
                                [op if j == i + len(outputs) or \
                                layer[-3]==layer[i+len(outputs)][j] for op in layer])
                    except: pass

            dotfile = open('temp.dot','a')
            opstack += [[op['outputs'][0][-1]] for node in graph['outputs']]
            graph['outputs'] = [[op + ['identity'] if len(layer) > 3 else op for j , \
                layer in enumerate(op)] for i,op in enumerate(graph['inputs']) \
                        ]
                
            for i in range(-len(opstack),0):
                opstack[i][-1] += [op2[-j+len(outputs)][i] if len(layer) > 3 else op + ['skip'] \
                if isinstance(node,torch.nn.ConvTranspose2d)\
                        and node==opstack[i+len(outputs)] for j , layer in enumerate(graph['inputs'])]

            inputs = [node['inputs'] for node in graph['outputs']]
            outputs  = [[i] + [op[-3] if len(layer) > 3 else op if isinstance(layer,list)\
                and not (isinstance(layer[0][1], torch.nn.ConvTranspose2d) and\
                    layer[-2]==layer[j+len(outputs)][-4:-2]) for i in range(-len(opstack),0)] for j , op \
                    in enumerate([op + [[op[-3]]] if len(op)>3 else [op[:-1]]for i, op in\
                        zip(*graph['inputs'][:])])]
            
            for op2,op1 in list(zip(*outputs))[::-1]:
                opstack += [op + ['skip']]
                for j , layer in enumerate([op + [[op[-3]]] if len(layer) > 3 else\
                    [(layer[i][-4:-2] if i==j+len(outputs)-1 or layer[i]==op \
                        and not isinstance(node,torch.nn.ConvTranspose2d)\
                            for j in range(-len(opstack),0)] for node in graph['inputs'] ]\
                        for op in opstack]):
                    op[-3] += [op if len(op)>1 else op[j] for i , layer \
                    in enumerate([layer for layer in zip(*op)])]
                        
            opstack = [[op + ['skip']]  if not isinstance(node,torch.nn.ConvTranspose2d) \
                and (len(graph['inputs'][0][i][-1])>4 or graph[j]['outputs'][0][-3]\
                    == graph['outputs'][0][-3] + [graph['inputs'][j+len(outputs)][i][-1]])\
                        for i in range(-len(opstack),0)] + opstack]

            op1 = [[op[-4:-2] if len(layer)>5 else [op] \
            or layer[-2]==layer[i][-3]  for j , layer in enumerate(graph['inputs'][:])] for i,op in zip(*opstack) ]
    
            graph['outputs'] += list(zip(*op1)) + [[op] + [[op]]  if len(layer)>5 \
                else [op if isinstance(layer[0][1], torch.nn.ConvTranspose2d)\
                    and node==op for i in range(-len(opstack),0)] \
                        + [op for op,node in zip(*op) if not (isinstance(node,\
            torch.nn.ConvTranspose2d) and  len(graph['inputs'][j+len(outputs)][i][-1])>4)\
                or node==op] for i , layer in enumerate(graph['inputs'])]

            for j,layer in enumerate([op for opstack in graph['outputs']]) \
                : dotfile.write('subgraph cluster_{:s} {{\n'.format(j))
            for node in list(zip(*[layer[-1] if len(node) > 3 else node[:-4] + [layer][-1] for layer in opstack])):
                 dotfile.write('%s[label="%s",shape="record"]\n'%(node,node))
            for j , layer in enumerate([op for op in graph['outputs']]):
                dotfile.write('}\n')

            for i,layer in enumerate(graph['inputs']):

                dotfile.write('subgraph cluster_{:s} {{\n'.format(i))
                
                if not isinstance(layer[-1][0][-4],torch.nn.ConvTranspose2d):
                    
                    for node in layer[:-1]:
                        try :dotfile.write('%s[label="%s",shape="record"]\n'%(node,node))
                        
                        except TypeError as error: print(error);dotfile.flush()
                        
                    dotfile.write('}\n')

                    for i ,layer in enumerate([op for opstack in graph['outputs']]) :
                        try :dotfile.write('%s->%s[label="%s"]\n'%(layer[-2][-1],layer[:-3][0],layer[-4:-2]))
                        
                        except TypeError as error: print(error);dotfile.flush()
                        

                    for j , layer in enumerate([op + [op[-3]]  if len(node) >5 or not (isinstance(\
                node[i][j][1],torch.nn.ConvTranspose2d) and layer[-4:-2]==layer[:-3][0])for i,layer in\
                        zip(*layer)] for j , opstack in enumerate(graph['outputs'][:])] :
                        
                        dotfile.write('subgraph cluster_{:s} {{\n'.format(j))
                        try:
                            if isinstance(op[1],torch.nn.ConvTranspose2d): 
                                dotfile.write('%s[label="%s",shape="record"]\n'%(layer[-3][-4:-2],layer[:-2]))
                                for layer in zip(*op) :
                                    try:
                                        dotfile.write('%s->%s[label="%s"]\n'%(layer,op[1][j][0],op))
                                        
                                        dotfile.flush()
                                    except TypeError as error :print(error);dotfile.flush()

                        finally:  pass
                        
                        for node in op[:-2] + [op[-3]]:
                            try :dotfile.write('%s[label="%s",shape="record"]\n'%(node,node))
                            except TypeError as error: print(error);dotfile.flush()

                        dotfile.write('}\n')
                        
                        dotfile.flush()

        for i in range(-len(opstack),0):
            try : dotfile.write('%s->%s[label="%s"]\n'%(op[-2][-1],graph['outputs'][i][:-3][j][-4:],graph['outputs'][i][:-3][j]))
            except TypeError as error:print(error);dotfile.flush()

        dotfile.write('}\n')
        for layer in opstack[0]:
            try : dotfile.write('%s[label="%s",shape="record"]\n'%(layer,layer))

            finally: pass
        
        dotfile.close()