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
        b['dtype'] = torch.int32
        b['layout'] = torch.strided
        b['device'] = torch.device('cpu')
        a['dtype'] = torch.float64
        a['layout'] = torch.strided
        a['device'] = torch.device('cpu')
        c = torch.addmm(x1, x2, x2, beta=0, alpha=1)
        d = torch.sum(c, dtype=b['dtype'], layout=b['layout'], device=b['device'])
        return d



func = Model().to('cpu')


x1 = torch.randn(2048, 9, device='cpu')

x2 = torch.randn(2048, 1024, device='cpu')

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2048x1024 and 2048x1024)

jit:
Failed running call_function <built-in method addmm of type object at 0x7b1b1a596ec0>(*(FakeTensor(..., size=(2048, 9)), FakeTensor(..., size=(2048, 1024)), FakeTensor(..., size=(2048, 1024))), **{'beta': 0, 'alpha': 1}):
a and b must have same reduction dim, but got [2048, 1024] X [2048, 1024].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''