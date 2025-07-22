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
        b['dtype'] = torch.qint8
        b['layout'] = torch.sparse_coo
        b['device'] = torch.device('cpu')
        a['dtype'] = torch.float16
        a['layout'] = torch.sparse_coo
        a['device'] = torch.device('cpu')
        a['dtype_to'] = torch.float32
        a['dtype_from'] = torch.float16
        b['dtype_to'] = torch.float16
        b['dtype_from'] = torch.float32
        t1 = torch.full([1, 1], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 0)
        return t3



func = Model().to('cuda')


x1 = torch.randn(1, 1, device='cpu')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
full(...) is not implemented for sparse layout

jit:
Failed running call_function <built-in method full of type object at 0x78d40c996ec0>(*([1, 1], 1), **{'dtype': torch.qint8, 'layout': torch.sparse_coo, 'device': device(type='cpu'), 'pin_memory': False}):
full(...) is not implemented for sparse layout

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''