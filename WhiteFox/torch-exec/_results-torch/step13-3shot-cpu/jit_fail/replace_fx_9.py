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

    def forward(self, x1, x2, x3):
        x1 = torch.nn.functional.dropout(x1, p=0.05)
        x2 = torch.rand_like(x2)
        x3 = torch.nn.functional.dropout(x3, p=float(x2.shape[1] < 8))
        return torch.sum(x1 + x2 + x3)



func = Model().to('cpu')


x1 = torch.randn(5, 10, 5)

x2 = torch.randn(5, 20, 5)

x3 = torch.randn(20, 10)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (20) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, s1, 5)), FakeTensor(..., size=(5, 20, 5))), **{}):
The size of tensor a (s1) must match the size of tensor b (20) at non-singleton dimension 1)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''