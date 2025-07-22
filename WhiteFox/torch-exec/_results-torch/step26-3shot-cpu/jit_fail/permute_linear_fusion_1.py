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
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(2, 32)
        self.weight = torch.nn.Parameter(torch.zeros(int(32)))
        self.bias = torch.nn.Parameter(torch.zeros(1))

    def forward(self, x):
        x = x.permute(0, 2, 1)
        x = torch.nn.functional.linear(x, self.linear.weight, self.linear.bias)
        x = torch.max(x, dim=-1)[0]
        x = x.unsqueeze(dim=-1)
        x = x + torch.max(x, dim=-1, keepdim=True)[0].to(self.weight.dtype)
        x = (x == -1).to(self.weight.dtype)
        x = torch.nn.functional.linear(x, self.weight, self.bias)
        x = torch.sum(torch.nn.functional.hardtanh(torch.nn.functional.tanh(x), -1.0, 1.0))
        return x



func = Model().to('cpu')


x = torch.randn(1, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat2 must be a matrix, got 1-D tensor

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 1)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
b must be 2D

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''