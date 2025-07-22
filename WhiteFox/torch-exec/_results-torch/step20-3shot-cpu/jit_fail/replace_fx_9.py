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
        return x1 + math.exp(x1)



func = Model().to('cpu')


x1 = torch.randn(4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
only one element tensors can be converted to Python scalars

jit:
Failed running call_function <built-in function exp>(*(FakeTensor(..., size=(s0,)),), **{}):
only one element tensors can be converted to Python scalars

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''