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
        b['device'] = torch.device('cpu')
        a['dtype'] = torch.uint8
        a['layout'] = torch.strided
        a['device'] = torch.device('cpu')
        a['dtype_to'] = torch.float32
        a['dtype_from'] = torch.uint8
        b['dtype_to'] = torch.float32
        b['dtype_from'] = torch.uint8
        t1 = torch.full([1000, 1000], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(memory_format=torch.channels_last)
        t4 = torch.view_as_real(t2)
        t3 = torch.cumsum(t4, 2)
        return t3



func = Model().to('cpu')


x1 = torch.randn(5, 2, 3, 3, device='cpu')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
required rank 4 tensor to use channels_last format

jit:
Failed running call_method to(*(FakeTensor(..., size=(1000, 1000)),), **{'memory_format': torch.channels_last}):
required rank 4 tensor to use channels_last format

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''