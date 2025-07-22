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
        self.linear = torch.nn.Linear(576, 224)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) + x2
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = v2.T.unsqueeze(-3)
        x3 = v3 + v1
        x3.permute(0, 2, 1).T.transpose(-2, -1) + v2.unsqueeze(-3) + v2
        return x3 + v3



func = Model().to('cpu')


x1 = torch.randn(1, 224, 298)

x2 = torch.randn(1, 32, 224)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (298) must match the size of tensor b (32) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, s1, 224)), FakeTensor(..., size=(1, 32, 224))), **{}):
The size of tensor a (s1) must match the size of tensor b (32) at non-singleton dimension 1)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''