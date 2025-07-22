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
        c = {}
        b['dtype'] = torch.float32
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.bool
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.uint8
        a['dtype_from'] = torch.bool
        b['dtype_to'] = torch.uint8
        b['dtype_from'] = torch.float32
        c['dtype'] = torch.float64
        c['layout'] = torch.strided
        c['device'] = torch.device('cuda:0')
        c['dtype_to'] = torch.float32
        c['dtype_from'] = torch.float64
        t1 = torch.full([1024, 2], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = t2.boolmask()
        t4 = torch.cumsum(t3, 1)
        t5 = t4.boolmask()
        t6 = t5.to(dtype=c['dtype'])
        t7 = torch.cumsum(t6, 1)
        return t7



func = Model().to('cpu')


x1 = torch.randn(1024, 2, device='cuda:0')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute 'boolmask'

jit:
Failed running call_method boolmask(*(FakeTensor(..., device='cuda:0', size=(1024, 2), dtype=torch.bool),), **{}):
'FakeTensor' object has no attribute 'boolmask'

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''