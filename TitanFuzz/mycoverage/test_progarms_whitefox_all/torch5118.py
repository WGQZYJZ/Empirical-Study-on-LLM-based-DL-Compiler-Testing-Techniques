import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        b = {}
        a = {}
        b['dtype'] = torch.half
        b['layout'] = torch.strided
        b['device'] = torch.device('cpu')
        a['dtype'] = torch.long
        a['layout'] = torch.strided
        a['device'] = torch.device('cpu')
        a['dtype_to'] = torch.half
        a['dtype_from'] = torch.long
        b['dtype_to'] = torch.float32
        b['dtype_from'] = torch.half
        t1 = torch.full([784, 1024], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3
m = Model()
# Inputs to the model
x1 = torch.randn(784, 1024, device='cpu')
