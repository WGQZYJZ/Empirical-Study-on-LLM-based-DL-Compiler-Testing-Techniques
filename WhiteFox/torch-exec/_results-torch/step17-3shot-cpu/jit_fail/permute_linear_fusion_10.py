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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = x1.permute(-1, 0, 2, 3)
        t2 = self.linear(t1)
        t3 = t2.transpose(-2, -1)
        t4 = torch.matmul(t1, t3)
        return torch.nn.functional.relu(t4)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute(): duplicate dims are not allowed.

jit:
Failed running call_method permute(*(FakeTensor(..., size=(1, 2, 2, 2)), -1, 0, 2, 3), **{}):
Received an invalid permutation, [3, 0, 2, 3]!

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''