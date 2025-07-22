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
        b['dtype'] = torch.int16
        b['layout'] = torch.sparse_coo
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.bool
        a['layout'] = torch.sparse_coo
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.int16
        a['dtype_from'] = torch.bool
        b['dtype_to'] = torch.int16
        b['dtype_from'] = torch.bool
        t1 = torch.full([256], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 0)
        return t3



func = Model().to('cpu')



x1 = torch.randn(256, device='cuda:0', dtype=torch.float)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
full(...) is not implemented for sparse layout

jit:
Failed running call_function <built-in method full of type object at 0x76bfded96ec0>(*([256], 1), **{'dtype': torch.int16, 'layout': torch.sparse_coo, 'device': device(type='cuda', index=0), 'pin_memory': False}):
full(...) is not implemented for sparse layout

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''