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
        self.linear = torch.nn.Linear(8, 16)

    def forward(self, x1, other=None):
        t1 = self.linear(x1)
        t2 = t1 + other
        t3 = torch.relu(t2)
        return t3


func = Model().to('cpu')


x1 = torch.randn(1, 8)

x2 = torch.randn(1, 8)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 16)), FakeTensor(..., size=(1, s1))), **{}):
The size of tensor a (16) must match the size of tensor b (s1) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''