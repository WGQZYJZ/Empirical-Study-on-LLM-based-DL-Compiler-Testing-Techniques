import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        b = {}
        a = {}
        a['dtype'] = torch.float64
        a['layout'] = torch.strided
        a['device'] = torch.device('cpu')
        b['dtype'] = torch.float16
        b['layout'] = torch.strided
        b['device'] = torch.device('cpu')
        a['dtype_to'] = torch.float64
        a['dtype_from'] = torch.float64
        b['dtype_to'] = torch.float16
        b['dtype_from'] = torch.float64
        t1 = torch.full([256, 1024], 1.0, dtype=a['dtype'], layout=a['layout'], device=a['device'], pin_memory=False)
        t2 = t1.to(dtype=b['dtype'])
        t3 = t2.to(dtype=a['dtype'])
        t4 = torch.add(t3, x1)
        t5 = torch.mul(t4, x2)
        t6 = torch.cumsum(t5, 1)
        return t6



func = Model().to('cpu')


x1 = torch.tensor([-2.6429, 0.0329, 0.94, 0.589, 0.3317, 0.294, 0.6286, -0.3628, 0.9315, 0.6357], requires_grad=True, device='cpu')


x2 = torch.tensor([1.0194, -0.8455, -0.0254, 0.3436, 0.0239, -0.4474, -0.891, -0.2121, 0.7194, 0.262], requires_grad=True, dtype=torch.float64, device='cpu')

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (1024) must match the size of tensor b (10) at non-singleton dimension 1

jit:
Failed running call_function <built-in method add of type object at 0x722687196ec0>(*(FakeTensor(..., size=(256, 1024), dtype=torch.float64), FakeTensor(..., size=(10,))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([10]); but expected shape should be broadcastable to [256, 1024]

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''