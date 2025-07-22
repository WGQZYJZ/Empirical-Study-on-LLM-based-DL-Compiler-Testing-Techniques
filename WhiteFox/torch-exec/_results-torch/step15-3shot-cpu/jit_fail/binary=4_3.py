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
        self.linear1 = torch.nn.Linear(23, 10)
        self.linear2 = torch.nn.Linear(10, 5)

    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = v1 + x2
        v3 = self.linear2(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 23)

x2 = torch.randn(1, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (5) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 10)), FakeTensor(..., size=(1, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 5]); but expected shape should be broadcastable to [1, 10]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''