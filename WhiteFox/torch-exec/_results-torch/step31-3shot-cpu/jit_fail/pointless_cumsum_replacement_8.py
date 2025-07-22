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
        b['dtype'] = torch.bool
        b['layout'] = torch.sparse_coo
        b['device'] = torch.device('cpu')
        a['dtype'] = torch.uint8
        a['layout'] = torch.strided
        a['device'] = torch.device('cpu')
        a['dtype_to'] = torch.uint8
        a['dtype_from'] = torch.bool
        b['dtype_to'] = torch.bool
        b['dtype_from'] = torch.uint8
        t1 = torch.full([128, 128], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3



func = Model().to('cpu')


x1 = torch.randn(128, 128, device='cpu')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
full(...) is not implemented for sparse layout

jit:
Failed running call_function <built-in method full of type object at 0x7f824a796ec0>(*([128, 128], 1), **{'dtype': torch.bool, 'layout': torch.sparse_coo, 'device': device(type='cpu'), 'pin_memory': False}):
full(...) is not implemented for sparse layout

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''