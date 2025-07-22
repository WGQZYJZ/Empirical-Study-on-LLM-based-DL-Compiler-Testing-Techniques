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
        v4 = x1
        v1 = torch.nn.functional.linear(v4, torch.randn(2, 2), torch.randn(2))
        a1 = v1.numpy()
        v2 = a1.permute((0, 2, 1))
        a2 = torch.from_numpy(v2).float()
        return a2



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'numpy.ndarray' object has no attribute 'permute'

jit:
Failed running call_function <Wrapped method <original permute>>(*(FakeTensor(..., size=(1, 2, 2)), (0, 2, 1)), **{}):
'ndarray' object has no attribute 'permute'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''