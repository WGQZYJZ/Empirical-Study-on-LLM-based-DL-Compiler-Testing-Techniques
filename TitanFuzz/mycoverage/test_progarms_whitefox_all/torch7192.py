import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        b = {}
        a = {}
        b['dtype'] = torch.complex128
        b['layout'] = torch.sparse_coo
        b['device'] = torch.device('cpu')
        a['dtype'] = torch.int64
        a['layout'] = torch.sparse_coo
        a['device'] = torch.device('cpu')
        a['dtype_to'] = torch.int64
        a['dtype_from'] = torch.long
        b['dtype_to'] = torch.float64
        b['dtype_from'] = torch.long
        t1 = torch.full([1024], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 0)
        return t3
m = Model()
# Inputs to the model
x1 = torch.randn(1024, dtype=torch.long, device='cpu')
