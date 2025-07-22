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

    def forward(self, x):
        y = torch.arange(40.0)
        x = x + y
        y = y + x
        x = y.clamp(max=10)
        y = x.clamp(max=10)
        z = torch.cat([x, x, y, x, y], dim=0)
        return x



func = Model().to('cpu')


x = torch.arange(10.0)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (40) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0,)), FakeTensor(..., size=(40,))), **{}):
The size of tensor a (s0) must match the size of tensor b (40) at non-singleton dimension 0)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''