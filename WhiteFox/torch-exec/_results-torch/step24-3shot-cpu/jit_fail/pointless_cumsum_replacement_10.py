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
        b['dtype'] = torch.uint16
        a['dtype'] = torch.int32
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        a['shape'] = (2048,)
        b['shape'] = (2048,)
        a['dtype_to'] = torch.int32
        a['dtype_from'] = torch.uint16
        b['dtype_to'] = torch.int32
        b['dtype_from'] = torch.uint16
        t1 = torch.full(b['shape'], 1, dtype=a['dtype'], layout=a['layout'], device=a['device'], pin_memory=False)
        t2 = t1.to(dtype=b['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3



func = Model().to('cpu')


x1 = torch.randn(2048, device='cuda:0')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 1)

jit:
Failed running call_function <built-in method cumsum of type object at 0x776121796ec0>(*(FakeTensor(..., device='cuda:0', size=(2048,), dtype=torch.uint16), 1), **{}):
Dimension out of range (expected to be in range of [-1, 0], but got 1)

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''