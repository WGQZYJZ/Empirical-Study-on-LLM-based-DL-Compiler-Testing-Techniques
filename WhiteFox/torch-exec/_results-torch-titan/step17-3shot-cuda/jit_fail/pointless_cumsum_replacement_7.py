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
        c = {}
        a = {}
        b['dtype'] = torch.complex128
        b['layout'] = torch.sparse_coo
        b['device'] = torch.device('cpu')
        c['dtype'] = torch.complex128
        c['layout'] = torch.strided
        c['device'] = torch.device('cpu')
        c['dtype_to'] = torch.complex128
        c['dtype_from'] = torch.complex64
        b['dtype_to'] = torch.complex64
        b['dtype_from'] = torch.complex128
        a['dtype'] = torch.float32
        a['layout'] = torch.strided
        a['device'] = torch.device('cpu')
        a['dtype_to'] = torch.float32
        a['dtype_from'] = torch.complex64
        t1 = torch.full([1, 3, 9, 1], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=c['dtype'])
        t3 = torch.addmm(t2, t2, t2)
        t4 = t3.to(dtype=a['dtype'])
        t5 = torch.addmm(t1, t1, t4)
        return t5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 9, 1, device='cpu')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
full(...) is not implemented for sparse layout

jit:
Failed running call_function <built-in method full of type object at 0x7581594699e0>(*([1, 3, 9, 1], 1), **{'dtype': torch.complex128, 'layout': torch.sparse_coo, 'device': device(type='cpu'), 'pin_memory': False}):
full(...) is not implemented for sparse layout

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''