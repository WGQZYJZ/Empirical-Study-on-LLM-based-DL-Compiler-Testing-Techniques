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
        self.linear = torch.nn.Linear(2, 3)
        self.linear3 = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v1 = torch.cat([x1, x1, x1], dim=-1)
        v2 = v1.permute(0, 2, 1)
        v21 = v2
        v22 = torch.nn.functional.relu(self.linear.weight) * v2 + self.linear.bias
        v2 = self.linear3(torch.nn.functional.relu(v22))
        v3 = v2.mean(dim=-2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (6) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(3, 2)), FakeTensor(..., size=(1, 6, 2))), **{}):
Attempting to broadcast a dimension of length 6 at -2! Mismatching argument at index 1 had torch.Size([1, 6, 2]); but expected shape should be broadcastable to [1, 3, 2]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''