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
        self.linear = torch.nn.Linear(32, 3, bias=False)
        self.lrelu = torch.nn.LeakyReLU()

    def _make_param(slef, dims):
        return torch.nn.Parameter(torch.zeros(dims))

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 > 0)
        v3 = self._make_param(((- 1),))
        v4 = torch.where(v2, v1, v3)
        return self.lrelu(v4)



func = Model().to('cuda')



x = torch.randn(1, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -1: [-1]

jit:
Failed running call_function <built-in method zeros of type object at 0x7c4e354699e0>(*((-1,),), **{}):


from user code:
   File "<string>", line 28, in forward
  File "<string>", line 23, in _make_param


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''