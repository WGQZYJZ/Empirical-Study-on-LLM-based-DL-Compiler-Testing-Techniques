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
        self.linear1 = torch.nn.Linear(20, 40)
        self.linear2 = torch.nn.Linear(40, 50)
        self.linear3 = torch.nn.Linear(50, 10)

    def forward(self, x1, other=None):
        v1 = self.linear1(x1)
        v2 = v1 + other if other is not None else v1
        v3 = torch.nn.functional.relu(v2)
        v4 = self.linear2(v3)
        v5 = v4 + other if other is not None else v4
        v6 = torch.nn.functional.relu(v5)
        v7 = self.linear3(v6)
        return v7


func = Model().to('cpu')


x1 = torch.randn(2, 20)

other = torch.randn(2, 50)

test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
The size of tensor a (40) must match the size of tensor b (50) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(2, 40)), FakeTensor(..., size=(2, 50))), **{}):
Attempting to broadcast a dimension of length 50 at -1! Mismatching argument at index 1 had torch.Size([2, 50]); but expected shape should be broadcastable to [2, 40]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''