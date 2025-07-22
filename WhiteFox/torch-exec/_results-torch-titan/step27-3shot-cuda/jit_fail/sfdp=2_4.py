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
        self.query_linear = torch.nn.Linear(3, 8)
        self.key_linear = torch.nn.Linear(3, 8)
        self.value_linear = torch.nn.Linear(3, 8)

    def forward(self, x1, x2):
        q1 = self.query_linear(x1)
        k1 = self.key_linear(x1)
        v1 = self.value_linear(x1)
        q2 = self.query_linear(x2)
        k2 = self.key_linear(x2)
        v2 = self.value_linear(x2)
        q3 = torch.matmul(q1, k2.transpose((- 2), (- 1)))
        k3 = torch.matmul(q2, k1.transpose((- 2), (- 1)))
        v3 = torch.matmul(q2, v1.transpose((- 2), (- 1)))
        v4 = torch.matmul(q1, v2.transpose((- 2), (- 1)))
        q4 = (q3 + k3)
        k4 = (q4 + k3)
        v5 = (v3 + v4)
        v6 = torch.matmul(q2, v5.transpose((- 2), (- 1)))
        return v6



func = Model().to('cuda')



x1 = torch.randn(1, 3, 4, 4)



x2 = torch.randn(1, 3, 4, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x4 and 3x8)

jit:
Failed running call_module L__self___query_linear(*(FakeTensor(..., device='cuda:0', size=(1, 3, 4, 4)),), **{}):
a and b must have same reduction dim, but got [12, 4] X [3, 8].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''