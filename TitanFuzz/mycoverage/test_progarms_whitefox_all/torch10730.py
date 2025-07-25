import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        b = {}
        a = {}
        b['dtype'] = torch.int8
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:2')
        a['dtype'] = torch.double
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:2')
        a['dtype_to'] = torch.int8
        a['dtype_from'] = torch.double
        b['dtype_to'] = torch.int8
        b['dtype_from'] = torch.double
        t1 = torch.full([1, 2], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3
m = Model()
# Inputs to the model
x1 = 2
