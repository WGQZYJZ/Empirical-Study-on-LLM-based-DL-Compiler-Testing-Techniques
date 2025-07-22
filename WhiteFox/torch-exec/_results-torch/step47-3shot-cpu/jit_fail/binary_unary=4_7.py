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
        self.linear = torch.nn.Linear(8, 5)

    def forward(self, x1, other=torch.tensor([[0, 0, 0, 0, 0, 1, 1, 1]])):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.nn.functional.relu(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 5)), FakeTensor(..., size=(1, s1), dtype=torch.int64)), **{}):
The size of tensor a (5) must match the size of tensor b (s1) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''