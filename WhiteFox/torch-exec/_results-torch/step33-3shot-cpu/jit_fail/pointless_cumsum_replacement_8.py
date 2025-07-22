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
        a['dtype'] = torch.float16
        a['layout'] = torch.strided
        a['device'] = torch.device('cpu')
        a['dtype_to'] = torch.float32
        a['dtype_from'] = torch.float16
        b['dtype_to'] = torch.float16
        b['dtype_from'] = torch.float32
        t1 = torch.full([1, 134217728], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.mm(t2, t2)
        t4 = t3.to(dtype=b['dtype'])
        t5 = t4.masked_fill(t4.gt(2), 0.0)
        t6 = t5.masked_fill(t5.lt(-1), 3)
        return t6



func = Model().to('cpu')


x1 = torch.randn(1, 134217728, device='cpu')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x134217728 and 1x134217728)

jit:
Failed running call_function <built-in method mm of type object at 0x745402f96ec0>(*(FakeTensor(..., size=(1, 134217728), dtype=torch.float16), FakeTensor(..., size=(1, 134217728), dtype=torch.float16)), **{}):
a and b must have same reduction dim, but got [1, 134217728] X [1, 134217728].

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''