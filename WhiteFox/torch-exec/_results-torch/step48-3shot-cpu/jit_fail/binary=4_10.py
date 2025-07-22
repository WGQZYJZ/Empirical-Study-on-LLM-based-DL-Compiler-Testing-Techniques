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
        self.linear = torch.nn.Linear(5, 3)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 4, 5)

x2 = torch.randn(1, 4, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, s0, 3)), FakeTensor(..., size=(1, 4, 2))), **{}):
The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 2)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''