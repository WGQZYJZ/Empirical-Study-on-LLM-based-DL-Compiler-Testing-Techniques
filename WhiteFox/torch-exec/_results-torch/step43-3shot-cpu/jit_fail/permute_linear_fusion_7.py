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
        self.linear1 = torch.nn.Linear(2, 2)
        self.softmax1 = torch.nn.Softmax()
        self.softmax2 = torch.nn.Softmax()

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)
        v3 = torch.stack([self.softmax1(v2)[0], self.softmax2(v2)[1]], dim=-1)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
index 1 is out of bounds for dimension 0 with size 1

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., size=(1, 2, 2)), 1), **{}):
index 1 is out of bounds for dimension 0 with size 1

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''