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

    def __init__(self, a=1.0, b=2.0):
        super().__init__()
        self.a = a
        self.b = b

    def forward(self, x1):
        x2 = torch.mean(x1)
        x3 = torch.rand_like(x1)
        x4 = torch.zeros_like(x3).to(torch.double)
        x5 = torch.randn_like(x1)
        x6 = torch.randint_like(x1, high=10)
        x7 = self.a * x1 + self.b
        x10 = torch.where(x2 > 1, x2, torch.relu(x5))
        return x4 + x5 + x6 + x7 + x10



func = Model().to('cpu')


x1 = torch.randint(low=1, high=100, size=(3, 4))

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mean(): could not infer output dtype. Input dtype must be either a floating point or complex dtype. Got: Long

jit:
Failed running call_function <built-in method mean of type object at 0x7a484bf96ec0>(*(FakeTensor(..., size=(3, 4), dtype=torch.int64),), **{}):
mean(): could not infer output dtype. Input dtype must be either a floating point or complex dtype. Got: torch.int64

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''