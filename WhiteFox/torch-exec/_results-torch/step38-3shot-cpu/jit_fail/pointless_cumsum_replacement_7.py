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

    def forward(self, x1):
        b = {}
        a = {}
        b['dtype'] = torch.float32
        b['layout'] = torch.strided
        b['device'] = torch.device('cpu:0')
        a['dtype'] = torch.float64
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.float16
        a['dtype_from'] = torch.float32
        b['dtype_to'] = torch.float16
        b['dtype_from'] = torch.float64
        t1 = torch.full([-5, 10, 8], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3



func = Model().to('cpu')


x1 = torch.randn(1000, 10, 8, device='cuda:0')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -5: [-5, 10, 8]

jit:
Failed running call_function <built-in method full of type object at 0x75b4b0996ec0>(*([-5, 10, 8], 1), **{'dtype': torch.float32, 'layout': torch.strided, 'device': device(type='cpu', index=0), 'pin_memory': False}):
Trying to create tensor with negative dimension -5: [-5, 10, 8]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''